import pandas as pd

# Read the CSV file into a DataFrame
selected_data = pd.read_csv("selected_data.csv")

# Find the row with the maximum "Traffic Total (Speed)"
max_speed_row = selected_data.loc[selected_data["Traffic Total (Speed)"].idxmax()]

# Print the maximum "Traffic Total (Speed)" and its corresponding "Date Time" and "Traffic Total (Speed)(RAW)"
print("Maximum Traffic Total (Speed) Information:")
print("Date Time:", max_speed_row["Date Time"])
print("Traffic Total (Speed):", max_speed_row["Traffic Total (Speed)"])
print("Traffic Total (Speed)(RAW):", max_speed_row["Traffic Total (Speed)(RAW)"])
