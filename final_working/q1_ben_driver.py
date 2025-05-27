# -*- coding: utf-8 -*-
"""
Created on Mon May 26 19:00:00 2025

@author: omrky
"""

import q1_ben as emp

def main():
    my_employee= emp.Employees("John", "Smith")
    my_employee.print_employee()
    
    my_comm_employee= emp.CommissionEmployee("Sue", "Jones", 10000, 0.6)
    my_comm_employee.print_employee()
    my_comm_employee.earnings()
    
    my_base_comm_employee=emp.BasePlusCommissionEmployee("Bob", "Lewis", 5000, 0.4, 300)
    my_base_comm_employee.print_employee()
    my_base_comm_employee.earnings()
    
main()