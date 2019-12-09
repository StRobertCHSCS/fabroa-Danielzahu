"""
-------------------------------------------------------
Name: problemtwo.py

Purpose: Driving distance tracker

Author: Daniel Zhu

Created: 9/12/2019
-------------------------------------------------------
"""

print("*** Welcome to the distance tracker. ***")

# takes distance and number of days value
distance = 0
days = 0

# while the distance is under 100, it will keep on taking in values for
# distance while updating the days value by one evey time
while distance < 100:
    new_distance = int(input("enter the distance traveled for today: ")) 
    distance = distance + new_distance
    days = days + 1

# print the final statements
print("It took", days, "to pass 100 km")
print("The average distance per day is", str(distance/days), "km.")
