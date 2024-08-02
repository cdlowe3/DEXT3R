## Bourbon Collection Sorted


import pandas as pd

# Create a dictionary with sample bourbon data
bourbon_data = {
    'Name': ['Blantons', 'Buffalo Trace', 'Evan Williams Black Label', 'Woodford Reserve', 'Makers Mark', 'Chicken Cock'],
    'Distillery': ['Sazerac CO INC', 'Sazerac CO INC', 'HEAVEN HILL SALES CO', 'BROWN FORMAN CORP', 'JIM BEAM BRANDS CO', 'PARK STREET IMPORTS LLC'],
    'ABV (%)': [46.5, 45.0, 43.0, 43.2, 45.0, 47.0],
    'Price ($)': [65.00, 35.00, 20.00, 50.00, 30.00, 60.00],
        
}

# Convert the dictionary into a DataFrame
df = pd.DataFrame(bourbon_data)

# Sort the DataFrame alphabetically by the 'Name' column
df_sorted = df.sort_values(by='Name')

# Define the file path
file_path = r'C:\Users\c2low\OneDrive\Desktop\Bourbon_Collection.xlsx'

# Save the DataFrame to an Excel file
df_sorted.to_excel(file_path, index=False, engine='openpyxl')

print(f"Bourbon Collection saved to {file_path}")
