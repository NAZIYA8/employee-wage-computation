'''
@Author: Naziya
@Date: 2021-08-08
@Last Modified by: Naziya
@Last Modified Time: 2021-08-08 09:15:00
@Title: Aim of the program is to calculate the Employee Daily and Monthly Wage.
'''

import random

class EmployeeWageBuilder:
    def __init__(self):
        self.check_attendence = 0

    check_attendence = random.randint(0, 1)
    if check_attendence == 1:
        print('Employee is present')
    else:
        print('Employee is absent')