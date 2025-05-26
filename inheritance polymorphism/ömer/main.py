# -*- coding: utf-8 -*-
"""
Created on Fri May 23 18:41:29 2025

@author: omrky
"""

import Cars

def main():
    my_gas_car = Cars.GasCar("Volvo", "Golf", 115, 198, "diesel", 109, 50)
    my_gas_car.print_car()     
    
    my_elec_car = Cars.ElectricCar("Tesla", "Model s", 301, 193, 20, "Li-ion", 60)
    my_elec_car.print_car()
main()


