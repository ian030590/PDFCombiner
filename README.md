# PDFCombiner

以命令列依檔名順序批次合併資料夾中的 PDF

Merge a folder of PDFs in filename order with a CLI.

![PDFCombiner 命令列執行畫面 / PDFCombiner CLI](assets/screenshot.png)

[中文](#中文) · [English](#english)

## 中文

適合將同一個資料夾中的多份 PDF 合成一份檔案。

### 功能

- 掃描 `pdf_merger.py` 或封裝後執行檔所在資料夾的 PDF，不搜尋子資料夾。
- 依一般檔名字串排序，例如 `1.pdf`、`10.pdf`、`2.pdf`。若要依數字順序合併，請先補零，例如 `01.pdf`、`02.pdf`、`10.pdf`。
- 使用 PyPDF2 合併頁面，檔案在本機處理。

### 安裝與執行

需先安裝 Python。下載原始碼後，在專案資料夾開啟終端機，將要合併的 PDF 放在 `pdf_merger.py` 旁，再執行：

```bash
python -m pip install PyPDF2
python pdf_merger.py
```

處理完成後按 Enter 結束程式。

若要在 Windows 自行建立 `PDFCombiner.exe`，於同一個資料夾執行：

```bash
python -m pip install pyinstaller
python -m PyInstaller PDFCombiner.spec
```

建置完成後，將 `dist` 中的 `PDFCombiner.exe` 與要合併的 PDF 放在同一個資料夾後執行。

### 輸出

結果儲存在腳本或執行檔旁的 `output/merged_result.pdf`。再次執行會覆寫同名輸出，來源 PDF 只供讀取。

### 授權

本專案採用 MIT License 授權開源。

## English

For combining several PDFs in one folder into a single file.

### Features

- Scans the folder containing `pdf_merger.py` or the packaged executable for PDFs, without searching subfolders.
- Uses ordinary filename sorting, such as `1.pdf`, `10.pdf`, `2.pdf`. For numeric order, add leading zeros first, such as `01.pdf`, `02.pdf`, `10.pdf`.
- Merges pages with PyPDF2 and processes files locally.

### Install and run

Install Python first. After downloading the source, open a terminal in the project folder, place the PDFs beside `pdf_merger.py`, and run:

```bash
python -m pip install PyPDF2
python pdf_merger.py
```

Press Enter after processing to exit.

To build `PDFCombiner.exe` on Windows, run these commands in the same folder:

```bash
python -m pip install pyinstaller
python -m PyInstaller PDFCombiner.spec
```

After building, place `PDFCombiner.exe` from `dist` in the same folder as the PDFs and run it.

### Output

The result is saved as `output/merged_result.pdf` beside the script or executable. Running it again overwrites that output. The tool only reads the source PDFs.

### License

This project is released under the MIT License.
