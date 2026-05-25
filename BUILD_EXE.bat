@echo off
REM PDF2PNG 轉換器 - 構建 EXE 批處理腳本
REM 適用於 Windows 用戶在本地構建可執行檔

echo ========================================
echo PDF2PNG 轉換器 - 構建 EXE
echo ========================================
echo.

REM 檢查 Python
python --version >nul 2>&1
if errorlevel 1 (
    echo [❌ 錯誤] Python 未找到
    echo 請從 https://www.python.org/downloads/ 安裝 Python 3.9+
    pause
    exit /b 1
)

REM 檢查 Poppler
pdftoppm --version >nul 2>&1
if errorlevel 1 (
    echo [⚠️  警告] Poppler 未找到，某些依賴項可能無法正常工作
    echo 可以通過 Chocolatey 安裝：choco install poppler
    echo.
)

echo [✓] 環境檢查完成
echo.

echo [進行中] 安裝 Python 依賴項...
pip install -r requirements.txt
if errorlevel 1 (
    echo [❌ 錯誤] 安裝依賴項失敗
    pause
    exit /b 1
)

echo [✓] 依賴項安裝完成
echo.

echo [進行中] 安裝 PyInstaller...
pip install pyinstaller
if errorlevel 1 (
    echo [❌ 錯誤] 安裝 PyInstaller 失敗
    pause
    exit /b 1
)

echo [✓] PyInstaller 安裝完成
echo.

echo [進行中] 構建 EXE 檔案...
echo 這可能需要幾分鐘...
echo.

pyinstaller --onefile --windowed --name "PDF2PNG轉換器" main.py

if errorlevel 1 (
    echo [❌ 構建失敗
    pause
    exit /b 1
)

echo.
echo ========================================
echo [✅] 建置成功！
echo ========================================
echo.
echo EXE 檔案位置：
echo   dist\PDF2PNG轉換器.exe
echo.
echo 您現在可以：
echo 1. 雙擊運行 PDF2PNG轉換器.exe
echo 2. 將其複製到任何位置使用
echo 3. 與他人分享
echo.
pause
