#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
nbStr = str(number)
for i in nbStr:
    last = i
last = int(last)
if number < 0:
    last = last * (-1)
print("Last digit of %d" % number, end=" ")
print("is %d" % last, end=" ")
if last > 5:
    print("and is greater than 5")
elif last == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")