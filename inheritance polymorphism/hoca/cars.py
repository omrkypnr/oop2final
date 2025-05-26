
class Car:
    
    def __init__(self,brand,model,power,speed):
        self.__brand = brand
        self.__model = model
        self.__power = power
        self.__max_speed = speed
        print("\nInitializer for",self.__brand,self.__model)
        
    def set_brand(self,brand):
        self.__brand = brand
    
    def set_model(self,model):
        self.__model = model
    
    def set_power(self,power):
        self.__power = power
        
    def set_max_speed(self,speed):
        self.__max_speed = speed
        
    
    def get_brand(self):
        return self.__brand
    
    def get_model(self):
        return self.__model
    
    def get_power(self):
        return self.__power
        
    def get_max_speed(self):
        return self.__max_speed
    
    def print_car(self):
        print("Brand:",self.get_brand())
        print("Model:",self.get_model())
        print("Power:",self.get_power(),"HP")
        print("Max Speed:",self.get_max_speed(), "km/h")
    
    
class GasCar(Car):
    
    def __init__(self,brand,model,power,speed,fuel,co2,tank):
        
        Car.__init__(self,brand,model,power,speed)
        
        self.__fuel_type = fuel
        self.__co2_emission = co2
        self.__fuel_tank_volume = tank
        
    
    def set_fuel_type(self,fuel):
        self.__fuel_type = fuel
    
    def set_co2_emission(self,co2):
        self.__co2_emission = co2
    
    def set_fuel_tank_volume(self,tank):
        self.__fuel_tank_volume = tank
    
    
    def get_fuel_type(self):
        return self.__fuel_type
    
    def get_co2_emission(self):
        return self.__co2_emission
    
    def get_fuel_tank_volume(self):
        return self.__fuel_tank_volume
    
    
    def print_car(self):
        super().print_car()
        print("Fuel Type:",self.get_fuel_type())
        print("CO2 Emission:",self.get_co2_emission(), "g/km")
        print("Fuel Tank Volume:",self.get_fuel_tank_volume(),"L")
        
    
class ElectricCar (Car):
    
    def __init__(self,brand,model,power,speed,time,bat_type,bat_cap):
        
        Car.__init__(self,brand,model,power,speed)
        
        self.__charging_time = time
        self.__battery_type = bat_type
        self.__battery_capacity = bat_cap
   
    
    def set_charging_time(self,time):
        self.__charging_time = time
    
    def set_battery_type(self,bat_type):
        self.__battery_type = bat_type
        
    def set_battery_capacity(self,bat_cap):
        self.__battery_capacity = bat_cap
    
    
    def get_charging_time(self):
        return self.__charging_time
    
    def get_battery_type(self):
        return self.__battery_type
        
    def get_battery_capacity(self):
        return self.__battery_capacity
    
    def print_car(self):
        super().print_car()
        print("Charging Time:",self.get_charging_time(),"hours")
        print("Battery Type: ",self.get_battery_type())
        print("Battery Capacity: ",self.get_battery_capacity(),"kW/h")
    
    
    
    
    
    
    