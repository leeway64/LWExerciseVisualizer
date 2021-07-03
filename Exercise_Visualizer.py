# This program visualizes several exercise statistics

import pandas as pd
import matplotlib.pyplot as plt

# Converts an Excel spreadsheet's cell into a list
# cell is a string
# Returns a list
def cell_to_list(cell):
    if len(cell) == 2 and cell[0] == "[" and cell[-1] == "]":
        return []
    cell_list = str(cell)  # Convert the data in the pandas data frame into a string
    cell_list = cell_list.split(",")

    # First and last characters of a cell will always be "[" and "]"
    cell_list[0] = cell_list[0][1:]
    cell_list[-1] = cell_list[-1][0:-1]
    
    cell_list = [int(element) for element in cell_list]  # Convert each element into an int
    return cell_list


# Finds the sum of the lengths of all the lists in a column
def sum_column(column):
    sum = 0
    for cell in column:
        sum = len(cell_to_list(cell)) + sum
    return sum


# Finds the sum of the lengths of all the lists in a row
def sum_row(row):
    sum = 0
    row = row[2:]  # First 2 rows will always be year and month
    for cell in row:
        sum = len(cell_to_list(cell)) + sum
    return sum


# Create graph of times exercised vs. the month
def frequency_vs_months_chart(DF):
    days_exercised_in_month = {}
    for row in DF.iloc:
        days_exercised = sum_row(row)


# Create bar chart of times exercised in each day of the week
def frequency_vs_day_chart(DF):
    pass


# Create bar chart of how many times I've done each type of exercise
def frequency_vs_exercise_type(DF):
    exercise_list = list(DF.columns)[2:]  # Ignore the year and month columns
    frequency_of_exercise = dict()
    for exercise in exercise_list:
        frequency_of_exercise[exercise] = sum_column(DF[exercise])



# Highlight the days of the year where I exercised
def print_exercise_days(DF):
    pass


def main():
    exercise_data = pd.read_excel(r'C:\Users\leewa\Documents\Important documents\Computer Science\Python Projects\Exercise_Tracking_and_Visualization\Exercise tracking.xlsx')
    exercise_data.drop(exercise_data.columns[exercise_data.columns.str.contains('unnamed', case = False)], axis = 1, inplace = True)
    exercise_data.reset_index(drop = True, inplace=True)
    frequency_vs_months_chart(exercise_data)
    frequency_vs_day_chart(exercise_data)
    frequency_vs_exercise_type(exercise_data)


if __name__ == '__main__':
    main()
