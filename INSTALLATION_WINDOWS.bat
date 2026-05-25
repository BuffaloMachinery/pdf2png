@echo off
REM PDF2PNG 轉換器 - Windows 一鍵安裝腳本

echo ========================================
echo PDF2PNG 轉換器 - 自動安裝
echo ========================================
echo.

REM 檢查 Python 是否已安裝
python --version >nul 2>&1
if errorlevel 1 (
    echo [錯誤] Python 未找到！
    echo 請訪問 https://www.python.org/downloads/ 安裝 Python 3.9+
    echo 安裝時請勾選 "Add Python to PATH"
    pause
    exit /b 1
)

echo [✓] Python 已安裝

REM 檢查 Poppler
pdftoppm --version >nul 2>&1
if errorlevel 1 (
    echo.
    echo [警告] Poppler 未找到
    echo.
    echo 要安裝 Poppler，請選擇下列方法之一：
    echo.
    echo 方法 1 (推薦): 使用 Chocolatey
    echo   以管理員身份打開 PowerShell 並運行：
    echo   choco install poppler
    echo.
    echo 方法 2: 手動安裝
    echo   下載: https://github.com/oschwartz10612/poppler-windows/releases/
    echo   解壓到: C:\Program Files\poppler
    echo   添加到 PATH: C:\Program Files\poppler\Library\bin
    echo.
    pause
) else (
    echo [✓] Poppler 已安裝
)

echo.
echo [進行中] 安裝 Python 依賴項...
pip install -r requirements.txt

if errorlevel 1 (
    echo [錯誤] 安裝依賴項失敗
    pause
    exit /b 1
)

echo.
echo ========================================
echo [✓] 安裝完成！
echo ========================================
echo.
echo 現在可以運行應用程式：
echo   python main.py
echo.
echo 或構建 EXE 文件：
echo   python build_exe.py
echo.
pause
