import pandas as pd
import matplotlib.pyplot as plt

# Load the cleaned CSV file
df = pd.read_csv("./table_3.1/cleaned_table_3_1.csv")

# Set figure size and style
plt.figure(figsize=(12, 6))

# Extract data for plotting
x_labels = df["Fractile Class"]
rural_values = df["Rural MPCE"]
urban_values = df["Urban MPCE"]

x = range(len(x_labels))
bar_width = 0.4

# Plot bars for Rural and Urban MPCE
plt.bar(x, rural_values, width=bar_width, label="Rural MPCE", color="skyblue", alpha=0.8)
plt.bar([p + bar_width for p in x], urban_values, width=bar_width, label="Urban MPCE", color="salmon", alpha=0.8)

# Labels and Titles
plt.xlabel("Fractile Class of MPCE")
plt.ylabel("Average MPCE (₹)")
plt.title("Comparison of Rural vs. Urban Average MPCE Across Fractile Classes")
plt.xticks([p + bar_width / 2 for p in x], x_labels, rotation=45)
plt.legend()

# Show the plot
plt.grid()
plt.show()