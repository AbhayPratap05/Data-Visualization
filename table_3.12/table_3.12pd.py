import pandas as pd
import os

# Load the original CSV file
df = pd.read_csv("./table_3.12/table_3.12.csv", encoding="utf-8")

# Remove extra header rows
df_cleaned = df.iloc[2:].reset_index(drop=True)

# Rename columns properly
df_cleaned.columns = ["State", "Rural ST", "Rural SC", "Rural OBC", "Rural Others", "Rural All (#)",
                      "Urban ST", "Urban SC", "Urban OBC", "Urban Others", "Urban All (#)"]

# Keep only relevant columns (excluding 'All' columns)
df_rural = df_cleaned[["State", "Rural ST", "Rural SC", "Rural OBC", "Rural Others", "Rural All (#)"]]
df_urban = df_cleaned[["State", "Urban ST", "Urban SC", "Urban OBC", "Urban Others", "Urban All (#)"]]

# Convert MPCE values to numeric format (remove commas and convert to float)
df_rural.iloc[:, 1:] = df_rural.iloc[:, 1:].apply(lambda x: x.str.replace(",", "").astype(float))
df_urban.iloc[:, 1:] = df_urban.iloc[:, 1:].apply(lambda x: x.str.replace(",", "").astype(float))

# Save cleaned files
df_rural.to_csv("./table_3.12/cleaned_table_3.12.0.csv", index=False)
df_urban.to_csv("./table_3.12/cleaned_table_3.12.1.csv", index=False)

print("✅ Data cleaning completed successfully!")