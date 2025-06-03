#Maşın işləkdir mi deyil mi +
#Maşını işə salmaq/söndürmək +
#Maşını sürmək +
#Maşının benzini 

class Car:
    def __init__(self, color, capacity, fuel, engine_power, motor_oil,l_per_km, oil_per_km):
        self.color = color
        self.capacity = capacity
        self.fuel = fuel
        self.engine_power = engine_power
        self.motor_oil = motor_oil
        self.l_per_km = l_per_km
        self.oil_per_km = oil_per_km
        #######################
        self.__total_km = 0 #Private
        self.__is_running = False #Private
        
    
    @property
    def is_running(self):
        return self.__is_running
    
    def toggle(self):
        if self.__is_running:
            self.__is_running = False

        else:
            self.__is_running = True

    def drive(self,driven_km):
        if driven_km <= 0:
            raise ValueError('Driven km must be positive')
        
        if not self.__is_running:
            raise ValueError('Car should be started to drive') 

        total_fuel = driven_km * self.l_per_km
        if self.fuel < total_fuel:
            raise ValueError('Not enough fuel')
        
        total_oil = driven_km * self.oil_per_km
        if self.motor_oil < total_oil:
            raise ValueError('Not enough oil')
        
        self.motor_oil -= total_oil # transaction.atomic
        self.fuel -= total_fuel
        self.__total_km += driven_km

    def fuel_car(self, added_fuel):
        if added_fuel <= 0:
            raise ValueError('Fuel must be positive')
        
        if (added_fuel + self.fuel) > self.capacity:
            raise ValueError('Fuel exceeds the capacity')
        
        self.fuel += added_fuel

    def oil_car(self, added_oil):
        if added_oil <= 0:
            raise ValueError('oil must be positive')
        
        self.motor_oil += added_oil

    @property
    def total_km(self):
        return self.__total_km


        
mercedes = Car('white',100, 0, 660, 5, 0.15,0.01)

# print(mercedes.is_running)
# mercedes.drive(10) error 
mercedes.toggle()
# print(mercedes.is_running)
# mercedes.drive(10) error
# mercedes.fuel_car(200) error
mercedes.fuel_car(50) 
# print(mercedes.fuel)
mercedes.drive(10)
print('Fuel:',mercedes.fuel)
print('Oil:',mercedes.motor_oil)

print('Total km:', mercedes.total_km)

mercedes.drive(10)
print('Fuel:',mercedes.fuel)
print('Total km:', mercedes.total_km)

mercedes.drive(100)

print('Fuel:',mercedes.fuel)
print('Total km:', mercedes.total_km)

mercedes.toggle()
print(mercedes.is_running)
# mercedes.drive(10)
# print('Fuel:',mercedes.fuel)
# print('Total km:', mercedes.total_km)

#Maşına benzin vurularkən motor sönlü olmalıdır.
#Maşın yağı ilə bağlı ( toggle )
