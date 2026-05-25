"""
PDF to PNG Converter Application
A simple GUI application to convert PDF files to PNG images
"""

import PySimpleGUI as sg
from pdf2image import convert_from_path
import os
from pathlib import Path

# Set the theme
sg.theme('DarkBlue3')

def main():
    """Main application window"""
    
    # Define the window layout
    layout = [
        [sg.Text('PDF 轉 PNG 轉換工具', font=('Helvetica', 16, 'bold'))],
        [sg.Text('')],  # Empty line for spacing
        
        # PDF file selection
        [sg.Text('選擇 PDF 檔案:', font=('Helvetica', 10, 'bold'))],
        [sg.InputText(key='-PDF_PATH-', disabled=True, size=(50, 1)), 
         sg.FileBrowse('瀏覽', file_types=(('PDF Files', '*.pdf'),), key='-PDF_FILE-')],
        
        [sg.Text('')],
        
        # Output folder selection
        [sg.Text('選擇輸出位置:', font=('Helvetica', 10, 'bold'))],
        [sg.InputText(key='-OUTPUT_PATH-', disabled=True, size=(50, 1)), 
         sg.FolderBrowse('瀏覽', key='-OUTPUT_FOLDER-')],
        
        [sg.Text('')],
        
        # DPI setting
        [sg.Text('解析度 (DPI):', font=('Helvetica', 10)),
         sg.Spin([100, 150, 200, 300, 400, 600], initial_value=200, size=(10, 1), key='-DPI-')],
        
        [sg.Text('')],
        
        # Progress text
        [sg.Multiline(size=(60, 10), disabled=True, key='-OUTPUT-', background_color='#1a1a1a')],
        
        [sg.Text('')],
        
        # Buttons
        [sg.Button('轉換', size=(12, 1), button_color=('white', '#0078d4')), 
         sg.Button('清除', size=(12, 1)), 
         sg.Button('結束', size=(12, 1))]
    ]
    
    # Create the window
    window = sg.Window('PDF 轉 PNG 轉換器', layout, finalize=True)
    
    # Bind file browser update
    window['-PDF_PATH-'].update(values='')
    window['-OUTPUT_PATH-'].update(values='')
    
    # Event loop
    while True:
        event, values = window.read()
        
        if event == sg.WINDOW_CLOSED or event == '結束':
            break
        
        elif event == '-PDF_FILE-':
            # Update PDF path when file is selected
            window['-PDF_PATH-'].update(values['-PDF_FILE-'])
        
        elif event == '-OUTPUT_FOLDER-':
            # Update output path when folder is selected
            window['-OUTPUT_PATH-'].update(values['-OUTPUT_FOLDER-'])
        
        elif event == '清除':
            # Clear all inputs
            window['-PDF_PATH-'].update('')
            window['-OUTPUT_PATH-'].update('')
            window['-OUTPUT-'].update('')
            window['-PDF_FILE-'].update('')
            window['-OUTPUT_FOLDER-'].update('')
        
        elif event == '轉換':
            # Convert PDF to PNG
            pdf_path = values['-PDF_PATH-']
            output_folder = values['-OUTPUT_PATH-']
            dpi = int(values['-DPI-'])
            
            # Validation
            output_text = window['-OUTPUT-']
            
            if not pdf_path:
                output_text.update('❌ 請選擇 PDF 檔案\n', append=False)
                continue
            
            if not os.path.exists(pdf_path):
                output_text.update('❌ PDF 檔案不存在\n', append=False)
                continue
            
            if not output_folder:
                output_text.update('❌ 請選擇輸出位置\n', append=False)
                continue
            
            if not os.path.exists(output_folder):
                output_text.update('❌ 輸出位置不存在\n', append=False)
                continue
            
            try:
                output_text.update('⏳ 正在轉換...\n', append=False)
                window.refresh()
                
                # Get the PDF filename without extension
                pdf_filename = Path(pdf_path).stem
                
                # Convert PDF to images
                images = convert_from_path(pdf_path, dpi=dpi)
                
                # Save images as PNG
                output_text.update('⏳ 正在保存 PNG 檔案...\n', append=True)
                window.refresh()
                
                saved_count = 0
                for i, image in enumerate(images, 1):
                    output_filename = f"{pdf_filename}_page_{i:03d}.png"
                    output_filepath = os.path.join(output_folder, output_filename)
                    image.save(output_filepath, 'PNG')
                    output_text.update(f'✓ 已保存: {output_filename}\n', append=True)
                    saved_count += 1
                
                output_text.update(f'\n✅ 轉換完成！共轉換 {saved_count} 頁\n', append=True)
                output_text.update(f'📁 輸出位置: {output_folder}\n', append=True)
                
            except Exception as e:
                output_text.update(f'❌ 錯誤: {str(e)}\n', append=False)
    
    window.close()

if __name__ == '__main__':
    main()
