# 🚀 快速获取 EXE - 推薦本地構建

## ⚠️ 重要通知

由於 GitHub Actions 環境限制，**自動 CI/CD 構建不穩定**。

**最推薦的方法：直接在 Windows 上本地構建！**

這樣可以：
- ✅ 100% 完整功能
- ✅ 完全支持 PDF 轉換
- ✅ 無需依賴 GitHub Actions
- ✅ 更可靠，更快速

---

## 方法 1️⃣: 本地構建 - BUILD_EXE.bat（推薦 ⭐⭐⭐⭐⭐）

**這是最好、最可靠的方法！**

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
   - 自動構建完整功能的 EXE
   - 完成後 EXE 在 `dist` 文件夾中

### 完成！
```bash
dist/PDF2PNG轉換器.exe
```

✅ 完全功能的 PDF 轉換器！

---

## 方法 2️⃣: 手動構建（進階用戶）

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

## 方法 3️⃣: 從 GitHub Release 下載（有限功能）

⚠️ **注意**：GitHub Actions 構建不穩定，Release 中的 EXE 可能不完整。

如果存在，可以在以下位置下載：
https://github.com/BuffaloMachinery/pdf2png/releases

**建議：改用方法 1 或 2**

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
- 確保 Python 版本 3.9+：`python --version`
- 運行：`pip install --upgrade pip`
- 刪除 `build` 和 `dist` 文件夾後重試
- 查看 [BUILD_LOCAL_WINDOWS.md](BUILD_LOCAL_WINDOWS.md) 獲取詳細說明

### Q: 為什麼 GitHub Actions 不穩定？
**A:**
- Windows runner 環境限制
- Poppler 安裝不穩定
- 網路和重試問題
- 本地構建完全避免這些問題

### Q: 可以分享 EXE 嗎？
**A:** 當然可以！
- EXE 是獨立的，無需任何依賴項
- 可以在任何 Windows 電腦上運行
- 無需安裝 Python 或 Poppler

---

## 📊 比較表

| 方法 | 難度 | 時間 | 完整性 | 可靠性 | 推薦度 |
|------|------|------|--------|--------|---------|
| 1. BUILD_EXE.bat | ⭐ 極簡 | 5 分鐘 | ✅ 100% | 🟢 很高 | ⭐⭐⭐⭐⭐ |
| 2. 手動構建 | ⭐⭐ 簡單 | 10 分鐘 | ✅ 100% | 🟢 很高 | ⭐⭐⭐⭐ |
| 3. GitHub Release | ⭐ 極簡 | 1 分鐘 | 🟡 有限 | 🟡 中等 | ⭐⭐ |

---

## 🎯 建議流程

1. **首先使用方法 1** → `BUILD_EXE.bat`（最推薦）
2. **如果失敗** → 檢查 Python 和 Poppler 是否正確安裝
3. **最後選擇** → 方法 2（手動構建）

---

## 📚 更多資源

- 📖 [BUILD_LOCAL_WINDOWS.md](BUILD_LOCAL_WINDOWS.md) - 詳細構建指南
- 📖 [README.md](README.md) - 使用說明
- 📖 [SETUP_GUIDE.md](SETUP_GUIDE.md) - 完整設置指南
- 🐛 Issue 追蹤: https://github.com/BuffaloMachinery/pdf2png/issues

---

## ✨ 最終建議

**不要依賴 GitHub Actions！直接在您的 Windows 電腦上構建。**

這樣可以：
- 獲得完整功能
- 無需等待 CI/CD
- 100% 可靠
- 支持所有 PDF 轉換功能

**立即開始：雙擊 `BUILD_EXE.bat`！** 🚀

