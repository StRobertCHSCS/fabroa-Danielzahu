"""
-------------------------------------------------------
Name: problemone.py

Purpose: Heating days average calculator

Author: Daniel Zhu

Created: 9/12/2019
-------------------------------------------------------
"""
print("*** Heating days tracker ***")
# take the input for number of days
numofdays = int(input("Enter number of days to track: "))

# num is the number of heating days, will be updated using an if loop every
# time the temperature is below 15 degrees
num = 0
for x in range(numofdays):
    temp = int(input())
    if temp < 15:
        num = num + 1

# print final statement
print("There are", num, "heating days.")