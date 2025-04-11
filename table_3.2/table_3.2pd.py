import pandas as pd

# Load the original CSV file
df = pd.read_csv("./table_3.2/table_3.2.csv", encoding="utf-8")

# Remove extra header rows
df_cleaned_1 = df.iloc[2:].reset_index(drop=True)
df_cleaned_2 = df.iloc[2:].reset_index(drop=True)

# Rename columns
df_cleaned_1.columns = ["Major State", "Rural MPCE", "Urban MPCE", "Rural-Urban Difference (%)"]
df_cleaned_2.columns = ["Major State", "Rural MPCE", "Urban MPCE", "Rural-Urban Difference (%)"]

# Keep only relevant columns
df_cleaned_1 = df_cleaned_1[["Major State", "Rural MPCE", "Urban MPCE"]]
df_cleaned_2 = df_cleaned_2[["Major State", "Rural-Urban Difference (%)"]]

# Convert MPCE values to numbers (remove commas)
df_cleaned_1["Rural MPCE"] = df_cleaned_1["Rural MPCE"].str.replace(",", "").astype(float)
df_cleaned_1["Urban MPCE"] = df_cleaned_1["Urban MPCE"].str.replace(",", "").astype(float)
df_cleaned_2["Rural-Urban Difference (%)"] = df_cleaned_2["Rural-Urban Difference (%)"].astype(float)

# Save the cleaned file
df_cleaned_1.to_csv("./table_3.2/cleaned_table_3_2.0.csv", index=False)
df_cleaned_2.to_csv("./table_3.2/cleaned_table_3_2.1.csv", index=False)

print("✅ Data cleaning completed successfully!")