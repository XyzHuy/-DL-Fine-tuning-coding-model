import google.generativeai as genai
import os
import json
import time 

# --- 1. Cấu hình API Key ---
api_key = None
try:
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("Chưa đặt biến môi trường GEMINI_API_KEY")
    print(f"--- Đã tải API Key (4 ký tự đầu): {api_key[:4]}... ---")
    genai.configure(api_key=api_key)
except ValueError as e:
    print(f"Lỗi: {e}")
    print("Vui lòng đặt API key của bạn vào biến môi trường.")
    exit()
except Exception as e:
    print(f"Đã xảy ra lỗi không xác định khi cấu hình: {e}")
    exit()

# --- 2. Đọc bài toán từ file ---
def create_problem_description(problem_filepath):
    problem_description = ""
    print(f"--- Đang đọc file: {problem_filepath} ---")
    try:
        with open(problem_filepath, 'r', encoding='utf-8') as f:
            problem_description = f.read()
        if not problem_description:
            print(f"CẢNH BÁO: File {problem_filepath} bị rỗng.")
            return None
        print(f"--- Đọc thành công file: {problem_filepath} ---")
        return problem_description
    except FileNotFoundError:
        print(f"LỖI: Không tìm thấy file '{problem_filepath}'.")
        return None
    except Exception as e:
        print(f"LỖI khi đọc file {problem_filepath}: {e}")
        return None

# --- 3. Tạo Prompt (Câu lệnh) ---
def create_prompt_template(problem_description):
    num_easy = 30
    num_medium = 10
    num_hard = 10
    total_cases = num_easy + num_medium + num_hard

    prompt_template = f"""
    Bạn là một QA Engineer chuyên nghiệp chuyên tạo test case cho lập trình thi đấu.

    Dựa trên mô tả bài toán dưới đây, hãy tạo chính xác {total_cases} test case.
    Phân loại: {num_easy} cơ bản (easy), {num_medium} trung bình (medium), và {num_hard} đặc biệt (hard/edge cases).

    YÊU CẦU ĐỊNH DẠNG ĐẦU RA:
    1.  Đầu ra phải là một ĐỐI TƯỢNG JSON (single JSON object) duy nhất.
    2.  Đối tượng JSON này phải có 2 key chính ở cấp cao nhất: `function_name` và `test_cases`.
    3.  Giá trị của `function_name`: (string) Tên hàm hoặc tên bài toán được suy ra từ mô tả (ví dụ: "sum_of_two_largest", "find_max_element").
    4.  Giá trị của `test_cases`: (array) Một mảng chứa chính xác {total_cases} test case object.
    5.  Mỗi object trong mảng `test_cases` phải có 2 key: `parameters` và `expected_output`.
    6.  Giá trị của `parameters`: (object) Một object chứa các tham số đầu vào. Tên key của tham số PHẢI khớp với tên biến trong mô tả bài toán (ví dụ: {{"nums": [1, 2, 3]}}, hoặc {{"s": "hello", "k": 2}}).
    7.  Giá trị của `expected_output`: (any) Kết quả đầu ra mong đợi cho test case đó.
    8.  **QUAN TRỌNG:** Chỉ trả về đối tượng JSON, không thêm bất kỳ văn bản nào trước hoặc sau nó, không dùng markdown (```json ... ```).

    Mô tả bài toán:
    {problem_description}
    """
    return prompt_template

# --- 4. Gọi API ---
def gen_test_case(prompt_template, problem_num, output_folder):
    print(f"\nĐang tạo test cases cho Problem {problem_num}, vui lòng chờ...")
    try:
        model = genai.GenerativeModel('gemini-pro-latest') 
        response = model.generate_content(prompt_template)
        raw_response_text = response.text
        
        print("\n--- KẾT QUẢ THÔ TỪ API ---")
        print(raw_response_text)
        
        try:
            # Clean text
            cleaned_text = raw_response_text.replace("```json", "").replace("```", "")
            cleaned_text = cleaned_text.strip()

            test_cases = json.loads(cleaned_text)
            
            output_filename = f"TestCases{problem_num}.json"
            output_filepath = os.path.join(output_folder, output_filename)

            with open(output_filepath, 'w', encoding='utf-8') as f:
                json.dump(test_cases, f, ensure_ascii=False, indent=2)
            
            print(f"\n--- ĐÃ GHI THÀNH CÔNG {len(test_cases["test_cases"])} TEST CASES VÀO FILE: {output_filepath} ---")
            return True # Trả về True nếu thành công

        except json.JSONDecodeError:
            print("\n[Lỗi PARSE]: Không thể parse kết quả JSON. Kết quả thô đã được in ở trên.")
        except IOError as e:
            print(f"\n[Lỗi GHI FILE]: Không thể ghi vào file {output_filepath}. Lỗi: {e}")
        except Exception as e:
            print(f"\n[Lỗi không xác định]: {e}")

    except Exception as e:
        print(f"\n--- LỖI API ---")
        print(f"Đã xảy ra lỗi khi gọi API: {e}")
    
    return False


# --- 5. HÀM MAIN ĐIỀU KHIỂN ---
if __name__ == "__main__":
    
    # --- Cấu hình ---
    PROBLEMS_FOLDER = "./data/problems"     # Thư mục chứa file .md
    TESTCASES_FOLDER = "./data/testcases"   # Thư mục chứa file .json (output)
    API_DELAY_SECONDS = 50           # 50 giây (an toàn cho 2 req/phút)

    # 1. Tạo thư mục output nếu chưa tồn tại
    os.makedirs(TESTCASES_FOLDER, exist_ok=True)

    # 2. Lấy danh sách file .md từ thư mục problems
    try:
        problem_files = [f for f in os.listdir(PROBLEMS_FOLDER) if f.endswith('.md')]
        if not problem_files:
            print(f"Không tìm thấy file .md nào trong thư mục '{PROBLEMS_FOLDER}'")
            exit()
            
        print(f"Tìm thấy {len(problem_files)} file problems: {problem_files}")

    except FileNotFoundError:
        print(f"LỖI: Thư mục '{PROBLEMS_FOLDER}' không tồn tại.")
        exit()

    # 3. Lặp qua từng file, xử lý và chờ
    total_files = len(problem_files)
    for i, filename in enumerate(problem_files):
        print(f"\n=================================================")
        print(f"BẮT ĐẦU XỬ LÝ FILE {i+1}/{total_files}: {filename}")
        print(f"=================================================")
        
        # Giả định tên file là "ProblemX.md" (ví dụ: "Problem1.md", "Problem10.md")
        # Chúng ta tách số "X" ra
        problem_num = filename.replace("Problem", "").replace(".md", "")
        if not problem_num.isdigit():
             # Fallback nếu tên file không chuẩn, dùng tên file (không đuôi)
             problem_num = filename.replace(".md", "")
        
        # Đường dẫn đầy đủ đến file input
        input_filepath = os.path.join(PROBLEMS_FOLDER, filename)
        
        # Bước 2: Đọc file
        description = create_problem_description(input_filepath)
        
        if description:
            # Bước 3: Tạo prompt
            prompt = create_prompt_template(description)
            
            # Bước 4: Gọi API và ghi file
            success = gen_test_case(prompt, problem_num, TESTCASES_FOLDER)
            
            if success:
                print(f"--- Xử lý thành công {filename} ---")
            else:
                print(f"--- Xử lý thất bại {filename} ---")
        
        # Bước 5: Chờ API (luôn chờ dù thành công hay thất bại)
        # Chỉ chờ nếu đây không phải là file cuối cùng
        if i < total_files - 1:
            print(f"\nĐANG CHỜ {API_DELAY_SECONDS} giây để API nghỉ ngơi...")
            time.sleep(API_DELAY_SECONDS)
        
    print("\n=================================================")
    print("HOÀN THÀNH: Đã xử lý tất cả các file problems.")
    print("=================================================")