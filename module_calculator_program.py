#1. improting a single function from a module:
from calculator_module import add
ad = add(5,6)
print(ad)

#2. importing multiple functions from a module
from calculator_module import add, sub
ad = add(5,3)
print(ad)
su =  sub(9,4)
print(su)

#3. importing all functions from module
from calculator_module import *
ad = add(5,3)
print(ad)
su =  sub(9,4)
print(su)


#4. importing module into the current namespace
#from calculator_module
import calculator_module
ad=calculator_module.add(5,6)
print("Addition is : ", ad)
su=calculator_module.sub(7,8)
print("Difference is: ", su)
mu=calculator_module.mul(110,10)
print("Product is: ",mu)
di=calculator_module.div(110,10)
print("Division is : ", di)
