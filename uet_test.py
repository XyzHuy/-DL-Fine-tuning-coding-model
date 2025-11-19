import os
import subprocess
import sys
import json
from pathlib import Path

# ================= CONFIG =================
PROBLEMS_DIR = Path("problems-test-50")
TESTCASES_DIR = Path("testcases")
SOLUTIONS_DIR = Path("solution_generated")
SOLUTIONS_DIR.mkdir(exist_ok=True)

UET_CODER_SCRIPT = "uet_coder.py" # nhập đường dẫn uet_coder
UET_MARKER_SCRIPT = "uet_marker.py"
TIMEOUT = 180  # giây (180 cho reasoning, 120 cho no reasoning)


def run_coder(problem_file: Path, solution_file: Path) -> bool:
    """
    Chạy uet_coder.py để sinh solution
    Trả về True nếu chạy xong trong TIMEOUT giây, False nếu timeout hoặc lỗi
    """
    try:
        subprocess.run(
            [sys.executable, UET_CODER_SCRIPT, "--problem", str(problem_file), "--output", str(solution_file)],
            timeout=TIMEOUT,
            check=True
        )
        return True
    except subprocess.TimeoutExpired:
        print(f"[TIMEOUT] Model did not produce code for {problem_file} within {TIMEOUT}s")
        # tạo file solution rỗng để thống kê
        with open(solution_file, "w") as f:
            f.write("# TIMEOUT: No solution generated\n")
        return False
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] uet_coder.py failed for {problem_file}: {e}")
        with open(solution_file, "w") as f:
            f.write("# ERROR: Failed to generate solution\n")
        return False


def run_marker(solution_file: Path, test_case_file: Path) -> float | None:
    """
    Chạy uet_marker.py và trả về score (%) từ stdout.
    Nếu timeout xảy ra (10s) thì trả về None
    """
    if not test_case_file.exists():
        print(f"[WARNING] Test case file not found: {test_case_file}")
        return 0.0

    try:
        result = subprocess.run(
            [sys.executable, UET_MARKER_SCRIPT, "--source_code_file", str(solution_file), "--test_cases", str(test_case_file)],
            capture_output=True,
            text=True,
            check=True,
            timeout=15  # set timeout 10 giây
        )
        # Tìm dòng Score: XX% trong stdout
        for line in result.stdout.splitlines():
            if line.startswith("Score:"):
                score_str = line.split(":")[1].strip().replace("%", "")
                return float(score_str)
        return 0.0
    except subprocess.TimeoutExpired:
        print(f"[TIMEOUT] uet_marker.py timed out for {solution_file}")
        return None
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] uet_marker.py failed for {solution_file}: {e}")
        return 0.0


def main():
    total_problems = 0
    total_score = 0.0
    timeout_count = 0

    # Duyệt tất cả problem trong problems-test
    for problem_file in sorted(PROBLEMS_DIR.glob("*.md")):
        total_problems += 1
        problem_name = problem_file.stem
        solution_file = SOLUTIONS_DIR / f"{problem_name}.py"
        test_case_file = TESTCASES_DIR / f"TestCase{problem_name.replace('Problem','')}.json"

        print(f"=== Evaluating {problem_name} ===")

        # 1. Sinh code bằng uet_coder
        success = run_coder(problem_file, solution_file)
        if not success:
            print(f"[TIMEOUT/ERROR] {problem_name} assigned score = 0")
            timeout_count += 1
            total_score += 0.0
            continue

        # 2. Chấm điểm solution bằng uet_marker
        score = run_marker(solution_file, test_case_file)
        if score is None:   # marker bị timeout
            print(f"Score for {problem_name}: TIMEOUT (count as 0%)\n")
            timeout_count += 1
            score = 0.0
        else:
            print(f"Score for {problem_name}: {score}%\n")

        total_score += score

    # Tổng kết
    avg_score = total_score / total_problems if total_problems > 0 else 0.0
    print("====================================")
    print(f"Total problems evaluated: {total_problems}")
    print(f"Problems timeout/error: {timeout_count}")
    print(f"Average score across all problems: {avg_score:.2f}%")
    print("====================================")


if __name__ == "__main__":
    main()
