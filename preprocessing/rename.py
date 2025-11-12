import os
import re

PROBLEMS_DIR = "problems"
SOLUTIONS_DIR = "solution"

# Regex nhận diện số trong tên file
problem_re = re.compile(r"Problem(\d+)\.md$")
solution_re = re.compile(r"Solution(\d+)\.py$")

def sorted_files_by_num(directory, pattern):
    """Trả về list (old_path, num) đã sắp xếp tăng dần"""
    files = []
    for name in os.listdir(directory):
        m = pattern.match(name)
        if m:
            num = int(m.group(1))
            files.append((name, num))
    return sorted(files, key=lambda x: x[1])

# Lấy danh sách đã sắp xếp
problem_files = sorted_files_by_num(PROBLEMS_DIR, problem_re)
solution_files = sorted_files_by_num(SOLUTIONS_DIR, solution_re)

# Kiểm tra số lượng có khớp không
if len(problem_files) != len(solution_files):
    print(f" Cảnh báo: số lượng problem ({len(problem_files)}) và solution ({len(solution_files)}) không khớp!")

# Đổi tên file theo thứ tự
for i, ((p_name, _), (s_name, _)) in enumerate(zip(problem_files, solution_files), start=1):
    new_problem = f"Problem{i}.md"
    new_solution = f"Solution{i}.py"

    old_p = os.path.join(PROBLEMS_DIR, p_name)
    old_s = os.path.join(SOLUTIONS_DIR, s_name)
    new_p = os.path.join(PROBLEMS_DIR, new_problem)
    new_s = os.path.join(SOLUTIONS_DIR, new_solution)

    os.rename(old_p, new_p)
    os.rename(old_s, new_s)
    print(f" {p_name} → {new_problem} | {s_name} → {new_solution}")

