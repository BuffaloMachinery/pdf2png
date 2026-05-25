"""
Build script to create a Windows executable using PyInstaller
Run: python build_exe.py
"""

import PyInstaller.__main__
import os

# Get the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Build the executable
PyInstaller.__main__.run([
    'main.py',
    '--onefile',  # Create a single executable file
    '--windowed',  # No console window
    '--name=PDF2PNG轉換器',  # Application name
    '--icon=icon.ico',  # Icon file (optional, will create one if not present)
    '--add-data=.;.',  # Include current directory
    '--distpath=dist',
    '--buildpath=build',
    '--specpath=.',
    f'--workpath={os.path.join(current_dir, "build")}',
    f'--distpath={os.path.join(current_dir, "dist")}',
])

print("\n✅ 建置完成！可執行檔位於 dist 資料夾中")
