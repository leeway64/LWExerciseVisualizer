# This program visualizes several exercise statistics

import datetime
import collections
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


# Returns the day of the week, based on the year, month, and day (all ints), as a string
def find_day_of_week(year, month, day):
    return number_to_weekday_dict()[datetime.date(year, month, day).weekday()]


def month_to_number_dict():
    month_to_number = {'January': 1,
    'February': 2,
    'March': 3,
    'April': 4,
    'May': 5,
    'June': 6,
    'July': 7,
    'August': 8,
    'September': 9,
    'October': 10,
    'November': 11,
    'December': 12}
    return month_to_number


def number_to_weekday_dict():
    number_to_weekday_dict = {0: 'Monday',
    1: 'Tuesday',
    2: 'Wednesday',
    3: 'Thursday',
    4: 'Friday',
    5: 'Saturday',
    6: 'Sunday'}
    return number_to_weekday_dict


def add_to_weekdays_exercised_dict(dictionary, year, month, days_list):
    for day in days_list:
        weekday = find_day_of_week(year, month, day)
        dictionary[weekday] = 1 + dictionary[weekday]
    return dictionary


# Create graph of times exercised vs. the month
def frequency_vs_months_chart(DF):
    days_exercised_in_month = {}
    for row in DF.iloc:
        days_exercised = sum_row(row)


# Create bar chart of times exercised in each day of the week
def frequency_vs_day_chart(DF):
    month_dict = month_to_number_dict()
    times_exercised_in_day_of_week = collections.OrderedDict()

    times_exercised_in_day_of_week = {'Sunday': 0,
    'Monday': 0,
    'Tuesday': 0,
    'Wednesday': 0,
    'Thursday': 0,
    'Friday': 0,
    'Saturday': 0}

    for row in DF.iloc:
        year = row[0]
        month = month_to_number_dict()[row[1]]
        for cell in row[2:0]:  # First 2 elements are the year and month
            days = cell_to_list(cell)
            times_exercised_in_day_of_week = add_to_weekdays_exercised_dict(
                                                    times_exercised_in_day_of_week, year, month, days)
    print(times_exercised_in_day_of_week.values())
    keys_list = list(times_exercised_in_day_of_week.keys())
    values_list = list(times_exercised_in_day_of_week.values())
    plt.style.use("ggplot")
    plt.figure()
    plt.bar(keys_list, values_list, color= 'blue')
    plt.title('Times exercised for each day of week')
    plt.xlabel('Day of week')
    plt.ylabel('Times exercised')
    plt.show()


# Create bar chart of how many times I've done each type of exercise
def frequency_vs_exercise_type(DF):
    exercise_list = list(DF.columns)[2:]  # Ignore the year and month columns
    frequency_of_exercise = collections.OrderedDict()
    for exercise in exercise_list:
        frequency_of_exercise[exercise] = sum_column(DF[exercise])

    plt.style.use("fivethirtyeight")
    plt.figure()
    plt.bar(frequency_of_exercise.keys(), frequency_of_exercise.values(), color='Orange')
    plt.title('Frequency of each type of exercise')
    plt.xlabel('Exercise type')
    plt.ylabel('Frequency')
    plt.show()


# Highlight the days of the year where I exercised
def print_exercise_days(DF):
    pass


def main():
    exercise_data = pd.read_excel(r'C:\Users\leewa\Documents\Important documents\Computer Science\Python Projects\Exercise_Tracking_and_Visualization\Exercise tracking (testing version).xlsx')
    exercise_data.drop(exercise_data.columns[exercise_data.columns.str.contains('unnamed', case = False)], axis = 1, inplace = True)
    frequency_vs_months_chart(exercise_data)
    frequency_vs_day_chart(exercise_data)
    frequency_vs_exercise_type(exercise_data)
    print_exercise_days(exercise_data)


if __name__ == '__main__':
    main()
