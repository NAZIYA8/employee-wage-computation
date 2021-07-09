'''
@Author: Naziya
@Date: 2021-08-08
@Last Modified by: Naziya
@Last Modified Time: 2021-09-08 01:08:00
@Title: Aim of the program is to calculate the Employee Daily and Monthly Wage.
'''

from employee_wage_builder import EmployeeWageBuilder
if __name__ == '__main__':
    emp = EmployeeWageBuilder()
    emp.total_employee_wage()
    emp.print_monthly_wage()
