'''
@Author: Naziya
@Date: 2021-08-08
@Last Modified by: Naziya
@Last Modified Time: 2021-09-08 01:07:00
@Title: Aim of the program is to calculate the Employee Daily and Monthly Wage.
'''

import random
from typing import List

IS_FULL_TIME = 1
IS_PART_TIME = 2
EMP_RATE_PER_HOUR = 20
PART_TIME_RATE_PER_HOUR = 8
NO_WORKING_DAYS = 20
MAX_HRS_IN_MONTH=100



class EmployeeWageBuilder:
    def __init__(self, check_attendence=0, emp_hrs=0, emp_wage=0, total_emp_wage=0, total_working_days=0,total_working_hours=0):
        self.check_attendence = check_attendence
        self.emp_hrs = emp_hrs
        self.emp_wage = emp_wage
        self.total_emp_wage = total_emp_wage
        self.total_working_days = total_working_days
        self.total_working_hours = total_working_hours
        self.list = []

    def total_employee_wage(self):
        """
        Description:
        This function is used for calculating the total employee wage.
        Parameter:
        self is an instance of the objects.
        """

        while self.total_working_hours <= MAX_HRS_IN_MONTH and self.total_working_days < NO_WORKING_DAYS:
            self.total_working_days = self.total_working_days + 1
            type_of_employee = random.randint(1, 3)
            self.emp_hrs = self.get_work_hours(type_of_employee)
            self.total_working_hours = self.total_working_hours + self.emp_hrs
            self.emp_wage = self.emp_hrs * EMP_RATE_PER_HOUR
            self.total_emp_wage = self.total_emp_wage + self.emp_wage
            self.list.append(self.emp_wage)
        print("Total Conditional Wage:", self.total_emp_wage)
    
    

    def print_monthly_wage(self):
        """
        Description:
        This function is used for printing the monthly wage.
        Parameter:
        self is an instance of the objects
        """
        i=1
        for item in self.list:
            print("Day:" + str(i) + ", Wage: " + str(item))
            i=i+1

    def get_work_hours(self, value):
        """
        Description:
        This function is used for calculating employee daily work hours.
        Parameter:
        value is used for getting employee daily hour if an employee is of
        full time it will store 8 and if employee is of part time it will store 4.
        self is an instance of the objects
        """

        switcher = {
        1: 8, 2: 4, 3: 0
        }
        return switcher.get(value, "hi")
