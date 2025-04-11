# Household Expenditure Analysis (India 2022-23)

This project analyzes household consumption and expenditure patterns in rural and urban India based on the 2022-23 HCES report. It involves data extraction from the official PDF, data cleaning, and generation of insightful visualizations to support policy research.

## Methods Used

- **pdfplumber**: To extract tables from the official PDF.
- **pandas**: For cleaning and transforming raw tabular data.
- **matplotlib & seaborn**: For visualizing trends and comparisons.

## File Structure

```
1) script.py  - Extracts raw data from PDF into script.csv
2) script.csv - Raw extracted CSV containing all tables
3) Approach towards Data analysis and Data visualization.pdf - Approach, Methods and Visualizations
4) Data Sources.pdf - Data Sources from Report_591_HCES_2022-2023
5) Methods used, Insights derived, and Visualization strategies employed.pdf - Methods, Insights and Strategies
6) Software & Codes.pdf - Software used and Codes
7) Report_591_HCES_2022-23New.pdf - Survey Report
3) folder - table_3.1
   ├── raw.csv          (Extracted raw data)
   ├── panda.py         (Cleans data)
   ├── cleaned.csv      (Cleaned dataset)
   ├── plot.py          (Plots graphs)
4) folder - table_3.2
   ├── raw.csv
   ├── panda.py
   ├── cleaned1.csv     (For first visualization)
   ├── cleaned2.csv     (For second visualization)
   ├── plot.py
5) folder - table_3.5
   ├── cleaned1.csv     (Manually cleaned data)
   ├── cleaned2.csv
   ├── plot.py
6) folder - table_3.12
   ├── raw.csv
   ├── panda.py
   ├── cleaned1.csv
   ├── cleaned2.csv
   ├── plot.py
6) folder - insights    (Includes all the visualizations)
   ├── 3.1_fractile_classes.png
   ├── 3.2.0_states.png
   ├── 3.2.1_states_diff.png
   ├── 3.5.0_items_rural.png
   ├── 3.5.1_items_urban.png
   ├── 3.12.0_social_group_rural.png
   ├── 3.12.1_social_group_urban.png
```
