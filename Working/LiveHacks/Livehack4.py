print("""
This program will get the temperature(celsius) and windspeed(km/h), and
outputs the wind chill factor. Please do not input any units
----------------------------------------------------------------------------
""")
temp = int(input("Input temperature here: "))
wind = int(input("Input windspeed here (km/h): "))
wind_chill = 13.12 + (.6215 * temp) - (11.37 * wind ** 0.16) + (.3965 * temp * wind ** 0.16)
print("The wind chill factor is:", round(wind_chill, 2))
