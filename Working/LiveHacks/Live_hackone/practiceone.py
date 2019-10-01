print("""
---------------------------------------------------------------------
Name: practiceone.py
Purpose: A program that converts fahrenheit to celsius

Author: Daniel Zhu

Created: 01/10/2019
--------------------------------------------------------------------
""")
# get fahrenheit from user
fahrenheit = float(input("Input temperature in degrees fahrenheit: "))
# compute celsius from fahrenheit
celsius = (5/9) * (fahrenheit - 32)
# output celsius
print(celsius, "degrees celsius") 