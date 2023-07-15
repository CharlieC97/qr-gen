
# pip install openpyxl qrcode

import openpyxl
import qrcode
import tkinter as tk
from tkinter import filedialog

def generate_qr_codes_from_excel():
    #Create Tkinter root window
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    
    # Prompt the user to select an Excel file
    file_path = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx")])
    
    if not file_path:
        print("No file selected.")
        return
    
    # Load the Excel workbook
    workbook = openpyxl.load_workbook(file_path)
    
    # Prompt the user to select a worksheet
    sheet_names = workbook.sheetnames
    print("Available Sheets:")
    for i, sheet_name in enumerate(sheet_names):
        print(f"{i+1}. {sheet_name}")
    
    sheet_index = 1
    try:
        sheet_index = int(sheet_index) - 1
        if sheet_index < 0 or sheet_index >= len(sheet_names):
            raise ValueError
    except ValueError:
        print("Invalid sheet index.")
        return
    
    # Select the worksheet
    worksheet = workbook[sheet_names[sheet_index]]
    
    # Prompt the user to select the URL and name columns
    url_column = "A"
    name_column = "B"
    
    # Get the columns of URLs and names
    urls = worksheet[url_column]
    names = worksheet[name_column]
    
    # Generate QR codes for each URL
    for url_cell, name_cell in zip(urls[1:], names[1:]):
        url = url_cell.value
        name = name_cell.value
        
        # Generate the QR code
        qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=4)
        qr.add_data(url)
        qr.make(fit=True)
        
        # Create an image from the QR code
        qr_image = qr.make_image(fill_color="black", back_color="white")
        
        # Save the QR code image with the name from the name column
        qr_image.save(f"{name}.png")


# Example usage
generate_qr_codes_from_excel()
