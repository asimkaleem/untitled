try:
    work_hours = float(raw_input("Please enter worked hours for last week: "))
    hourly_rate= float(raw_input("Please enter your hourly rate: "))
    bonus_rate = float(raw_input("Please enter your bonus rate: "))
    if work_hours <= 40:
        print "Your pay for last week will be", work_hours*hourly_rate
    elif work_hours > 40:
        extra_hours = work_hours - 40.0
        normal_hours = work_hours - extra_hours
        print "Your pay along with bonus hours will be"
        print (normal_hours*hourly_rate)+(extra_hours*(hourly_rate*bonus_rate))
except:
    print "Please give numerical values"