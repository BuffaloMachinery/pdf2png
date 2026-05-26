@echo off
cls
echo ========================================
echo PDF2PNG Converter - Building EXE (With Poppler)
echo ========================================
echo.

REM 1. Check Python
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python not found!
    pause
    exit /b 1
)

REM 2. Check main.py exists
if not exist "main.py" (
    echo [ERROR] main.py not found in this folder!
    pause
    exit /b 1
)

REM 【新增檢查】檢查 poppler 資料夾是否存在
if not exist "poppler\bin\pdftoppm.exe" (
    echo [ERROR] poppler\bin\pdftoppm.exe not found!
    echo Please make sure you downloaded Poppler and placed it in the "poppler" folder.
    pause
    exit /b 1
)

echo [OK] Environment check passed.
echo.

REM 3. Install Requirements
echo [INFO] Installing requirements...
pip install -r requirements.txt
if errorlevel 1 (
    echo [ERROR] Failed to install requirements.
    pause
    exit /b 1
)

REM 4. Install PyInstaller
echo [INFO] Installing PyInstaller...
pip install pyinstaller
if errorlevel 1 (
    echo [ERROR] Failed to install PyInstaller.
    pause
    exit /b 1
)

echo.
echo [INFO] Starting PyInstaller build...
echo Please wait a moment...
echo.

REM 5. Run PyInstaller (💡 已加入 --add-data 參數包入 poppler 資料夾)
python -m PyInstaller --onefile --windowed --add-data "poppler;poppler" --name "PDF2PNG_Converter" "main.py"

if errorlevel 1 (
    echo [ERROR] PyInstaller build failed!
    pause
    exit /b 1
)

echo.
echo ========================================
echo [SUCCESS] Build completed successfully!
echo ========================================
echo.
echo Your EXE is inside the "dist" folder.
echo.
pause