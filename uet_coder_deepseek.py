import argparse
import os
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, GenerationConfig, BitsAndBytesConfig
from peft import PeftModel


def load_model():
    print("Loading base model...")

    model_name = "deepseek-ai/deepseek-coder-1.3b-instruct"

    quant_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.float16,
    bnb_4bit_use_double_quant=True,
    )

    base_model = AutoModelForCausalLM.from_pretrained(
    model_name,
    quantization_config=quant_config,
    device_map="auto",
    trust_remote_code=True,
    )

    adapter_path = "lora_weight_deepseek"  
    print("Loading fine-tuned adapter...")
    # Load tokenizer
    tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
    tokenizer.pad_token = tokenizer.eos_token

    # Gắn adapter QLoRA
    model = PeftModel.from_pretrained(base_model, adapter_path)
    model.eval()
    return model, tokenizer


def build_prompt(problem_text: str) -> str:
    prompt = f"""
            <|system|>
            You are a highly skilled Python engineer. Your task is to provide correct and optimal Python solutions for coding problems.
            
            <|user|>
            ### Problem
            {problem_text}
            
            ### Write the solution in Python.
            
            <|assistant|>
            ```python
            """
    return prompt


def generate_code(model, tokenizer, prompt: str) -> str:
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    inputs = tokenizer(prompt, return_tensors="pt").to(device)


    outputs = model.generate(
        **inputs,
        max_new_tokens=400,
        do_sample=False,
        pad_token_id=tokenizer.eos_token_id,
        eos_token_id=tokenizer.eos_token_id
    )

    generated = tokenizer.decode(outputs[0], skip_special_tokens=True)
    code = generated[len(prompt):]
    if "```" in code:
        code = code.split("```")[0]
    return code.strip()


def main():
    parser = argparse.ArgumentParser(description="UET Coder - DM BAO")
    parser.add_argument("--problem", required=True, help="Path to the problem markdown file (.md)")
    parser.add_argument("--output", required=True, help="Path to save the generated solution (.py)")
    args = parser.parse_args()

    # Đọc đề bài
    if not os.path.exists(args.problem):
        raise FileNotFoundError(f"Problem file not found: {args.problem}")

    with open(args.problem, "r", encoding="utf-8") as f:
        problem_text = f.read()

    # Build prompt
    prompt = build_prompt(problem_text)

    # Load model
    model, tokenizer = load_model()

    # Generate solution
    print("Generating solution...")
    generated_code = generate_code(model, tokenizer, prompt)

    output_dir = os.path.dirname(args.output)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)

    # Ghi file
    with open(args.output, "w", encoding="utf-8") as f:
        f.write(
"""
from typing import *
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
