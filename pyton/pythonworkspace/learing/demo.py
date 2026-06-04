##Function
import math # using this we can use all the function in that module.
#from math import sqrt  " this specficaly call only one function from the module.
def sdd():
    a,b=5,9
    c=a+b
    return c

def add(a,b):
    """it is adds to value"""
    c = a + b
    return c

def mul(a,b):
    c = a*b
    return c
def sub(a,b):
    c=a-b
    return c

def sq(num):
    re=math.sqrt(num)##math is the module using that only we call sqrt is the function.
    return re


print(sdd())
print(add(5,2))
print(mul(5,2))
print(sub(5,2))
print(sq(144))
