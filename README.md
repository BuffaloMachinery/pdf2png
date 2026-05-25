# PDF 轉 PNG 轉換工具

一個簡單且易於使用的 Windows 應用程式，可以將 PDF 檔案轉換為 PNG 圖像。

## 功能特點

- 🖱️ **簡單的圖形界面** - 使用 PySimpleGUI 創建的直觀用戶界面
- 📄 **PDF 轉換** - 支援任何 PDF 檔案的轉換
- 🎯 **可調節解析度** - 支援多種 DPI 設定 (100-600)
- 📁 **自定義輸出位置** - 可選擇任何資料夾作為輸出位置
- 💾 **批量轉換** - 自動將 PDF 的每一頁保存為單獨的 PNG 檔案

## 系統要求

- Windows 10/11
- Python 3.7 或更高版本 (如果從源代碼運行)

## 安裝方法

### 方法 1: 使用預建的 EXE 文件 (推薦)

1. 從 `dist` 資料夾下載 `PDF2PNG轉換器.exe`
2. 雙擊運行 EXE 檔案
3. 無需安裝 Python 或依賴項

### 方法 2: 從源代碼運行

#### 前置條件

- 安裝 Python 3.7+
- 安裝 Poppler (用於 PDF 處理)

#### Windows 上安裝 Poppler

1. **使用 Chocolatey (推薦)**
```bash
choco install poppler
```

2. **或手動安裝**
   - 從 https://github.com/oschwartz10612/poppler-windows/releases/ 下載 Poppler
   - 解壓至 `C:\Program Files\poppler`
   - 將 `C:\Program Files\poppler\Library\bin` 添加到 Windows PATH 環境變量

#### 安裝 Python 依賴

```bash
pip install -r requirements.txt
```

#### 運行應用

```bash
python main.py
```

## 從源代碼構建 EXE

如果要創建自己的 EXE 文件：

1. 安裝 PyInstaller
```bash
pip install pyinstaller
```

2. 運行構建腳本
```bash
python build_exe.py
```

3. 可執行檔將在 `dist` 資料夾中生成

## 使用方法

1. 點擊 "瀏覽" 按鈕選擇要轉換的 PDF 檔案
2. 點擊 "瀏覽" 按鈕選擇輸出位置
3. (可選) 調整解析度 (DPI)
4. 點擊 "轉換" 按鈕開始轉換
5. 轉換完成後，PNG 檔案將保存在指定的位置

## 文件結構

```
pdf2png/
├── main.py              # 主應用程式
├── build_exe.py         # EXE 構建腳本
├── requirements.txt     # Python 依賴項
├── README.md           # 本文件
└── dist/               # 構建輸出 (包含 EXE)
```

## 常見問題

### Q: 轉換後的 PNG 質量不好？
**A:** 增加 DPI 值。更高的 DPI 會產生更清晰的圖像，但文件會更大。

### Q: 支援多頁 PDF 嗎？
**A:** 是的，每一頁都會被轉換為單獨的 PNG 檔案，命名為 `filename_page_001.png`、`filename_page_002.png` 等。

### Q: 能否批量轉換多個 PDF？
**A:** 目前版本逐個轉換。可以重複使用應用程式轉換多個檔案。

### Q: 轉換速度如何？
**A:** 速度取決於 PDF 的頁數、解析度和您的電腦性能。通常每頁需要 1-2 秒。

## 許可證

MIT License

## 貢獻

歡迎提交 Issue 和 Pull Request！

## 支援

如遇到問題，請檢查：
1. Poppler 是否正確安裝
2. 所有 Python 依賴項是否已安裝
3. PDF 檔案是否有效且不受密碼保護