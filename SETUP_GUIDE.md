# PDF2PNG 轉換器 - 完整設置指南

## 快速開始 (最簡單的方法)

### 如果您只想使用應用程式

1. **下載並運行 EXE**
   - 獲取 `PDF2PNG轉換器.exe` 文件
   - 雙擊運行即可
   - 無需安裝任何東西！

---

## 從源代碼運行 (開發者/進階用戶)

### 步驟 1: 安裝 Python

1. 下載 Python 3.9+ 從 https://www.python.org/downloads/
2. 運行安裝程式
3. ⚠️ **重要**: 勾選 "Add Python to PATH" 選項
4. 完成安裝

驗證安裝:
```bash
python --version
```

### 步驟 2: 安裝 Poppler

Poppler 是必需的依賴項，用於 PDF 處理。

#### 選項 A: 使用 Chocolatey (推薦 - 最簡單)

1. 以管理員身份打開 PowerShell
2. 安裝 Chocolatey (如果尚未安裝):
```powershell
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
```

3. 安裝 Poppler:
```bash
choco install poppler
```

#### 選項 B: 手動安裝 (如果 Chocolatey 不可用)

1. 下載 Poppler:
   - 訪問: https://github.com/oschwartz10612/poppler-windows/releases/
   - 下載最新版本的 `poppler-xx.xx.x_windows-x86_64.zip`

2. 解壓到 `C:\Program Files\poppler`

3. 添加到 PATH:
   - 按 `Win + X` > "系統"
   - 點擊 "進階系統設定" > "環境變數"
   - 在 "系統變數" 中，找到 "Path" 並點擊編輯
   - 點擊 "新增"
   - 輸入: `C:\Program Files\poppler\Library\bin`
   - 點擊確定並重啟您的終端

驗證 Poppler 安裝:
```bash
pdftoppm --version
```

### 步驟 3: 克隆或下載項目

```bash
cd Desktop
git clone https://github.com/BuffaloMachinery/pdf2png.git
cd pdf2png
```

或從 ZIP 文件提取。

### 步驟 4: 安裝 Python 依賴項

在項目目錄中打開終端，運行:

```bash
pip install -r requirements.txt
```

### 步驟 5: 運行應用程式

```bash
python main.py
```

---

## 構建 EXE 文件 (可選)

如果要創建可獨立運行的 EXE 文件:

### 步驟 1: 安裝 PyInstaller

```bash
pip install pyinstaller
```

### 步驟 2: 構建 EXE

在項目目錄中運行:

```bash
python build_exe.py
```

### 步驟 3: 找到您的 EXE

可執行檔將位於 `dist` 資料夾中:
```
dist/
└── PDF2PNG轉換器.exe
```

現在您可以:
- 在任何 Windows 電腦上運行此 EXE (無需 Python 或 Poppler)
- 與他人共享 EXE 檔案
- 將其放在 "開始" 菜單中以便快速訪問

---

## 故障排除

### 問題 1: "找不到 python" 或 "不是內部或外部命令"

**原因**: Python 不在 PATH 中
**解決方案**: 
- 重新安裝 Python 並勾選 "Add Python to PATH"
- 或在命令中使用完整路徑: `C:\Python39\python.exe main.py`

### 問題 2: "ModuleNotFoundError: No module named 'pdf2image'"

**原因**: 未安裝 Python 依賴項
**解決方案**:
```bash
pip install -r requirements.txt
```

### 問題 3: "pdftoppm: command not found" 或 Poppler 相關錯誤

**原因**: Poppler 未安裝或不在 PATH 中
**解決方案**:
- 重新安裝 Poppler (參見上面的步驟 2)
- 確保路徑正確添加到環境變量中
- 重啟終端以加載新的環境變量

### 問題 4: 轉換後的 PNG 質量低或文件很大

**原因**: DPI 設定不合適
**解決方案**:
- 增加 DPI 以獲得更好的質量 (200-300 是標準)
- 300+ DPI 用於高質量列印
- 100 DPI 適合屏幕查看且文件較小

### 問題 5: EXE 運行時出現黑色窗口

**原因**: 可能是圖形界面初始化延遲
**解決方案**:
- 等待幾秒鐘
- 確保您有有效的 PDF 文件
- 檢查 Poppler 是否正確安裝在 EXE 中

---

## 系統要求總結

| 項目 | 要求 |
|------|------|
| 作業系統 | Windows 10/11 |
| Python 版本 | 3.7+ (如果從源代碼運行) |
| 磁盤空間 | ~100MB (用於 EXE) / ~50MB (用於依賴項) |
| 內存 | 最低 512MB，推薦 2GB+ |

---

## 文件說明

| 文件 | 用途 |
|------|------|
| `main.py` | 主應用程式代碼 |
| `build_exe.py` | 用於構建 EXE 的腳本 |
| `requirements.txt` | Python 依賴項列表 |
| `README.md` | 用戶友好的文檔 |
| `SETUP_GUIDE.md` | 本文件 - 詳細設置說明 |

---

## 需要幫助？

如果遇到問題:
1. 檢查故障排除部分
2. 驗證所有依賴項是否已正確安裝
3. 確保 PDF 文件有效且不受密碼保護
4. 提交 Issue 到項目的 GitHub 頁面

祝您使用愉快！
