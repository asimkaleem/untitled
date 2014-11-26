largest = None
smallest = None

while True:
    try:
        num = raw_input("Enter a number: ")
        if num == "done":
            break
        num = float(num)
        if num > largest:
            largest = num
        if smallest is None:
            smallest = num
        elif num < smallest:
            smallest = num
    except:
        print "Invalid Input"

print "Maximum is ", int(largest)
print "Minimum is ", int(smallest)