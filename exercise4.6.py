
# Exercise 4.6 Rewrite your pay computation with time-and-a-half for overtime
# and create a function called computepay which takes two parameters (hours and rate).


weekly_hours = float(raw_input("Please enter your weekly hours:"))
hourly_rate = float(raw_input("Please enter your hourly rate:"))

def computepay(hours,rate):
    extra_hours = weekly_hours - 40
    extra_rate = 1.5 * hourly_rate
    if weekly_hours > 40:
        weekly_pay = extra_hours*extra_rate + 40 * hourly_rate
        return weekly_pay
    else:
        weekly_pay = weekly_hours*hourly_rate
        return weekly_pay

pay = computepay(weekly_hours,hourly_rate)
print "Your Pay is:", pay
