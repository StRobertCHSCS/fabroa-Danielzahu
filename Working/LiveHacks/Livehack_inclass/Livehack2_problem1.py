"""
------------------------------------------------------------------------------
Name:      Livehack2_problem1.py
 
Purpose:   To check the type of triangle a user inputs

Author:    Zhu.D

Created:   18/11/2019
------------------------------------------------------------------------------
"""
print ("Welcome to the Triangle checker")

angleone = int(input("Enter the first angle: "))
angletwo = int(input("Enter the second angle: "))
anglethree = int(input("Enter the third angle: "))
anglesum = angleone + angletwo + anglethree 


def triangle_checker(angleone, angletwo, anglethree, anglesum):
    if anglesum != 180:
        print("Error: the angle do not form a triangle.")
    elif angleone and angletwo and anglethree == 60:
        print("A triangle with angles", angleone, angletwo, "and", anglethree, "forms an equilateral triangle.")
    elif angleone == angletwo or angletwo == anglethree or anglethree == angleone:
        print("A triangle with angles", angleone, angletwo, "and", anglethree, "forms a isosceles triangle.")
    elif angleone != angletwo and angletwo != anglethree or anglethree != angleone:
        print("A triangle with angles", angleone, angletwo, "and", anglethree, "forms a scalene triangle.")

triangle_checker(angleone, angletwo, anglethree, anglesum)