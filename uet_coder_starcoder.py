import argparse
import os
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, GenerationConfig, BitsAndBytesConfig
from peft import PeftModel

# Load fine-tune model
def load_model():
    print("Loading base model...")
    quant_config = BitsAndBytesConfig(load_in_4bit=True)

    base_model = AutoModelForCausalLM.from_pretrained(
        "bigcode/starcoder2-3b",
        quantization_config=quant_config,
        dtype=torch.float16,
        device_map="auto"
    )

    print("Loading fine-tuned adapter...")
    model = PeftModel.from_pretrained(base_model, "lora_weight_starcoder")

    tokenizer = AutoTokenizer.from_pretrained("bigcode/starcoder2-3b")
    return model, tokenizer


def build_prompt(problem_text: str) -> str:
    return f"""### Problem:
{problem_text.strip()}

"Instruction: Write clean and efficient Python code that correctly solves the problem."
"The solution should be the most optimal approach in terms of time and space complexity."
"Do not include testing or extra text.\n"

### Solution:
"""


def generate_code(model, tokenizer, prompt: str) -> str:
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    inputs = tokenizer(
        prompt,
        return_tensors="pt",
        truncation=True,
        max_length=2048
    ).to(device)

    generation_config = GenerationConfig(
        max_new_tokens=256,
        do_sample=True,
        temperature=0.2,
        top_p=0.95,
        pad_token_id=tokenizer.eos_token_id,
        eos_token_id=tokenizer.eos_token_id
    )

    with torch.no_grad():
        outputs = model.generate(**inputs, generation_config=generation_config)

    full_output = tokenizer.decode(outputs[0], skip_special_tokens=True)

    generated_code = full_output.split("### Solution:")[-1].strip()
    generated_code = generated_code.split("<|end_of_solution|>")[0].strip()

    return generated_code


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
        f.write(generated_code + "\n")

    print(f"Solution saved to {args.output}")
    print("=== Generated Code ===")
    print(generated_code)


if __name__ == "__main__":
    main()
