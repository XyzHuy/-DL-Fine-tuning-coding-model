import argparse
import os
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
from peft import PeftModel


def load_model(adapter_path: str):
    print("Loading base model...")

    model_name = "Qwen/Qwen2.5-Coder-3B-Instruct"

    quant_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_compute_dtype=torch.bfloat16,  # Đổi thành bfloat16 để phù hợp với fine-tune
        bnb_4bit_use_double_quant=True,
    )

    base_model = AutoModelForCausalLM.from_pretrained(
        model_name,
        quantization_config=quant_config,
        device_map="auto",
        trust_remote_code=True,
    )

    print("Loading fine-tuned adapter...")
    tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
    tokenizer.pad_token = tokenizer.eos_token

    model = PeftModel.from_pretrained(base_model, adapter_path)
    model.eval()
    return model, tokenizer


def build_messages(problem_text: str) -> list:
    system_prompt = (
        "You are an expert Python programmer and problem solver. "
        "You will be given LeetCode-style problems and must generate structured Python code solutions. "
        "Always return a class named 'Solution' with the required method, and include an alias function "
        "outside the class that calls the method. Ensure your code includes detailed comments and "
        "follows Python best practices."
    )

    user_prompt = problem_text + (
        "\n\nPlease implement the solution using a class named `Solution` "
        "with the method matching the function signature. "
        "Include an alias function outside the class that calls the method."
    )

    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ]


def generate_code(model, tokenizer, messages: list) -> str:
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    # Dùng apply_chat_template để giữ đúng định dạng cho Qwen
    prompt = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True  # Có <im_start>assistant\n
    )

    inputs = tokenizer(
        prompt,
        return_tensors="pt",
        truncation=True,
        max_length=2048,
    ).to(device)

    with torch.inference_mode():
        output_ids = model.generate(
            **inputs,
            max_new_tokens=1024,
            temperature=0.1,
            do_sample=False,
            pad_token_id=tokenizer.eos_token_id,
        )

    # Decode chỉ phần mới sinh (loại bỏ phần prompt)
    generated = tokenizer.decode(
        output_ids[0][inputs["input_ids"].shape[1]:],
        skip_special_tokens=True
    )
    return generated.strip()


def extract_code(text: str) -> str:
    """
    Trích xuất phần code từ output nếu có khối ```python
    """
    import re
    pattern = r"```python\n(.*?)\n```"
    match = re.search(pattern, text, re.DOTALL)
    if match:
        return match.group(1).strip()
    # Nếu không tìm thấy, trả về toàn bộ
    return text


def main():
    parser = argparse.ArgumentParser(description="UET Coder - Qwen-based")
    parser.add_argument("--problem", required=True, help="Path to the problem markdown file (.md)")
    parser.add_argument("--output", required=True, help="Path to save the generated solution (.py)")
    parser.add_argument("--adapter", default="qwen-finetuned-lora", help="Path to the LoRA adapter folder")
    args = parser.parse_args()

    # Đọc đề bài
    if not os.path.exists(args.problem):
        raise FileNotFoundError(f"Problem file not found: {args.problem}")

    with open(args.problem, "r", encoding="utf-8") as f:
        problem_text = f.read()

    # Load model
    model, tokenizer = load_model(args.adapter)

    # Tạo messages
    messages = build_messages(problem_text)

    # Generate solution
    print("Generating solution...")
    generated_code_full = generate_code(model, tokenizer, messages)
    generated_code = extract_code(generated_code_full)

    output_dir = os.path.dirname(args.output)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)

    # Ghi file với boilerplate
    with open(args.output, "w", encoding="utf-8") as f:
        f.write(
"""from typing import *
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
            +
            generated_code + "\n")

    print(f"Solution saved to {args.output}")
    print("=== Generated Code ===")
    print(generated_code)


if __name__ == "__main__":
    main()