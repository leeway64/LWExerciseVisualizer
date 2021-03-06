import unittest
import pandas as pd
import os
import sys
from LWExerciseVisualizer import *


class TestExerciseVisualizerMethods(unittest.TestCase):
    def test_cell_to_list(self):
        self.assertEqual(cell_to_list("[]"), [])
        self.assertEqual(cell_to_list("[10101010100]"), [10101010100])
        self.assertEqual(cell_to_list("[1,2,3,4]"), [1,2,3,4])
        self.assertEqual(cell_to_list("[1,2,3,4,5,6,7,8]"), [1,2,3,4,5,6,7,8])
        self.assertEqual(cell_to_list("[10,2,38,900,1000000]"), [10,2,38,900,1000000])
    
    def test_sum_row(self):
        df = pd.read_excel(f'{os.path.dirname(__file__)}/exercise_tracking_test_1.xlsx')
        df.drop(df.columns[df.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)
        self.assertEqual(sum_row(df.iloc[0]), 8)
        self.assertEqual(sum_row(df.iloc[1]), 19)
        self.assertEqual(sum_row(df.iloc[2]), 4)
    
    def test_sum_column(self):
        df = pd.read_excel(f'{os.path.dirname(__file__)}/exercise_tracking_test_1.xlsx')
        df.drop(df.columns[df.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)
        self.assertEqual(sum_column(df['Running']), 23)
        self.assertEqual(sum_column(df['Strength']), 12)
        self.assertEqual(sum_column(df['Testing1']), 0)

    def test_find_day_of_week(self):
        self.assertEqual(find_day_of_week(2021, 7, 5), 'Monday')
        self.assertEqual(find_day_of_week(2021, 7, 4), 'Sunday')
        self.assertEqual(find_day_of_week(2020, 4, 1), 'Wednesday')
        self.assertEqual(find_day_of_week(2019, 6, 7), 'Friday')

    def test_add_to_weekdays_exercised_dict(self):
        times_exercised_in_day_of_week = {'Sunday': 0, 'Monday': 0,
                                            'Tuesday': 0, 'Wednesday': 0,
                                            'Thursday': 0, 'Friday': 0,
                                            'Saturday': 0}

        times_exercised_in_day_of_week = add_to_weekdays_exercised_dict(
                                            times_exercised_in_day_of_week, 2021, 7, list(range(4, 11)))

        for key in times_exercised_in_day_of_week.keys():
            self.assertEqual(times_exercised_in_day_of_week[key], 1)


# Manual functional testing (comment out unittest.main() to run)
def functional_tests():
    exercise_data1 = read_data(f'{os.path.dirname(__file__)}/exercise_tracking_test_1.xlsx')
    exercise_data2 = read_data(f'{os.path.dirname(__file__)}/exercise_tracking_test_2.xlsx')

    # Testing frequency vs. months
    frequency_vs_months_chart(exercise_data1)

    # Testing frequency vs. day
    frequency_vs_day_chart(exercise_data2)

    # Testing frequency vs. exercise type
    frequency_vs_exercise_type(exercise_data1)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise RuntimeError("Incorrect number of arguments! Enter either unit (for unit testing) or func (for functional testing).")
    
    if sys.argv[1] == "unit":
        print("Running unit tests:")
        unittest.main(argv=['first-arg-is-ignored'], exit=False)
    elif sys.argv[1] == "func":
        print("Running functional tests:")
        functional_tests()
    else:
        raise RuntimeError("Enter either unit (for unit testing) or func (for functional testing).")

