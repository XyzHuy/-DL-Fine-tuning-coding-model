import argparse
import os
import re
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
from peft import PeftModel

ADAPTER_PATH = "qwen-finetuned-lora"
MODEL_NAME = "Qwen/Qwen2.5-3B-Instruct"

# Pre-compile Regex để tối ưu tốc độ xử lý chuỗi
CODE_BLOCK_PATTERN = re.compile(r"```python\n(.*?)\n```", re.DOTALL)

# Boilerplate code cho file output
BOILERPLATE = """from typing import *
from functools import *
from collections import *
from itertools import *
from heapq import *
from bisect import *
from string import *
from operator import *
from math import *

inf = float('inf')

"""

def load_optimized_model():
    print(f"Loading model...")

    bnb_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_compute_dtype=torch.bfloat16,
        bnb_4bit_use_double_quant=True,
    )

    base_model = AutoModelForCausalLM.from_pretrained(
        MODEL_NAME,
        quantization_config=bnb_config,
        device_map="auto",
        trust_remote_code=True,
        attn_implementation="sdpa",  # FASTER attention
    )

    model = PeftModel.from_pretrained(base_model, ADAPTER_PATH)
    model.eval()

    model = model.half().to("cuda")

    if torch.__version__ >= "2.1":
        model = torch.compile(model)

    torch.set_grad_enabled(False)

    torch.backends.cuda.matmul.allow_tf32 = False
    torch.backends.cudnn.allow_tf32 = False

    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, trust_remote_code=True)
    tokenizer.pad_token = tokenizer.eos_token

    return model, tokenizer

def prepare_prompt_and_tokenize(tokenizer, problem_text: str):
    system_prompt = (
        "You are an expert Python programmer and problem solver. "
        "You will be given LeetCode-style problems and must generate structured Python code solutions that pass all the test cases "
        "Always return a class named 'Solution' with the required method, and include an alias function "
        "outside the class that calls the method."
    )

    user_prompt = problem_text + (
        "\n\nPlease implement the solution using a class named `Solution` "
        "with the method matching the function signature. "
        "Include an alias function outside the class that calls the method."
    )
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ]

    inputs = tokenizer.apply_chat_template(
        messages,
        tokenize=True,
        add_generation_prompt=True,
        return_tensors="pt",
        return_dict=True
    ).to("cuda")

    return inputs


@torch.inference_mode()
def generate_solution(model, tokenizer, inputs):
    output_ids = model.generate(
        **inputs,
        max_new_tokens=512,
        do_sample=False,
        pad_token_id=tokenizer.eos_token_id,
        use_cache=True,
    )

    # Chỉ decode phần token mới sinh ra
    generated_ids = output_ids[0][inputs["input_ids"].shape[1]:]
    return tokenizer.decode(generated_ids, skip_special_tokens=True).strip()


def extract_code(text: str) -> str:
    match = CODE_BLOCK_PATTERN.search(text)
    return match.group(1).strip() if match else text


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--problem", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    if not os.path.exists(args.problem):
        raise FileNotFoundError(f"File not found: {args.problem}")

    # 1. Read problem text
    with open(args.problem, "r", encoding="utf-8") as f:
        problem_text = f.read()

    # 2. Load model (optimized)
    model, tokenizer = load_optimized_model()

    # 3. Tokenize
    inputs = prepare_prompt_and_tokenize(tokenizer, problem_text)

    # 4. Generate solution
    print("Generating...")
    raw_output = generate_solution(model, tokenizer, inputs)
    print("Extract code from output....")
    final_code = extract_code(raw_output)

    # 5. Save output
    output_dir = os.path.dirname(args.output)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
    with open(args.output, "w", encoding="utf-8") as f:
        f.write(BOILERPLATE + final_code + "\n")

    print(f"Done. Saved to {args.output}")

if __name__ == "__main__":
    main()
