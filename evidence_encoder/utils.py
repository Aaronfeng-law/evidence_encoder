import pymupdf
import os
import re
from dotenv import load_dotenv
load_dotenv()
FONT_PATH = os.getenv("FONT_PATH")

def check_directory(input_dir='input'):
    if input_dir != 'input':
        print(f"Input directory '{input_dir}' is not allowed. Please use 'input' as the directory name.")
        raise ValueError("Input directory must be named 'input'.")
    os.makedirs(input_dir, exist_ok=True)
    print(f"Input directory '{input_dir}' is created and ready for use.")
        

def check_pdf_files(input_dir='input'):
    """檢查資料夾內是否有 PDF 檔案，且僅允許 PDF。"""
    pdf_files = os.listdir(input_dir)
    if not pdf_files or len(pdf_files) == 0:
        print(f"Input directory '{input_dir}' is empty. Please place your PDF files here.")
        raise ValueError("Input directory is empty. Please place your PDF files here.") 
    for file in pdf_files:
        if not file.endswith('.pdf'):
            print(f"File '{file}' is not a PDF. Please place only PDF files in the input directory.(extension .pdf)")
            raise SystemExit(f"File '{file}' is not a PDF. Please place only PDF files in the input directory.(extension .pdf)")
            
def get_all_file_path(input_dir='input'):
    return [os.path.join(input_dir, file) for file in os.listdir(input_dir) if file.endswith('.pdf')]

def get_file_info(file_path, verbose=False):
    doc = pymupdf.open(file_path)
    file_info = {
        'file_name': os.path.basename(file_path),
        'file_size': os.path.getsize(file_path),
        'page_count': doc.page_count,
        'metadata': doc.metadata,
        'rotation' : doc.load_page(0).rotation,
        'orientation': 'Portrait' if doc.load_page(0).rect.width < doc.load_page(0).rect.height else 'Landscape',
    }
    if verbose:
        print(f"檔案名稱：{file_info['file_name']}")
        print(f"檔案大小：{file_info['file_size']} bytes")
        print(f"頁數：{file_info['page_count']}")
        print(f"第一頁旋轉角度：{file_info['rotation']} degrees")
        print(f"第一頁方向：{file_info['orientation']}")
    doc.close()
    return file_info

def check_rotation(file_path, page_num=0):
    info = get_file_info(file_path)
    orientation, rotation = info["orientation"], info["rotation"]
    if orientation == "Landscape":
        print(f"File '{file_path}' is in Landscape orientation with rotation {rotation} degrees.")
        print("Please rotate the PDF to Portrait orientation before proceeding.")
    

def add_text_to_pdf(input_pdf, output_pdf, page_num=0, text="TESTING!!", x=50, y=400, font_size=40, fontname = None, encoding='utf-8-sig', font_path = FONT_PATH):
    doc = pymupdf.open(input_pdf)
    page = doc[page_num]
    page.insert_font(fontname="TW-MOE-Std-Kai", fontfile=font_path)
    page.insert_text((x, y), text, fontsize=font_size, color=(0, 0, 0), 
                        fontname=fontname, encoding=encoding) 
    doc.save(output_pdf)
    doc.close()
    return True

def add_vertical_text_to_pdf(
    input_pdf, output_pdf, page_num=0, text="直式書寫範例",
    x=570, y=25, font_size=16, fontname="TW-MOE-Std-Kai", font_path=FONT_PATH
):
    doc = pymupdf.open(input_pdf)
    page = doc[page_num]
    if fontname and font_path:
        page.insert_font(fontname=fontname, fontfile=font_path)
    # 將連續數字視為一組
    tokens = re.findall(r'\d+|[^\d]', text)
    y_offset = y
    for token in tokens:
        if token.isdigit():
            page.insert_text(
                (x, y_offset),
                token,
                fontsize=font_size,
                color=(0, 0, 0),
                fontname=fontname,
                rotate=0,
            )
            y_offset += font_size
        else:
            page.insert_text(
                (x, y_offset),
                token,
                fontsize=font_size,
                color=(0, 0, 0),
                fontname=fontname,
            )
            y_offset += font_size
    doc.save(output_pdf)
    doc.close()
    return True

