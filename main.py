#exercise 5
#question 1
import random
numDice = int(input("How many dice to roll? "))
sumRoll = 0
for i in range (numDice):
    sumRoll += random.randint(1,6)
print("Sum of all dices is: ", sumRoll)
#question 2
print("Enter at least 5 numbers !!!")
listNum = []
num = input("Enter a number: ")
while num != "":
    listNum.append(int(num))
    num = input("Enter a number: ")
listNum.sort(reverse=True)
print("The first 5 greatest numbers are:")
for i in range(5):
    print(listNum[i], end="   ")
#question 3
num = int(input("Give an integer number: "))
halfNum = num // 2
divisible = False
for i in range (2, halfNum+1):
    if num % i == 0:
        divisible = True
        break
if divisible == False:
    print("This is a prime number")
else:
    print("This is not a prime number")
#question 4
citylist = []
print("Enter the name of 5 cities")
for i in range(5):
    citylist.append(input("Name of a city: "))
for i in range(5):
    print(citylist[i])
#excercise6
#question1
import random
def diceroll():
    return random.randint(1,6)
num = diceroll()
while num != 6:
    print(num)
    num = diceroll()
print(num)
#question2
import random
def diceroll(sides):
    return random.randint(1,sides)
numSides = int(input("How many sides the dice has? "))
num = diceroll(numSides)
while num != numSides:
    print(num)
    num = diceroll(numSides)
print(numSides)
#question3
def gallontoLit(gallons):
    return gallons * 3.785
print("Enter negative number to exit")
numgallon = float(input("How many gallons? "))
while numgallon >= 0:
    print(f"Equal to {gallontoLit(numgallon):.4f} litters")
    numgallon = float(input("How many gallons? "))
#question4
def sumlist(intList):
    sumresult = 0
    for i in intList:
        sumresult += i
    return sumresult
predefList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Sum of a list is: ",sumlist(predefList))
#question5
def showlist(intList):
    newlist = []
    for i in intList:
        if i % 2 == 0:
            newlist.append(i)
    print("Old list: ", intList)
    print("New list: ", newlist)
predefList = [1,2,3,4,5,6,7,8,9,10]
showlist(predefList)
#question6
import math
def calc_PricePizza(diameter, price,name):
    areaPizza = math.pi * diameter/2 * diameter/2
    print("The price per square meter of pizza",name,f": {price / (areaPizza * 0.0001):.3f}")
    return price / (areaPizza * 0.0001)
dia1 = float(input("Enter the diameter of pizza 1 in cm: "))
price1 = float(input("Enter the price of pizza 1 in euro: "))
dia2 = float(input("Enter the diameter of pizza 2 in cm: "))
price2 = float(input("Enter the price of pizza 2 in euro: "))
if calc_PricePizza(dia1,price1,1) < calc_PricePizza(dia2,price2,2):
    print("Pizza 1 is cheaper than pizza 2")
elif calc_PricePizza(dia1,price1,1) > calc_PricePizza(dia2,price2,2):
    print("Pizza 2 is cheaper than pizza 1")
else:
    print("Same price")
