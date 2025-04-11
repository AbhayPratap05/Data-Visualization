import pandas as pd

# Load the original CSV file
df = pd.read_csv("./table_3.1/table_3.1.csv", encoding="utf-8")

# Remove extra header rows
df_cleaned = df.iloc[2:].reset_index(drop=True)

# Rename columns
df_cleaned.columns = ["Fractile Class", "Rural Upper Limit", "Rural MPCE", "Urban Upper Limit", "Urban MPCE"]

# Keep only relevant columns
df_cleaned = df_cleaned[["Fractile Class", "Rural MPCE", "Urban MPCE"]]

# Convert MPCE values to numbers (remove commas)
df_cleaned["Rural MPCE"] = df_cleaned["Rural MPCE"].str.replace(",", "").astype(float)
df_cleaned["Urban MPCE"] = df_cleaned["Urban MPCE"].str.replace(",", "").astype(float)

# Save the cleaned file
df_cleaned.to_csv("./table_3.1/cleaned_table_3_1.csv", index=False)

print("✅ Data cleaning completed successfully!")