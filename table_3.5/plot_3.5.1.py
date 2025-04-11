import pandas as pd
import matplotlib.pyplot as plt

def plot_nested_pie(csv_file, title):

    # Load the data from CSV file
    df = pd.read_csv(csv_file)

    # Separate major categories and subcategories
    major = df[df['Category'] == 'Major']
    subcats = df[df['Category'] != 'Major']

    # Data for the pie charts
    inner_sizes, inner_labels = major['Percentage'], major['Item']
    outer_sizes, outer_labels = subcats['Percentage'], subcats['Item']

    # Colors for the pie charts
    inner_colors = ['#ff9999', '#66b3ff']
    outer_colors = ["#2980B9", "#5D6D7E", "#1ABC9C", "#D35400", "#E74C3C", "#2980B9", "#9B59B6", "#16A085", "#F39C12", "#8E44AD", "#34495E",
                    "#F1C40F", "#7F8C8D", "#27AE60", "#8E44AD", "#C0392B", "#D5DBDB", "#F5B041", "#85929E", "#A569BD", "#1F618D", "#F7DC6F"]

    # Create the nested pie chart
    fig, ax = plt.subplots(figsize=(10, 8))

    # Outer pie chart (subcategories)
    wedges_outer, _, _ = ax.pie(outer_sizes, colors=outer_colors, startangle=90, autopct='%1.1f%%', pctdistance=0.85)

    # Inner pie chart (major categories)
    wedges_inner, _, _ = ax.pie(inner_sizes, colors=inner_colors, radius=0.7, startangle=90, autopct='%1.1f%%', pctdistance=0.75)

    # Draw a circle in the center to create the donut effect
    ax.add_artist(plt.Circle((0, 0), 0.4, color='white'))

    # Equal aspect ratio ensures that pie is drawn as a circle
    ax.axis('equal')

    # Add a title
    plt.title(title)

    # Add a legend
    plt.legend(wedges_inner + wedges_outer, inner_labels.tolist() + outer_labels.tolist(),
            title="Items", loc="center left", bbox_to_anchor=(1, 0.5))

    # Adjust layout and display
    plt.tight_layout()
    plt.show()

# Plot the first CSV file
plot_nested_pie('./table_3.5/table_3.5.0.csv', 'Percentage break-up of MPCE by item groups in Rural India in 2022-23: All-India')

# Plot the second CSV file
plot_nested_pie('./table_3.5/table_3.5.1.csv', 'Percentage break-up of MPCE by item groups in Urban India in 2022-23: All-India')