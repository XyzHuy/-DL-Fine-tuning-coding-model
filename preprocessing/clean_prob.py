import os
import re
from bs4 import BeautifulSoup

# === Cấu hình ===
INPUT_DIR = "../data/problems"          # Thư mục chứa file .md gốc
OUTPUT_DIR = "../data/cleaned_problems" # Thư mục lưu file sạch
os.makedirs(OUTPUT_DIR, exist_ok=True)

def clean_html(text: str) -> str:
    """
    Xóa toàn bộ HTML, giữ lại nội dung text thuần.
    """
    soup = BeautifulSoup(text, "html.parser")
    # Xóa hình ảnh
    for img in soup.find_all("img"):
        img.decompose()
    # Lấy text thuần, thay &nbsp; bằng space
    text = soup.get_text()
    text = text.replace("\xa0", " ")
    return text

def normalize_whitespace(text: str) -> str:
    """
    Chuẩn hóa khoảng trắng, dòng trống.
    """
    text = re.sub(r"[ \t]+", " ", text)            # bỏ thừa space/tab
    text = re.sub(r"\n{3,}", "\n\n", text.strip()) # không quá 2 dòng trống
    return text.strip() + "\n"

def clean_md_content(content: str) -> str:
    # Xóa tiêu đề đầu (dòng bắt đầu bằng '# ')
    content = re.sub(r"^# .*\n+", "", content)

    # Xóa toàn bộ HTML tags và hình ảnh
    content = clean_html(content)

    # Xóa các dấu &lt; &gt; &amp; còn sót
    content = (
        content.replace("&lt;", "<")
        .replace("&gt;", ">")
        .replace("&amp;", "&")
    )

    # Chuẩn hóa khoảng trắng
    content = normalize_whitespace(content)

    return content

def process_all_files():
    for filename in os.listdir(INPUT_DIR):
        if not filename.endswith(".md"):
            continue

        input_path = os.path.join(INPUT_DIR, filename)
        output_path = os.path.join(OUTPUT_DIR, filename)

        with open(input_path, "r", encoding="utf-8") as f:
            raw = f.read()

        cleaned = clean_md_content(raw)

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(cleaned)

        print(f"Cleaned: {filename}")

if __name__ == "__main__":
    process_all_files()
    print("\n✨ Done! All cleaned files are in:", OUTPUT_DIR)
