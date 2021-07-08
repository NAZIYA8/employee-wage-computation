'''
@Author: Naziya
@Date: 2021-08-08
@Last Modified by: Naziya
@Last Modified Time: 2021-08-08 0:20:00
@Title: Aim of the program is to calculate the Employee Daily and Monthly Wage.
'''

import random
from typing import DefaultDict
IS_FULL_TIME = 1
IS_PART_TIME = 2
EMP_RATE_PER_HOUR = 20
PART_TIME_RATE_PER_HOUR = 8


class EmployeeWageBuilder:
    def __init__(self, check_attendence=0, emp_hrs=0, emp_wage=0):
        self.check_attendence = check_attendence

    switch = random.randint(1, 3)
    if switch == 1:
        emp_hrs = 8
    elif switch == 2:
        emp_hrs = 4
    else:
        emp_hrs = 0
    emp_wage = emp_hrs * EMP_RATE_PER_HOUR
    print("Employee Wage is:", emp_wage)