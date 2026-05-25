# Windows 本地構建指南

如果您想在 Windows 上本地構建 EXE 檔案，請按照以下步驟進行：

## 快速方法（推薦）

### 步驟 1: 安裝 Python
1. 訪問 https://www.python.org/downloads/
2. 下載 Python 3.9 或更高版本
3. 運行安裝程式
4. ⚠️ **重要**：勾選 "Add Python to PATH"
5. 完成安裝

### 步驟 2: 安裝 Poppler
打開 PowerShell（以管理員身份），運行：
```powershell
choco install poppler -y
```

如果沒有安裝 Chocolatey，先運行：
```powershell
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
```

### 步驟 3: 一鍵構建
1. 下載項目檔案
2. 進入項目目錄
3. **雙擊執行 `BUILD_EXE.bat`**
4. 等待構建完成

✅ EXE 檔案將在 `dist` 資料夾中生成！

---

## 詳細方法

如果上述方法不起作用，可以手動執行以下命令：

### 步驟 1: 打開命令提示字元或 PowerShell
```bash
cd /path/to/pdf2png
```

### 步驟 2: 安裝依賴項
```bash
pip install -r requirements.txt
```

### 步驟 3: 安裝 PyInstaller
```bash
pip install pyinstaller
```

### 步驟 4: 構建 EXE
```bash
pyinstaller --onefile --windowed --name "PDF2PNG轉換器" main.py
```

### 步驟 5: 查找 EXE
```
dist/
└── PDF2PNG轉換器.exe
```

---

## 故障排除

### 問題 1: "Python 不是內部或外部命令"
**解決方案**：
- 重新安裝 Python 並勾選 "Add Python to PATH"
- 或使用完整路徑：`C:\Python39\python.exe`

### 問題 2: "找不到 pdftoppm"
**解決方案**：
```powershell
choco install poppler -y
```

### 問題 3: "找不到 PyInstaller"
**解決方案**：
```bash
pip install pyinstaller
```

### 問題 4: 構建失敗，出現編碼錯誤
**解決方案**：
- 確保命令提示字元編碼為 UTF-8
- 或避免在路徑中使用中文字符

---

## 構建選項

如果需要自定義構建，可以修改命令：

```bash
# 添加圖標
pyinstaller --onefile --windowed --icon=icon.ico --name "PDF2PNG轉換器" main.py

# 設置版本信息
pyinstaller --onefile --windowed --version-file=version.txt --name "PDF2PNG轉換器" main.py

# 控制台模式（用於調試）
pyinstaller --onefile --console --name "PDF2PNG轉換器" main.py
```

---

## 驗證構建

構建完成後：

1. **測試 EXE**
   ```bash
   dist/PDF2PNG轉換器.exe
   ```

2. **檢查大小**
   - EXE 檔案應約為 50-100 MB

3. **分發 EXE**
   - 只需複製 `dist/PDF2PNG轉換器.exe`
   - 無需複製任何其他檔案或依賴項

---

## 自動化構建（GitHub Actions）

如果您有 GitHub 帳戶，可以利用我們的自動化工作流：

1. Fork 該項目
2. 推送新的 tag：`git tag -a v1.1.0 -m "Release"`
3. GitHub Actions 自動構建並發佈 EXE

查看進度：https://github.com/BuffaloMachinery/pdf2png/actions

---

## 需要幫助？

- 查看 [README.md](README.md) 了解使用說明
- 查看 [SETUP_GUIDE.md](SETUP_GUIDE.md) 了解完整安裝指南
- 提交 Issue：https://github.com/BuffaloMachinery/pdf2png/issues
