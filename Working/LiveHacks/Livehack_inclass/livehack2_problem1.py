"""
------------------------------------------------------------------------------
Name:      Livehack2_problem1.py
 
Purpose:   To calculate BMI of user

Author:    Zhu.D

Created:   18/11/2019
------------------------------------------------------------------------------
"""

weight = float(input("Enter your weight(kg): "))
height = float(input("Enter your height(m): "))

bmi = weight/height ** 2

def bmi_category(bmi):
    if bmi < 18.5:
        print("You are underweight")
    if bmi >= 18.5 and bmi <= 25:
        print("Your weight is normal")
    if bmi > 25:
        print("You are overweight")

bmi_category(bmi)

