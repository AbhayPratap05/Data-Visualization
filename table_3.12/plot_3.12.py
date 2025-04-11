import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the cleaned CSV files
df_rural = pd.read_csv("./table_3.12/cleaned_table_3.12.0.csv")
df_urban = pd.read_csv("./table_3.12/cleaned_table_3.12.1.csv")

# Set "State" as the index for heatmap plotting
df_rural.set_index("State", inplace=True)
df_urban.set_index("State", inplace=True)

# Set figure size
plt.figure(figsize=(12, 8))

# Create a heatmap for Rural MPCE
sns.heatmap(df_rural, cmap="YlGn", annot=True, fmt=".0f", linewidths=0.5)

# Labels and Title
plt.title("Average Rural MPCE (₹) by Social Group in 2022-23, Major States", fontsize=14)
plt.xlabel("Social Group", fontsize=12)
plt.ylabel("State", fontsize=12)
plt.figtext(0.5, 0.01, "# includes not reporting cases (i.e., those who have not reported social group) also.",  ha="center", fontsize=8, style="italic")

# Show the plot
plt.show()

# Create a separate heatmap for Urban MPCE
plt.figure(figsize=(12, 8))

sns.heatmap(df_urban, cmap="YlGn", annot=True, fmt=".0f", linewidths=0.5)

# Labels and Title
plt.title("Average Urban MPCE (₹) by Social Group in 2022-23, Major States", fontsize=14)
plt.xlabel("Social Group", fontsize=12)
plt.ylabel("State", fontsize=12)
plt.figtext(0.5, 0.01, "# includes not reporting cases (i.e., those who have not reported social group) also.",  ha="center", fontsize=8, style="italic")


# Show the plot
plt.show()