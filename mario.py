import pandas as pd
import csv

# Convert Excel sheets to CSVs
xls = pd.ExcelFile("mario_kart_data.xlsx")
for sheet_name in xls.sheet_names:
    df = pd.read_excel(xls, sheet_name=sheet_name)
    df.to_csv(f"{sheet_name}.csv", index=False)

# Function to calculate column averages
def average_of_columns(file_path):
    column_sums = {}
    column_counts = {}

    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)

        for col in range(len(header)):
            column_sums[col] = 0
            column_counts[col] = 0
        
        for row in csv_reader:
            for col, value in enumerate(row):
                try:
                    numerical_value = float(value)
                    column_sums[col] += numerical_value
                    column_counts[col] += 1
                except ValueError:
                    pass

    column_averages = {}
    for col in column_sums:
        if column_counts[col] > 0:
            column_averages[header[col]] = column_sums[col] / column_counts[col]
        else:
            column_averages[header[col]] = 0

    return column_averages

# Calculate and print averages
file_path = 'character_kart_stats.csv'
column_averages = average_of_columns(file_path)

for col, average in column_averages.items():
    print(f'Average of "{col}": {average}')