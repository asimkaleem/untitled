# Exercise 3.1 Rewrite your pay computation to give the employee 1.5 times the
# hourly rate for hours worked above 40 hours.
# Enter Hours: 45
# Enter Rate: 10
# Pay: 475.0

weekly_hours = float(raw_input("Please enter your weekly hours:"))
hourly_rate = float(raw_input("Please enter your hourly rate:"))

extra_hours = weekly_hours - 40
extra_rate = 1.5 * hourly_rate

if weekly_hours > 40:
    #extra_hours = weekly_hours - 40
    weekly_pay = extra_hours*extra_rate + 40 * hourly_rate
    print "Your pay for this week will be: ", weekly_pay
else:
    weekly_pay = weekly_hours*hourly_rate
    print "Your pay for this week will be: ", weekly_pay




