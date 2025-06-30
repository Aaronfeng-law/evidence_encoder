from utils import *
import argparse
import os
from dotenv import load_dotenv
load_dotenv()
FONT_PATH = os.getenv("FONT_PATH")

def main():
    print("Active Evidence Encoder")
    check_directory('input')
    print("Checking for PDF files in the 'input' directory...")
    check_pdf_files('input')
    print("PDF files check complete. All the files are valid.")
    
    evidence_options = {
    "1": "告證",
    "2": "被證",
    "3": "原證",
    "4": "上證",
    "5": "被上證",
    '6': "附圖",
    '7': "附表",
    '8': "附件",
    '9': "附錄",
    '0': "自訂",
}

    pdf_files = get_all_file_path('input')
    for pdf_file in pdf_files:
        print(f"\n處理檔案：{pdf_file}")
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
print("已完成插入直式文字！")
if __name__ == "__main__":
    main()