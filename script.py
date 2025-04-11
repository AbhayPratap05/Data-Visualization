import pdfplumber
import pandas as pd

# Path to the HCES 2022-23 PDF file
pdf_path = "Report_591_HCES_2022-23New.pdf"

# Keywords to detect relevant tables
keywords = ["Average MPCE across fractile classes of MPCE",
            "Average MPCE and urban-rural differences in MPCE in 2022-23",
            "Absolute and percentage break-up of MPCE by item groups in 2022-23",
            "Average MPCE (Rs.) by social group in 2022-23",]

# Open the PDF
extracted_tables = []
with pdfplumber.open(pdf_path) as pdf:
    for page in pdf.pages:
        text = page.extract_text()
        if text and any(keyword in text for keyword in keywords):  # Check if page contains relevant data
            table = page.extract_table()
            if table:
                extracted_tables.append(table)

# Convert extracted tables into a structured DataFrame
dataframes = []
for table in extracted_tables:
    df = pd.DataFrame(table)
    dataframes.append(df)

# Merge all extracted tables into a single CSV file
if dataframes:
    final_df = pd.concat(dataframes, ignore_index=True)
    final_df.to_csv("script.csv", index=False)
    print("Extracted relevant data and saved as 'script.csv'!")
else:
    print("No relevant tables found!")