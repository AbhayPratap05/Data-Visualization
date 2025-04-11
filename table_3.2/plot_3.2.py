import matplotlib.pyplot as plt
import pandas as pd

# Load the cleaned CSV file
df = pd.read_csv("./table_3.2/cleaned_table_3_2.0.csv")

# Set figure size and style
plt.figure(figsize=(14, 6))

# Extract data for plotting
x_labels = df["Major State"]
rural_values = df["Rural MPCE"]
urban_values = df["Urban MPCE"]

x = range(len(x_labels))
bar_width = 0.3

# Plot bars for Rural and Urban MPCE
plt.bar(x, rural_values, width=bar_width, label="Rural MPCE", color="skyblue", alpha=0.8)
plt.bar([p + bar_width for p in x], urban_values, width=bar_width, label="Urban MPCE", color="salmon", alpha=0.8)

# Labels and Titles
plt.xlabel("Major States")
plt.ylabel("Average MPCE (₹)")
plt.title("Comparison of Rural vs. Urban Average MPCE Across Major States")
plt.xticks([p + bar_width / 2 for p in x], x_labels, rotation=45)
plt.legend()

# Show the plot
plt.grid()
plt.show()

# Load the cleaned Table 3.2 CSV
df = pd.read_csv("./table_3.2/cleaned_table_3_2.1.csv")

# Plot Horizontal Bar Chart
plt.figure(figsize=(10, 8))

difference = df["Rural-Urban Difference (%)"]
state = df["Major State"]

plt.barh(state, difference, color = "salmon", height = 0.5)

# Labels and Title
plt.xlabel("Rural-Urban Difference (%)", fontsize=12)
plt.ylabel("State", fontsize=12)
plt.title("Urban-Rural MPCE Difference (%) by State (2022-23)", fontsize=14)

# Show the plot
plt.grid()
plt.show()