print("""
-----------------------------------------------------------------
Name:       problem1.py

Purpose:    To convert degrees celsius to degrees fahrenheit.

Author:     Zhu.D

Created:    02/10/2019
-----------------------------------------------------------------
""")
# takes the temperature in celsius from the user, stores it in a variable
celsius = float(input("Input temperature here(celsius): "))
# uses the formula to convert celsius into fahrenheit, stores it in a variable
fahrenheit = (9/5) * celsius + 32

# prints the temperature in fahrenheit
print(fahrenheit, "degrees fahrenheit")
