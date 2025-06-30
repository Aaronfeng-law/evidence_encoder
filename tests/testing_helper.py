from fpdf import FPDF
import os
from dotenv import load_dotenv
load_dotenv()
FONT_PATH = os.getenv("FONT_PATH")

def make_some_dummy_files():
        os.makedirs('input', exist_ok=True)
        with open('input/test1.pdf', 'w') as f:
            f.write("abcd")
        with open('input/test2.pdf', 'w') as f:
            f.write("This is a test file.")
        with open('input/test3.pdf', 'w') as f:
            f.write("This is another test PDF file.")
        with open('input/test4.txt', 'w') as f:
            f.write("This is a test PDF file.")
            

FONT_PATH = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"  # Default font path, change if necessary
def create_fpdf(directory="output_pdfs", filename="my_test_document.pdf", orientation='P', font_path=FONT_PATH):
    if not os.path.exists(FONT_PATH):
        print(f"錯誤: 找不到字體檔案 '{FONT_PATH}'。")
        print("請確認 MoeStandardKai.ttf 字體是否安裝在你的 Ubuntu 系統上，")
        print("或修改 FONT_PATH 為其他確實存在的英文字體路徑。")
        return

    os.makedirs(directory, exist_ok=True)  # 確保目錄存在
    file_path = os.path.join(directory, filename)  # 組合完整路徑

    pdf = FPDF(orientation=orientation, unit='mm', format='A4') # Changed to landscape mode
    pdf.add_page()
    try:
        pdf.add_font("DejaVu", "", FONT_PATH, uni=True) 
    except RuntimeError as e:
        print(f"添加字體時發生錯誤: {e}")
        print("請檢查字體檔案是否損壞或無效。")
        return

    pdf.set_font("DejaVu", size=14)
    english_text = (
        "This is a test PDF document created with fpdf2.\n"
        "It contains only English characters to avoid encoding issues.\n"
        "We are using a font that is definitely available on Ubuntu, like MoeStandardKai Sans.\n"
        "This approach ensures compatibility and avoids the 'latin-1' codec error.\n"
        "Document created on June 29, 2025."
    )
    pdf.multi_cell(0, 10, english_text)

    try:
        pdf.output(file_path)
        print(f"PDF file '{file_path}' has been successfully created.")
    except Exception as e:
        print(f"An error occurred while creating the PDF file: {e}")