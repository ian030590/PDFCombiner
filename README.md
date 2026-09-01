# PDFCombiner (PDF 批次合併工具)

簡單高效的 Python PDF 批次合併工具，可將同一目錄下的多個 PDF 檔案自動按檔名排序並合併輸出至 `output` 資料夾。

## 核心功能 / Features

- **自動搜尋合併**：自動偵測執行檔或腳本所在目錄內的所有 `.pdf` 檔案。
- **智慧排序**：依照自然檔名排序進行頁面合併，確保文件章節順序正確。
- **自動建立輸出目錄**：處理完成後自動將成果輸出至 `output/merged_output.pdf`，不破壞原始檔案。
- **免安裝 Portable 支援**：支援 PyInstaller 打包為單一 EXE 執行檔，開箱即用。

## 檔案結構 / File Structure

```text
PDFCombiner/
├── pdf_merger.py      # PDF 合併核心原始碼
├── PDFCombiner.spec   # PyInstaller 打包設定檔
└── README.md          # 專案說明文件
```

## 使用方式 / Usage

### 執行 Python 腳本
```bash
pip install PyPDF2
python pdf_merger.py
```

### 使用打包 EXE
將待合併的 PDF 檔案放入與程式相同資料夾，雙擊執行 `PDFCombiner.exe` 即可於 `output` 資料夾取得合併後文件。

## 授權 / License

MIT License
