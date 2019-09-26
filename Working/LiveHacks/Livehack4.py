print("""
------------------------------------------------------------------------------
┃ This program will take the temperature (celsius) and windspeed (km/h), and ┃
┃ outputs the wind chill factor (degrees celsius). Please do not input units ┃
------------------------------------------------------------------------------
""")

temp = float(input("Input temperature here: "))
wind = float(input("Input windspeed here (km/h): "))
wind_chill = 13.12 + (.6215 * temp) - (11.37 * wind ** 0.16) + (.3965 * temp * wind ** 0.16)

print("The wind chill factor is:", round(wind_chill, 2))
