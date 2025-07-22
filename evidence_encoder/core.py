from utils import *
import os
from dotenv import load_dotenv
load_dotenv()
FONT_PATH = os.getenv("FONT_PATH")

evidence_options = {
    "1": "告證",
    "2": "被證",
    "3": "原證",
    "4": "上證",
    "5": "聲證",
    "6": "抗證",
    "7": "再證",
    "8": "相證",
    "9": "再上證",   
    "10": "被上證",
    "11": "附圖",
    "12": "附表",
    "13": "附件",
    "14": "附錄",
    "0": "自訂",
}

def process_pdf(
    pdf_file,
    evidence_type,
    evidence_number="1",
    need_number=True,
    custom_text="",
    font_size=16,
    output_dir="output",
    x=570,
    y=25
):
    """
    處理單一 PDF，插入證據標籤。
    """
    get_file_info(pdf_file, verbose=True)
    if evidence_type == '0':
        text = custom_text
    else:
        text = evidence_options[evidence_type]
    text = f"{text}{evidence_number}"
    if need_number:
        text = f"{text}號"
    os.makedirs(output_dir, exist_ok=True)
    output_pdf = os.path.join(output_dir, f"{text}_{os.path.basename(pdf_file)}.pdf")
    add_vertical_text_to_pdf(
        input_pdf=pdf_file,
        output_pdf=output_pdf,
        text=text,
        font_size=int(font_size),
        x=x,
        y=y
    )
    return output_pdf

def batch_process_pdfs(
    pdf_files,
    evidence_type,
    evidence_number="1",
    need_number=True,
    custom_text="",
    font_size=16,
    output_dir="output",
    x=570,
    y=25
):
    """
    批次處理多個 PDF。
    """
    results = []
    for pdf_file in pdf_files:
        output_pdf = process_pdf(
            pdf_file,
            evidence_type,
            evidence_number,
            need_number,
            custom_text,
            font_size,
            output_dir,
            x,
            y
        )
        results.append(output_pdf)
    return results

def main():
    print("Active Evidence Encoder")
    check_directory('input')
    print("Checking for PDF files in the 'input' directory...")
    check_pdf_files('input')
    print("PDF files check complete. All the files are valid.")
    
    

    pdf_files = get_all_file_path('input')
    
    
    for pdf_file in pdf_files:
        print(f"\n處理檔案：{pdf_file}")
        
        get_file_info(pdf_file,verbose=True)
        
        print("請選擇要插入的文字：")
        for k, v in evidence_options.items():
            print(f"{k}. {v}")
        while True:
            choice = input("請輸入選項編號：")
            if choice in evidence_options:
                break
            else:
                print(f"請輸入 {', '.join(evidence_options.keys())}")
        if choice == '0':
            text = input("請輸入自訂文字：")
        else:
            text = evidence_options[choice]
        
        while True:
            evidence_number = input("請輸入編號（預設：1）：") or "1"
            if evidence_number.isdigit() and int(evidence_number) > 0:
                text = f"{text}{evidence_number}"
                break
            else:
                print("請輸入正整數編號！")
        
        
        while True:
            need_Number = input("是否需要在編號加上「號」？(y/n，預設：y)：") or "y"
            if need_Number.lower() == 'y':
                text = f"{text}號"
                break
            elif need_Number.lower() == 'n':
                break
            else:
                print("請輸入 'y' 或 'n'！")
        
        while True:
            font_size = input("請輸入字體大小（預設：16）：") or "16"
            if font_size.isdigit() and int(font_size) > 0:
                font_size = int(font_size)
                break
            else:
                print("請輸入正整數字體大小！")
        

        os.makedirs("output", exist_ok=True)
        add_vertical_text_to_pdf(
            input_pdf=pdf_file,
            #with text as file name head
            output_pdf=os.path.join("output", f"{text}_{os.path.basename(pdf_file)}.pdf"),
            text=text,
            font_size=int(font_size),
        )
        print(f"{pdf_file} 已處理完成，輸出至 output 資料夾。")

    print("所有 PDF 批次處理完成！")
if __name__ == "__main__":
    main()