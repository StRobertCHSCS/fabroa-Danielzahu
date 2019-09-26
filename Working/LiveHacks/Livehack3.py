print("""
----------------------------------------------------------------
┃This program will convert minutes into days, hours and minutes┃
----------------------------------------------------------------
""")
input_minutes = float(input("Input minutes here: "))

days = input_minutes//1440
hours = (input_minutes % 1440)//60
minutes = (input_minutes % 1440) % 60

print(days, "days,", hours, "hours, and", minutes, "minutes.")