# import pandas as pd

# url = "https://mkwrs.com/mk8dx/"
# tables = pd.read_html(url)

# df = tables[0]  # assumes the first table is the correct one

# df.to_csv("mk8dx_world_records.csv", index=False)

# print("Done! Saved as mk8dx_world_records.csv")
# import pandas as pd

# url = "https://www.mariowiki.com/Mario_Kart_8_Deluxe_in-game_statistics"
# tables = pd.read_html(url)

# # Save all tables
# for i, table in enumerate(tables):
#     filename = f"mk8dx_driver_stats_table_{i}.csv"
#     table.to_csv(filename, index=False)
#     print(f"Saved Table {i} as {filename}")

import pandas as pd

# Load the CSV file
df = pd.read_csv('mario_kart_stats.csv')

# Display the first few rows
print(df.head())

# Example: Analyze average speed by character
average_speed = df.groupby('Character')['Speed'].mean()
print(average_speed)
