import os
import re
import shutil
from pathlib import Path

# --- Cấu hình ---
PYTHON_DIR = Path("../data/python")
PROBLEM_DIR = Path("../data/problems")
SOLUTION_DIR = Path("../data/solution")
SOLUTION_DIR.mkdir(exist_ok=True)

def extract_problem_ids_from_problems():
    """Lấy danh sách id từ các file Problem{id}.md"""
    ids = []
    for file in PROBLEM_DIR.glob("Problem*.md"):
        match = re.match(r"Problem(\d+)\.md", file.name)
        if match:
            ids.append(int(match.group(1)))
    return sorted(set(ids))

def extract_id_from_filename(filename):
    """Trích id (int) từ tên file python, bỏ số 0 đầu"""
    match = re.match(r"(\d+)_", filename)
    if match:
        return int(match.group(1))
    return None

def filter_and_copy_solutions():
    valid_ids = extract_problem_ids_from_problems()
    print(f" Found {len(valid_ids)} valid problem IDs: {valid_ids[:20]}{'...' if len(valid_ids) > 20 else ''}")

    count = 0
    for file in PYTHON_DIR.glob("*.py"):
        qid = extract_id_from_filename(file.name)
        if qid and qid in valid_ids:
            new_name = f"Solution{qid}.py"
            dst = SOLUTION_DIR / new_name
            shutil.copy(file, dst)
            count += 1
            print(f" Copied: {file.name} -> {dst.name}")
        else:
            print(f"⏭Skipped: {file.name}")

    print(f"\n {count} solution files copied to '{SOLUTION_DIR}'")

if __name__ == "__main__":
    filter_and_copy_solutions()
