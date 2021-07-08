'''
@Author: Naziya
@Date: 2021-08-08
@Last Modified by: Naziya
@Last Modified Time: 2021-08-08 23:51:00
@Title: Aim of the program is to calculate the Employee Daily and Monthly Wage.
'''

import random
IS_FULL_TIME = 1
IS_PART_TIME = 2
EMP_RATE_PER_HOUR = 20
PART_TIME_RATE_PER_HOUR = 8


class EmployeeWageBuilder:
    def __init__(self):
        self.check_attendence = 0

    check_attendence = random.randint(0, 1)
    if check_attendence == IS_FULL_TIME:
        emp_hrs = 8
    else:
        emp_hrs = 4
    emp_wage = emp_hrs * EMP_RATE_PER_HOUR
    print("Daily Employee Wage is:", emp_wage)
    part_time_hrs = random.randint(1, 8)
    part_time_wage = part_time_hrs * PART_TIME_RATE_PER_HOUR
    print("Part Time Employee Wages:", part_time_wage)