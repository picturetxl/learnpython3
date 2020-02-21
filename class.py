'''
@Author: your name
@Date: 2020-02-20 15:58:24
@LastEditTime: 2020-02-20 16:42:43
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /python/class.py
'''

# 类：狗类
# 属性:name and age
#　方法：sit roll_over
class Dog():
    # 构造器
    def __init__(self,name,age):#self必不可少　且位于第一个
        print("in init")
        self.name = name 
        self.age = age
        

    def sit(self):# 必须要有self
        print(self.name.title() + " is now sitting.")

    def do_nothing(self):
        print("do...")

    def roll_over(self):
        print(self.name.title()+" roll over!")

my_dog = Dog('willie',6)
my_dog.sit()
my_dog.do_nothing()
print("My dog's name is "+my_dog.name.title() + ".")
print("My dog's is "+str(my_dog.age) + " years old.")



class Car():
    def __init__(self,make,model,year):
        print("in Car init")
        self.make = make
        self.model = model
        self.year = year
        self.odmeter_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year)+' '+self.make +' '+self.model
        return long_name.title()
    
    def read_odometer(self):
        print("this car has "+str(self.odmeter_reading)+" miles on it")

    def update_odometer(self,mileage):
        if mileage >= self.odmeter_reading:
            self.odmeter_reading = mileage
        else:
            print("you can't roll back an odometer!")

    def increament_odometer(self,miles):
        self.odmeter_reading+=miles

    def fill_gas_tank(self):
        print("fill gas tank!!")

#　这就是继承
class ElectricCar(Car):
    def __init__(self,make,model,year):
        print("in ElectricCar init")
        super().__init__(make,model,year)
        self.battery_size = 70

    def describe_battery(self):
        print("This car has a "+ str(self.battery_size) +"-kWh battery.")

    def fill_gas_tank(self):
        print("This car does't need a gas tank!!")

my_car = Car('car','car s',2016)
my_car.fill_gas_tank()

my_tesla = ElectricCar('tesla','model s',2016)
my_tesla.describe_battery()
my_tesla.fill_gas_tank()
