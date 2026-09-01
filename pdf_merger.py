import os
import sys
import time
from PyPDF2 import PdfMerger

def merge_pdfs_in_folder():
    # 1. 設定路徑：取得目前 exe 所在的資料夾路徑
    if getattr(sys, 'frozen', False):
        application_path = os.path.dirname(sys.executable)
    else:
        application_path = os.path.dirname(os.path.abspath(__file__))
    
    # 設定 Output 資料夾路徑
    output_dir = os.path.join(application_path, 'output')
    
    # 2. 檢查並建立 Output 資料夾
    if not os.path.exists(output_dir):
        try:
            os.makedirs(output_dir)
            print(f"已建立 output 資料夾：{output_dir}")
        except Exception as e:
            print(f"建立資料夾失敗：{e}")
            input("按 Enter 鍵退出...")
            return

    # 3. 搜尋所有 .pdf 檔案
    # 過濾掉 output 資料夾內的檔案，避免重複合併
    files = [f for f in os.listdir(application_path) if f.lower().endswith('.pdf')]
    
    # 依照檔名排序（確保合併順序正確，例如 1.pdf, 2.pdf...）
    files.sort()

    if not files:
        print("錯誤：當前資料夾中沒有找到任何 PDF 檔案。")
        input("按 Enter 鍵退出...")
        return

    print(f"找到 {len(files)} 個 PDF 檔案，準備合併...")
    
    # 4. 執行合併
    merger = PdfMerger()
    
    try:
        for filename in files:
            filepath = os.path.join(application_path, filename)
            print(f"正在加入：{filename}")
            merger.append(filepath)
        
        # 設定輸出檔名 (例如：merged_result.pdf)
        output_filename = "merged_result.pdf"
        output_path = os.path.join(output_dir, output_filename)
        
        merger.write(output_path)
        merger.close()
        
        print("-" * 30)
        print(f"成功！檔案已合併至：\n{output_path}")
        print("-" * 30)
        
    except Exception as e:
        print(f"合併過程中發生錯誤：{e}")
    
    # 暫停程式，讓使用者能看到結果，而不是視窗閃一下就消失
    input("按 Enter 鍵結束程式...")

if __name__ == "__main__":
    merge_pdfs_in_folder()