# evidence_encoder

## 專案簡介
**evidence_encoder** 是一個用於批次處理 PDF 檔案並自動插入證據編號標籤的工具，適合律師、助理、實習生等需大量處理法律文件的使用者。支援自訂標籤、字體大小、插入位置，並可選擇直式或橫式標註。

---

## 主要功能

- **批次處理 PDF**：自動掃描 `input/` 目錄下所有 PDF，批次插入證據標籤。
- **自訂證據標籤**：支援多種常見證據類型（如告證、被證、原證等），也可自訂標籤文字。
- **自訂字體與位置**：可調整字體大小、插入座標（X, Y），直式標註。
- **圖形化介面**：提供簡易 GUI，設定與批次處理。
- **環境變數設定**：可於 `.env` 設定字體路徑，支援 MoeStandardKai.ttf 或其他字體。
- **單元測試**：內建測試腳本，確保功能正確。

---

## 目錄結構

```
evidence_encoder/
    core.py
    gui_main.py
    main.py
    utils.py
    __init__.py
    ...
input/                # 放待處理 PDF
output/               # 處理後 PDF 輸出
example/              # 範例 PDF
tests/                # 單元測試
TW-MOE-Std-Kai.ttf    # 預設中文字體
.env                  # 字體路徑設定
main.sh               # 啟動 GUI 腳本
test.sh               # 執行單元測試
requirements.txt      # 依賴套件
README.md             # 本說明文件
```

---

## 安裝需求

- Python 3.10+
- 必要套件：
  - `pymupdf`
  - `fpdf`
  - `python-dotenv`
  - `PyQt5`
  - 其他詳見 [requirements.txt](requirements.txt)
- 系統需安裝支援中文字體（預設為 [TW-MOE-Std-Kai.ttf](TW-MOE-Std-Kai.ttf)）

### 安裝套件

```sh
pip install -r requirements.txt
```

#### Windows 安裝與相容性說明

- **相依套件安裝**：使用 `pip install PyQt5 pymupdf python-dotenv` 安裝必要套件。
- **字體路徑設定**：確保 `.env` 檔案中 `FONT_PATH` 指向正確的字體檔案路徑（例如 `C:\path\to\TW-MOE-Std-Kai.ttf`）。如果未設定，程式會嘗試尋找位於專案根目錄下的 `TW-MOE-Std-Kai.ttf`。
- **啟動應用程式**：使用 `main.bat` 腳本啟動 GUI 介面，命令為：
  ```bat
  main.bat
  ```
  或直接執行：
  ```bat
  python evidence_encoder/gui_main.py
  ```

---

## 使用說明

### 1. 準備 PDF 與字體

- 將待處理 PDF 檔案放入 `input/` 目錄。(也不一定，但建議放入此目錄，確保所有需要處理的文件都在同一目錄內)
- 確認 `.env` 檔案內 `FONT_PATH` 指向正確的字體檔案（預設為 `TW-MOE-Std-Kai.ttf`）。

### 2. 啟動圖形化介面

根據你的系統，你可能會需要建立虛擬環境(venv)

```sh
bash main.sh
```
或
```sh
python3 evidence_encoder/gui_main.py
```

### 3. 操作流程

1. 點選「選擇 PDF 檔案」加入欲處理檔案。
2. 於右側設定證據類型、編號、自訂文字、字體大小與插入位置。
3. 可針對每個檔案分別儲存設定。
4. 點選「批次處理所有檔案」，處理結果將輸出至 `output/` 目錄。




## 字體說明

- 預設使用 [教育部標準楷書 MoeStandardKai.ttf](https://language.moe.gov.tw/result.aspx?classify_sn=23&subclassify_sn=436&content_sn=47)
- 亦可於 `.env` 設定其他支援中文字體之路徑

---

## 常見問題

- **Q：PDF 沒有正確插入標籤？**
  - 請確認字體路徑正確，且 PDF 為標準格式。
- **Q：出現字體相關錯誤？**
  - 請下載並安裝 MoeStandardKai.ttf，或於 `.env` 設定其他可用字體。
- **Q：GUI 無法啟動？**
  - 請確認已安裝 PyQt5。

---

## 貢獻與授權

- 歡迎 issue、pull request 與建議！

---
