import pandas as pd
from Exercise_Visualizer import cell_to_list, sum_row

# Test harness

# Testing cell_to_list function
assert cell_to_list("[]") == []
assert cell_to_list("[10101010100]") == [10101010100]
assert cell_to_list("[1,2,3,4]") == [1,2,3,4]
assert cell_to_list("[1,2,3,4,5,6,7,8]") == [1,2,3,4,5,6,7,8]
assert cell_to_list("[10,2,38,900,1000000]") == [10,2,38,900,1000000]


# Testing sum_row function
df = pd.read_excel(r'C:\Users\leewa\Documents\Important documents\Computer Science\Python Projects\Exercise_Tracking_and_Visualization\Exercise tracking (testing version).xlsx')
df.drop(df.columns[df.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)
assert sum_row(df.iloc[0]) == 8
assert sum_row(df.iloc[1]) == 19