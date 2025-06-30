import pymupdf
import os
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

def get_file_info(file_path):
    doc = pymupdf.open(file_path)
    file_info = {
        'file_name': os.path.basename(file_path),
        'file_size': os.path.getsize(file_path),
        'page_count': doc.page_count,
        'metadata': doc.metadata,
        'first_page_orientation': 'Portrait' if doc.load_page(0).rect.width < doc.load_page(0).rect.height else 'Landscape',
    }
    
    doc.close()
    return file_info 

def add_text_to_pdf(input_pdf, output_pdf, page_num=0, text="TESTING!!", x=50, y=400, font_size=40, FONT_PATH=FONT_PATH):
    doc = pymupdf.open(input_pdf)
    page = doc[page_num]
    page.insert_text((x, y), text, fontsize=font_size, color=(0, 0, 0)) 
    doc.save(output_pdf)
    doc.close()
    return True
