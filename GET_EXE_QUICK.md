# 🚀 快速获取 EXE - 3 种方法

## 方法 1️⃣: 一鍵自動構建（推薦 ⭐⭐⭐）

**最簡單，最可靠的方法！**

### 前置條件
- ✅ Windows 10/11/12
- ✅ Python 3.9+ (從 https://www.python.org/downloads/ 下載)
- ✅ 安裝 Python 時勾選 "Add Python to PATH"

### 3 個簡單步驟

1. **下載本項目**
   ```bash
   git clone https://github.com/BuffaloMachinery/pdf2png.git
   cd pdf2png
   ```
   或直接下載 ZIP 文件並解壓

2. **安裝 Poppler**（重要！）
   
   以**管理員身份**打開 PowerShell，運行：
   ```powershell
   choco install poppler -y
   ```
   
   如果沒有 Chocolatey，先運行：
   ```powershell
   Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
   ```

3. **雙擊執行 `BUILD_EXE.bat`**
   - 自動安裝所有 Python 依賴
   - 自動構建 EXE
   - 完成後 EXE 在 `dist` 文件夾中

### 完成！
```bash
dist/PDF2PNG轉換器.exe
```

---

## 方法 2️⃣: 從 GitHub Release 下載（最簡單 ⭐⭐）

如果 GitHub Actions 成功构建了 EXE：

1. 訪問 Releases 頁面
   - https://github.com/BuffaloMachinery/pdf2png/releases

2. 下載 `PDF2PNG轉換器.exe`

3. 雙擊運行 ✅

**注意**: 如果 Release 中沒有 EXE，請使用方法 1

---

## 方法 3️⃣: 手動構建（進階用戶）

### 步驟

```bash
# 1. 進入項目目錄
cd /path/to/pdf2png

# 2. 安裝 Python 依賴
pip install -r requirements.txt

# 3. 安裝 PyInstaller
pip install pyinstaller

# 4. 構建 EXE
pyinstaller --onefile --windowed --name "PDF2PNG轉換器" main.py

# 5. 找到 EXE
# dist/PDF2PNG轉換器.exe
```

---

## 🆘 常見問題

### Q: 執行 BUILD_EXE.bat 後沒有反應？
**A:** 
- 檢查是否以管理員身份運行
- 確保 Python 已安裝並在 PATH 中
- 在命令提示字元中手動運行 `python --version`

### Q: "找不到 Poppler"？
**A:**
```powershell
# 以管理員身份運行
choco install poppler -y
```
或手動下載：https://github.com/oschwartz10612/poppler-windows/releases/

### Q: 構建失敗？
**A:**
- 確保 Python 版本 3.9+
- 運行 `pip install --upgrade pip`
- 刪除 `build` 和 `dist` 文件夾後重試

### Q: 可以分享 EXE 嗎？
**A:** 當然可以！
- EXE 是獨立的，無需任何依賴項
- 可以在任何 Windows 電腦上運行
- 無需安裝 Python 或 Poppler

---

## 📊 比較表

| 方法 | 難度 | 時間 | 可靠性 | 推薦指數 |
|------|------|------|--------|---------|
| 1. BUILD_EXE.bat | ⭐ 極簡 | 5 分鐘 | 🟢 很高 | ⭐⭐⭐ |
| 2. GitHub Release | ⭐ 極簡 | 1 分鐘 | 🟡 中等 | ⭐⭐ |
| 3. 手動構建 | ⭐⭐⭐ 複雜 | 10 分鐘 | 🟢 很高 | ⭐ |

---

## 🎯 建議流程

1. **首先嘗試方法 1** → `BUILD_EXE.bat`（最可靠）
2. **如果失敗** → 檢查 Python 和 Poppler 是否正確安裝
3. **最後選擇** → 方法 3（手動構建）

---

## 需要幫助？

- 📖 查看 [BUILD_LOCAL_WINDOWS.md](BUILD_LOCAL_WINDOWS.md) 獲取詳細說明
- 📖 查看 [README.md](README.md) 了解使用方法
- 🐛 提交 Issue: https://github.com/BuffaloMachinery/pdf2png/issues

---

**最推薦的方式：直接在 Windows 上使用 `BUILD_EXE.bat` 構建，避免依賴 GitHub Actions！** ✨
