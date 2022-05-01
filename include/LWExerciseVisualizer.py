# This program visualizes several exercise statistics

from functools import reduce
import datetime
import collections
import pandas as pd
import matplotlib.pyplot as plt


# Converts an Excel spreadsheet's cell into a list
# cell is a string of format "[days exercised separated by commas]""
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
    sum = reduce(lambda x, y: x + len(cell_to_list(y)), column, 0)  # Initialize sum to 0
    return sum


# Finds the sum of the lengths of all the lists in a row
def sum_row(row):
    row = row[2:]  # First 2 rows will always be year and month
    sum = reduce(lambda x, y: x + len(cell_to_list(y)), row, 0)
    return sum


def month_to_number_dict():
    month_to_number = {'January': 1, 'February': 2, 'March': 3, 'April': 4,
                        'May': 5, 'June': 6, 'July': 7, 'August': 8,
                        'September': 9, 'October': 10, 'November': 11, 'December': 12}
    return month_to_number


def number_to_weekday_dict():
    number_to_weekday_dict = {0: 'Monday', 1: 'Tuesday',
                                2: 'Wednesday', 3: 'Thursday',
                                4: 'Friday', 5: 'Saturday',
                                6: 'Sunday'}
    return number_to_weekday_dict


# Returns the day of the week, based on the year, month, and day (all ints), as a string
# Returns Sunday, Monday, Tuesday, etc. as strings
def find_day_of_week(year, month, day):
    weekday = datetime.date(year, month, day).weekday()
    return number_to_weekday_dict()[weekday]


# Increments, in a dictionary, the number of times exercised for a particular weekday
# year and month are the years and month in ints (i.e., January is 1, February is 2, and so on)
# days_list is a list of days in a particular year and month
# Returns the dictionary
def add_to_weekdays_exercised_dict(dictionary, year, month, days_list):
    for day in days_list:
        weekday = find_day_of_week(year, month, day)
        dictionary[weekday] = 1 + dictionary[weekday]
    return dictionary


# Create graph of times exercised vs. the month
def frequency_vs_months_chart(DF):
    days_exercised_in_month = collections.OrderedDict()
    for row in DF.iloc:  # For each row in the data
        year = str(row[0])[-2:]  # Only retrieve the last 2 digits of the year
        month = row[1][0:3]  # Only retrieve the first 3 letters of each month
        month_year = month + " '" + year  # Format the month and year
        times_exercised = 0
        for cell in row[2:]:  # First 2 elements are the year and month
            days = cell_to_list(cell)
            times_exercised = len(days) + times_exercised
        days_exercised_in_month[month_year] = times_exercised
        
    plt.figure()
    plt.plot(days_exercised_in_month.keys(), days_exercised_in_month.values(), color='green')
    plt.title('Times exercised for each month')
    plt.xlabel('Month')
    plt.ylabel('Times exercised')
    plt.show()


# Create bar chart of times exercised in each day of the week
def frequency_vs_day_chart(DF):
    month_dict = month_to_number_dict()
    times_exercised_in_day_of_week = collections.OrderedDict()
    times_exercised_in_day_of_week = {'Sunday': 0, 'Monday': 0,
                                        'Tuesday': 0, 'Wednesday': 0,
                                        'Thursday': 0, 'Friday': 0,
                                        'Saturday': 0}
    for row in DF.iloc:  # For each row in the data
        year = row[0]
        month = month_dict[row[1]]
        for cell in row[2:]:  # First 2 elements are the year and month
            days = cell_to_list(cell)
            times_exercised_in_day_of_week = add_to_weekdays_exercised_dict(
                                                times_exercised_in_day_of_week, year, month, days)

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
    month_dict = month_to_number_dict()
    date = datetime.date(2021, 7, 18)
    for row in DF.iloc:  # For each row in the data
        year = row[0]
        month = month_dict[row[1]]
        for cell in row[2:]:  # First 2 elements are the year and month
            pass


# Returns a pandas DataFrame of the data in file_name, an Excel spreadsheet holding the exercise
# data 
def read_data(file_name):
    exercise_data = pd.read_excel(file_name)
    exercise_data.drop(exercise_data.columns[exercise_data.columns.str.contains('unnamed',
                                                            case = False)], axis = 1, inplace = True)
    return exercise_data


def main():
    exercise_data = read_data('Exercise tracker.xlsx')
    frequency_vs_months_chart(exercise_data)
    frequency_vs_day_chart(exercise_data)
    frequency_vs_exercise_type(exercise_data)
    print_exercise_days(exercise_data)


if __name__ == '__main__':
    main()
