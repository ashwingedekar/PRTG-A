import pandas as pd

# Path to the CSV file
csv_file_path = "C:/prtg/test.csv"

try:
    # Use pandas to read the CSV data
    df = pd.read_csv(csv_file_path)

    # Convert "Traffic Total (Speed)(RAW)" to numeric type
    df["Traffic Total (Speed)(RAW)"] = pd.to_numeric(df["Traffic Total (Speed)(RAW)"], errors='coerce')

    # Drop rows with NaN values in "Traffic Total (Speed)(RAW)"
    df = df.dropna(subset=["Traffic Total (Speed)(RAW)"])

    # Check if the DataFrame is not empty
    if not df.empty:
        # Find the row with the maximum "Traffic Total (Speed)(RAW)"
        max_raw_speed_row = df.loc[df["Traffic Total (Speed)(RAW)"].idxmax()]

        # Print the result in the terminal
        print("Row with the maximum Traffic Total (Speed)(RAW):")
        print(max_raw_speed_row)
    else:
        print("No non-NaN values found in 'Traffic Total (Speed)(RAW)'.")

except Exception as e:
    print(f"Error processing CSV data: {e}")
