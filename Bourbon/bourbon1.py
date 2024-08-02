## Bourbon Collection Sorted and Formatted

import pandas as pd
from openpyxl import load_workbook
from openpyxl.styles import Font, Alignment, Border, Side
from datetime import datetime

# Define the bourbon collection data

data = {
    'Name': ['Buffalo Trace', 'Woodford Reserve', 'Blanton\'s', 'Evan Williams Green Label', 'Maker\'s Mark', 'Chicken Cock'],
    'Type': ['Bourbon', 'Bourbon', 'Bourbon', 'Bourbon', 'Bourbon', 'Bourbon'],
    'Age (Years)': [8, 7, 10, 4, 6, 10],
    'ABV (%)': [45, 43.2, 46.5, 43, 45, 45],
    'Price ($)': [30, 40, 60, 25, 35, 57],
    'Region': ['Kentucky', 'Kentucky', 'Kentucky', 'Kentucky', 'Kentucky', 'Kentucky'],
    'UPC Code': ['080244009236', '081128001506', '088004002039', '0009674902132', '085246501610', '810020890020'],
    'Volume': ['750ml', '750ml', '750ml', '750ml', '750ml', '750ml'],
    'Quantity': [8, 4, 15, 27, 7, 2,],
    ' Last Updated ': [datetime.now() , datetime.now(), datetime.now() , datetime.now() , datetime.now() , datetime.now()],
    
}

# Create a DataFrame
df = pd.DataFrame(data)

# Sort the DataFrame by 'Name'
df_sorted = df.sort_values(by='Name')

# Define the file path
file_path = r'C:\Users\xxxxx\OneDrive\Desktop\Bourbon_Collection.xlsx'

# Save the sorted DataFrame to an Excel file
with pd.ExcelWriter(file_path, engine='openpyxl') as writer:
    df_sorted.to_excel(writer, sheet_name='Bourbon Collection', index=False)

    # Load the workbook and sheet to apply formatting
    workbook = writer.book
    sheet = workbook['Bourbon Collection']

    # Define cell styles
    bold_font = Font(bold=True)
    center_alignment = Alignment(horizontal='center')
    border = Border(left=Side(border_style='thin'), right=Side(border_style='thin'),
                    top=Side(border_style='thin'), bottom=Side(border_style='thin'))

    # Apply formatting to header
    for cell in sheet[1]:
        cell.font = bold_font
        cell.alignment = center_alignment
        cell.border = border

    # Apply formatting to columns
    for col in sheet.columns:
        max_length = 0
        column = col[0].column_letter  # Get the column name
        for cell in col:
            try:
                if len(str(cell.value)) > max_length:
                    max_length = len(cell.value)
            except:
                pass
        adjusted_width = (max_length + 2)
        sheet.column_dimensions[column].width = adjusted_width

    # Save the workbook
    workbook.save(file_path)

print(f"Bourbon collection sorted by name and saved to {file_path}")
