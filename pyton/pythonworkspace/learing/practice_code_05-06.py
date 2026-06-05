# # print hello word
print("Hello")
#
# #Take a user name as input and print a greeting
def greeting(name):
    print("Welcome mr",name)
#
name=input("Enter your name ")
greeting(name)
#
# #Find whether a number is even or odd
def Evnorodd(number):
    ans = number % 2
    if ans == 0:
         print(f'Given {number} number is Even ')
    else:
         print(f'given number {number} is odd')
number = int(input("Enter the number to check even or odd"))
Evnorodd(number)
#
# #fing the largest in three number
def largeinthree(a,b,c):
     if (a > b) and (a > c):
         print(f'{a} is grests')
     elif (b > a) and (b > c):
         print(f'{b} is the grestest')
     else:
         print(f'{c} is the grest')

a = int(input("Enter numbers"))
b= int(input("Enter the number"))
c=int(input("enter the numbers"))
largeinthree(a,b,c)

#calculate the factorial of the number

def fac(num):
     fact = num
     for i in range(num-1):
         print(i)
         fact *=(num-1)
         num = (num - 1)

     print(f'{num} factorial is {fact}')
num = int(input("enter the number"))
fac(num)

# find the sum of 1 to n
def sumofnum(num):
     sumo=num
     for i in range(num):
         sumo+=i
         print(sumo)
     print(f'Sum of given number {num} id {sumo}')

def sumofnnum(num):
     sumo=(num*(num+1)/2)
     print(f'sum of n {sumo}')

num = int(input('enter number'))
sumofnum(num)
sumofnnum(num)

#reverse a string
def rev(name):
     temp=name[::-1]
     print(f'Rverse of give string{name} is {temp}')


name=input("enter the name")
rev(name)

#Count the number of vowels in string

#Given string is palinrome or not
def pal(string):
     temp=string[::-1]
     if string == temp:
         print(f'given strin {string} is palindrom')
     else:
         print(f'given strin {string} is not palindrom')

name=input("enter the name")
pal(name)






