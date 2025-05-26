# -*- coding: utf-8 -*-
"""
Created on Mon May 26 18:05:20 2025

@author: omrky
"""

class Employees():
    def __init__(self, firstName, lastName):
        self.__firstName=firstName
        self.__lastName=lastName
        
    def set_first_name(self,fName):
        self.__firstName=fName
        
    def set_last_name(self,lName):
        self.__lastName=lName
    
    def get_first_name(self):
        return self.__firstName
    
    def get_last_name(self):
        return self.__lastName
    
    def print_employee(self):
        print("First Name: ",self.get_first_name())
        print("Last Name: ",self.get_last_name())
        
class CommissionEmployee(Employees):
    def __init__(self, firstName, lastName, commission_rate, gross_sales):
        Employees.__init__(self, firstName, lastName)
        self.__commission_rate=commission_rate
        self.__gross_sales=gross_sales
    
    def set_commission_rate(self,commission_rate):
        self.__commission_rate=commission_rate
        
    def set_gross_sales(self,gross_sales):
        self.__gross_sales=gross_sales
        
    def get_commission_rate(self):
         return self.__commission_rate
     
    def get_gross_sales(self):
        return self.__gross_sales
    
    def print_employee(self):
        super().print_employee()
        print("Commission Rate: ",self.get_commission_rate())
        print("Gross Sales: ",self.get_gross_sales())
        
        
    def earnings(self):
        print("Earning: ",self.get_commission_rate()*self.get_gross_sales(),"\n")
    
class BasePlusCommissionEmployee(CommissionEmployee):
    def __init__(self, firstName, lastName, commission_rate, gross_sales, base_salary):
        CommissionEmployee.__init__(self, firstName, lastName, commission_rate, gross_sales)
        self.__base_salary=base_salary
        
    def set_base_salary(self,base_salary):
        self.__base_salary=base_salary
      
    def get_base_sales(self):
        return self.__base_salary
    
    def print_employee(self):
        super().print_employee()
    
    def earnings(self):
        print("Earning: ",self.get_base_sales()+(self.get_commission_rate()*self.get_gross_sales()),"\n")
        
    