import os
import re
import requests
from pathlib import Path

# --- Cấu hình ---
PYTHON_DIR = Path("python")
PROBLEM_DIR = Path("problems")
PROBLEM_DIR.mkdir(exist_ok=True)

# --- B1: Lấy danh sách id từ thư mục python ---
def extract_ids_from_python_dir():
    ids = []
    for file in PYTHON_DIR.glob("*.py"):
        match = re.match(r"(\d+)_", file.name)
        if match:
            qid = int(match.group(1))  # bỏ số 0 đầu
            ids.append(qid)
    return sorted(set(ids))

# --- B2: Tạo ánh xạ id -> slug ---
def fetch_id_slug_map():
    print("Fetching LeetCode problem list...")
    url = "https://leetcode.com/api/problems/all/"
    resp = requests.get(url)
    resp.raise_for_status()
    data = resp.json()

    id_to_slug = {}
    # dùng frontend_question_id (số hiển thị như 1, 2, 2429, ...)
    for item in data["stat_status_pairs"]:
        frontend_id = item["stat"].get("frontend_question_id")
        slug = item["stat"].get("question__title_slug")
        if frontend_id is not None and slug:
            id_to_slug[int(frontend_id)] = slug
    return id_to_slug


# --- B3: Lấy mô tả đề bài qua GraphQL ---
def fetch_problem_description(slug):
    query = """
    query getQuestion($titleSlug: String!) {
      question(titleSlug: $titleSlug) {
        questionId
        title
        content
        difficulty
      }
    }
    """
    url = "https://leetcode.com/graphql"
    headers = {
        "Content-Type": "application/json",
        "Referer": "https://leetcode.com",
        "User-Agent": "Mozilla/5.0",
    }
    resp = requests.post(url, json={"query": query, "variables": {"titleSlug": slug}}, headers=headers)
    data = resp.json()

    q = data.get("data", {}).get("question")
    if not q:
        return None

    return {
        "id": q["questionId"],
        "title": q["title"],
        "difficulty": q["difficulty"],
        "content": q["content"],
    }

# --- B4: Ghi ra file Markdown ---
def save_problem_markdown(q):
    filename = PROBLEM_DIR / f"Problem{q['id']}.md"
    html_content = q["content"]
    # Markdown cơ bản
    md_content = f"""# {q['title']} ({q['difficulty']})

{html_content}
"""
    filename.write_text(md_content, encoding="utf-8")
    print(f"Saved: {filename}")

# --- Main ---
def main():
    ids = extract_ids_from_python_dir()
    print(f"Found {len(ids)} problem IDs from python/: {ids}")

    id_to_slug = fetch_id_slug_map()

    for qid in ids:
        if qid not in id_to_slug:
            print(f"Skipping id={qid} (not found in LeetCode API)")
            continue

        slug = id_to_slug[qid]
        print(f"Fetching problem {qid} ({slug})...")
        qdata = fetch_problem_description(slug)
        if not qdata:
            print(f"Failed to fetch {slug}")
            continue
        save_problem_markdown(qdata)

    print("\nDone! All problems saved in 'problems/' folder.")

if __name__ == "__main__":
    main()
