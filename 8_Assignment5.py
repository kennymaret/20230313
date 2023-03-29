import pandas as pd

# 1. Input
raw_data = pd.read_csv("AssignmentCSV.csv")
print(raw_data)

# 2. Process 
numberofitem =len(raw_data)
sorted_data = raw_data.sort_values ("Menu",ascending=True)

# 3. Output 
print(f"count:{numberofitem}")
print(f'{sorted_data}')
