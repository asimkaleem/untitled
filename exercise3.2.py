# Exercise 3.2 Rewrite your pay program using try and except so that your program handles non-numeric input gracefully
# by printing a message and exiting the program. The following shows two executions of the program:
# 3.11. Exercises
# 41
# Enter Hours: 20
# Enter Rate: nine
# Error, please enter numeric input
# Enter Hours: forty
# Error, please enter numeric input

try:
    weekly_hours = float(raw_input("Please enter your weekly hours:"))
    hourly_rate = float(raw_input("Please enter your hourly rate:"))

    extra_hours = weekly_hours - 40
    extra_rate = 1.5 * hourly_rate

    if weekly_hours > 40:
        weekly_pay = extra_hours*extra_rate + 40 * hourly_rate
        print "Your pay for this week will be: ", weekly_pay
    else:
        weekly_pay = weekly_hours*hourly_rate
        print "Your pay for this week will be: ", weekly_pay

except:
    print "Please enter numeric input"



