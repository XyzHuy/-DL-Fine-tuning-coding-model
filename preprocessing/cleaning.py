import os
import re

PROBLEMS_DIR = "problems"
SOLUTIONS_DIR = "solution"

# Regex để lấy số thứ tự {nums} từ filename
problem_re = re.compile(r"Problem(\d+)\.md$")
solution_re = re.compile(r"Solution(\d+)\.py$")

# Lấy danh sách solution hiện có
solution_nums = set()
for fn in os.listdir(SOLUTIONS_DIR):
    m = solution_re.match(fn)
    if m:
        solution_nums.add(int(m.group(1)))

# Duyệt problems, xóa file không có solution
deleted_files = []
for fn in os.listdir(PROBLEMS_DIR):
    m = problem_re.match(fn)
    if not m:
        continue
    num = int(m.group(1))
    if num not in solution_nums:
        path = os.path.join(PROBLEMS_DIR, fn)
        os.remove(path)
        deleted_files.append(fn)

print(f"Deleted {len(deleted_files)} problem(s) with no solution:")
for f in deleted_files:
    print(f"  - {f}")
