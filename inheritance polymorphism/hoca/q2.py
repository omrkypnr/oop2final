
import cars

def main():
    
    my_gas_car = cars.GasCar("Volkswagen","Golf", 115,198,"Diesel",109,50)
    my_gas_car.print_car()
    
    my_electrical_car=cars.ElectricCar("Tesla","Model S", 301,193,20,"Li-ion",60)
    my_electrical_car.print_car()
    
main()
