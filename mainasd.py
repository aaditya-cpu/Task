import pandas as pd

# Replace 'your_file.csv' with the path to your CSV file
file_path = '/home/vlad/code/pyth/Task/page-visits-20240302.csv'

# Load the CSV file
df = pd.read_csv(file_path)

# Filter rows where the "params" column contains "crmid="
# Replace 'params' with the exact name of your column containing the parameters
filtered_df = df[df['params'].str.contains("crmid=", na=False)]

# Display the filtered rows
print(filtered_df)

# Save the filtered DataFrame to a new CSV file
# Replace 'filtered_file.csv' with your desired file name
filtered_df.to_csv('filtered_file.csv', index=False)
