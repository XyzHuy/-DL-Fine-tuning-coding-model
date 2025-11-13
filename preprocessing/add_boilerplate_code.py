import os
import re
import textwrap

PROBLEM_DIR = "../data/problems"
SOLUTION_DIR = "../data/solution"

def extract_boilerplate(solution_code: str) -> str:
    """
    Phân loại file solution để trích boilerplate code phù hợp.
    """
    # Giữ comment định nghĩa cấu trúc (nếu có)
    definition_lines = []
    for line in solution_code.splitlines():
        if line.strip().startswith("# Definition"):
            definition_lines.append(line)
        elif line.strip().startswith("class ") or line.strip().startswith("def "):
            break

    # ==== Loại 4: Chỉ có class ====
    if re.search(r"^class\s+\w+", solution_code, re.M) and not re.search(r"^def\s+\w+", solution_code, re.M):
        class_block = extract_class_structure(solution_code)
        return "\n".join(definition_lines + [class_block])

    # ==== Loại 3: Có class và def ====
    if "class " in solution_code:
        # Giữ lại comment + class đầu tiên + def đầu tiên bên ngoài class
        class_part = extract_first_class(solution_code)
        first_def = extract_first_function(solution_code, outside_class=True)
        return "\n".join(definition_lines + [class_part, first_def])

    # ==== Loại 2: Nhiều def ====
    defs = re.findall(r"^\s*def\s+\w+\s*\([^)]*\)\s*(?:->\s*[^\s:]+)?\s*:", solution_code, re.M)
    if len(defs) >= 1:
        first_def = defs[0]
        return first_def + "\n    ..."

    # ==== Loại 1: Một def duy nhất ====
    single_def = re.search(r"^\s*def\s+\w+\s*\([^)]*\)\s*(?:->\s*[^\s:]+)?\s*:", solution_code, re.M)
    if single_def:
        return single_def.group(0) + "\n    ..."

    return ""  # fallback


def extract_class_structure(code: str) -> str:
    """
    Dành cho loại 4: chỉ có class, xóa thân method, để lại dấu ...
    """
    lines = code.splitlines()
    result = []
    inside_func = False
    func_indent = None

    for line in lines:
        if re.match(r"^\s*class\s+\w+", line):
            result.append(line)
            continue

        # Khi gặp def, chỉ ghi định nghĩa + thân là ...
        m = re.match(r"^(\s*)def\s+\w+\s*\(.*\):", line)
        if m:
            indent = m.group(1)
            result.append(line)
            result.append(f"{indent}    ...")
            inside_func = True
            func_indent = len(indent)
            continue

        # Khi rời khỏi 1 hàm
        if inside_func and (not line.strip() or len(line) <= func_indent):
            inside_func = False

    return "\n".join(result)


def extract_first_class(code: str) -> str:
    """
    Lấy class đầu tiên (nguyên văn)
    """
    pattern = r"^class\s+\w+\s*\(?.*?:"
    match = re.search(pattern, code, re.M)
    if not match:
        return ""
    start = match.start()
    # Lấy block class (cho đến hết hoặc def bên ngoài)
    lines = code[match.start():].splitlines()
    collected = []
    indent_level = None
    for line in lines:
        if re.match(r"^def\s+\w+", line):  # dừng khi gặp def bên ngoài
            break
        if indent_level is None and line.strip():
            indent_level = len(line) - len(line.lstrip())
        collected.append(line)
    return "\n".join(collected)


def extract_first_function(code: str, outside_class=False) -> str:
    """
    Lấy hàm đầu tiên (nếu outside_class=True, chỉ lấy hàm ngoài class)
    """
    pattern = r"^\s*def\s+\w+\s*\([^)]*\)\s*(?:->\s*[^\s:]+)?\s*:"
    lines = code.splitlines()
    for line in lines:
        if re.match(pattern, line):
            if outside_class:
                # bỏ qua def nằm trong class
                indent = len(line) - len(line.lstrip())
                if indent > 0:
                    continue
            return line + "\n    ..."
    return ""


def append_boilerplate_to_md(problem_path, boilerplate_code):
    with open(problem_path, "a", encoding="utf-8") as f:
        f.write("\n\nBoilerplate code:\n")
        f.write("```python\n")
        f.write(boilerplate_code.strip() + "\n")
        f.write("```\n")


def process_all():
    for file in os.listdir(PROBLEM_DIR):
        if not file.endswith(".md"):
            continue

        problem_num = re.findall(r"\d+", file)
        if not problem_num:
            continue

        num = problem_num[0]
        sol_file = f"Solution{num}.py"
        sol_path = os.path.join(SOLUTION_DIR, sol_file)
        prob_path = os.path.join(PROBLEM_DIR, file)

        if not os.path.exists(sol_path):
            print(f"⚠️  Missing {sol_file}, skipping")
            continue

        with open(sol_path, "r", encoding="utf-8") as f:
            sol_code = f.read()

        boilerplate = extract_boilerplate(sol_code)
        if not boilerplate.strip():
            print(f"Cannot extract from {sol_file}")
            continue

        append_boilerplate_to_md(prob_path, boilerplate)
        print(f"Added boilerplate to {file}")


if __name__ == "__main__":
    process_all()
    print("\n✨ Done adding boilerplate to all .md files!")
