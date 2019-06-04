part_name = "electricity bill calculation"

# number of days for the months
JANUARY = MARCH = MAY = JULY = AUGUST = OCTOBER = DECEMBER = January = March = May = July = Agust = October = December = january = march = may = july = agust = october = december = 31
APRIL = JUNE = SEPTEMBER = NOVEMBER = April = June = September = November = april = june = september = november = 30
FEBRUARY = February = february = 28

# Price per kWh of electric, including taxes
UnitPrice = 0.6788

# How much user consumed electricity per month?
MonthlyConsumption = input ("Enter your monthly electricity consumption in kWh: ")

# Which month's bill the user wants to know?
term = input ("""Which month would you like to calculate the bill? """)

# We convert the data from the input () function to a format that # Python can understand
Month = eval(term)

# Daily electricity consumption of the user
DailyConsumption = int(MonthlyConsumption) / Month

#bill amount
bill = UnitPrice * DailyConsumption * Month

dash = "-" * 20
print (dash)
print (part_name)
print (dash)
print ("Daily Consumption: \t" , DailyConsumption , " kWh \n" , "Estimated Bill Amount: \t" , bill , " TL" , sep="")