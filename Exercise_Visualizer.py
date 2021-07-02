# This program visualizes several exercise statistics

import pandas as pd

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

# Create graph of times exercised vs. the month
def frequency_vs_months_chart():
    pass

# Create bar chart of times exercised in each day of the week
def frequency_vs_day_chart():
    pass

# Create bar chart of how many times I've done each type of exercise
def frequency_vs_exercise_type():
    
    pass

def main():
    frequency_vs_months_chart()
    frequency_vs_day_chart()
    frequency_vs_exercise_type()

if __name__ == '__main__':
    main()

