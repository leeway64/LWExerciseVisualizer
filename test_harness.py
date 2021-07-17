# Test harness

import pandas as pd
from Exercise_Visualizer import add_to_weekdays_exercised_dict, cell_to_list, find_day_of_week, sum_row, sum_column

df = pd.read_excel('Exercise tracking (testing version).xlsx')
df.drop(df.columns[df.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)


# Testing cell_to_list function
assert cell_to_list("[]") == []
assert cell_to_list("[10101010100]") == [10101010100]
assert cell_to_list("[1,2,3,4]") == [1,2,3,4]
assert cell_to_list("[1,2,3,4,5,6,7,8]") == [1,2,3,4,5,6,7,8]
assert cell_to_list("[10,2,38,900,1000000]") == [10,2,38,900,1000000]


# Testing sum_row function
assert sum_row(df.iloc[0]) == 8
assert sum_row(df.iloc[1]) == 19
assert sum_row(df.iloc[2]) == 4


# Testing sum_column function
assert sum_column(df['Running']) == 23
assert sum_column(df['Strength']) == 12
assert sum_column(df['Testing1']) == 0


# Testing find_day_of_week function
assert find_day_of_week(2021, 7, 5) == 'Monday'
assert find_day_of_week(2021, 7, 4) == 'Sunday'
assert find_day_of_week(2020, 4, 1) == 'Wednesday'
assert find_day_of_week(2019, 6, 7) == 'Friday'


# Testing add_to_weekdays_exercised_dict function
times_exercised_in_day_of_week = {'Sunday': 0,
                                    'Monday': 0,
                                    'Tuesday': 0,
                                    'Wednesday': 0,
                                    'Thursday': 0,
                                    'Friday': 0,
                                    'Saturday': 0}

times_exercised_in_day_of_week = add_to_weekdays_exercised_dict(
                                      times_exercised_in_day_of_week, 2021, 7, list(range(4, 11)))

for key in times_exercised_in_day_of_week.keys():
    assert times_exercised_in_day_of_week[key] == 1
