# evidence_encoder

## 專案簡介
evidence_encoder 是一個用於批次處理 PDF 檔案並自動插入證據編號文字的工具，適合法律文件、證據資料等需要標註的場合。使用者可自訂插入的文字、編號與字體大小

## 為什麼要開發這個工具？
證據編號、貼小耳朵，這些工作對於作過律所助理、實習生的人來說應該再熟悉不過了，每次都要本來都是都過手寫與蓋印張，而我是個懶鬼，所以我做了這個。

### 功能
- 透過預先設定的證據標號（原證、被證、附件...)，自動化為pdf上標籤
### 限制
- 限使用於A4直式pdf檔案


## 目錄結構
- `evidence_encoder/`：主要程式碼（包含 PDF 處理與文字插入功能）
- `input/`：放置待處理的 PDF 檔案
- `output/`：輸出已插入證據編號的 PDF 檔案
- `tests/`：單元測試
- `example/`：範例 PDF
- `.env`：環境變數（如字體路徑）

## 安裝需求
- Python 3.10+
- 本工具在ubuntu24.04上開發
- 套件：`pymupdf`, `fpdf`, `python-dotenv`
- 系統需安裝支援中文字體（預設為 MoeStandardKai.ttf）

安裝套件：
```sh
pip install pymupdf fpdf python-dotenv
```

## 使用說明
1. 將待處理的 PDF 檔案放入 `input/`
2. 編輯 `.env` 檔案，設定字體路徑
3. 執行 `main.sh` 進行批次處理
4. 處理完成後，已插入證據編號的 PDF 檔案將儲存在 `output/` 目錄中，輸出檔案格式為：[證據編號]_原檔案名稱.pdf

## 系統需求
- Python 3.10+
- 套件：`pymupdf`, `fpdf`, `python-dotenv`
- 系統需安裝支援中文字體（預設為 MoeStandardKai.ttf），8可以在以下網址下載：https://language.moe.gov.tw/result.aspx?classify_sn=23&subclassify_sn=436&content_sn=47

## 未來
- 自動偵測pdf方向
- 更彈性的標注
