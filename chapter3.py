try:
    first_number = float(raw_input("Please enter first number: "))
    second_number = float(raw_input("Please enter second number: "))
except:
    print"Please Enter only numbers!"
if first_number==second_number:
    print "First number is same as the second one"
else:
    if first_number < second_number:
        print"First Number is less than second one!"
    elif first_number > second_number:
        print "First Number is greater than second one!"


