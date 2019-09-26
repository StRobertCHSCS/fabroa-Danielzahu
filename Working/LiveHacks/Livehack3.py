print("""
----------------------------------------------------------------
┃This program will convert minutes into days, hours and minutes┃
----------------------------------------------------------------
""")
minutes = int(input("Input minutes here: "))
print((minutes//1440), "days,", ((minutes % 1440)//60), "hours, and", 
((minutes % 1440) % 60), "minutes.")