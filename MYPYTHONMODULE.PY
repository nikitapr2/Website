# python

import math

print("square root:",math.sqrt(81))
print("square of :",math.pow(5,3))
print("factorial:",math.factorial(5))

# import random


number=random.randint(1,10)
print(number)

print(random.choice(["anushka","kajal","anchal","shradha"]))

# import datetime

today=datetime.date.today()
print(today)

currenttime=datetime.date.datetime.now()
print(currenttime)



# import statistics

marks=[50,40,20,40,80,60,70]

print(statistics.mean(marks))
print(statistics.median(marks))
print(statistics.mode(marks))


# import os

print(os.name)
print(os.getcwd())
os.mkdir("module_today")




# question
import calculator
a=80
b=20
print(calculator.xyz(80,20))
print(calculator.sub(80,20))
print(calculator.mul(80,20))
print(calculator.div(80,20))
total=calculator.a + calculator.b
print(total)
from calculator import mul,xyz
print(xyz(80,20))


# math ModuleNotFoundError
import math
print("square root:",math.sqrt(64))
print("square of:",math.pow(13,2))
print("factorial:",math.factorial(7))


# Random quiz

import random
question=["what is the exception ?",
          "what is the IDE ?",
          "Stand for OOP ?"]
question=random.choice(question)
print("random quiz question:")
print(question)