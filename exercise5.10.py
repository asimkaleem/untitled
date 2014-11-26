__author__ = 'asim'
total_count = 0
total_sum = 0
user_input = 0

while True:
    try:
        inpt = raw_input(" Enter a Number: ")
        if inpt != 'done':
            num = float(inpt)
            total_count = total_count + 1
            total_sum = total_sum + num
            average = total_sum/total_count
            print "here is what you gave ", num

        elif inpt == 'done':
            print "we are done taking inputs"
            print "Total counts: ", total_count
            print "Total Sum: ", total_sum
            print "Total Average: ", average
            break
    except:
        print "Bad Data"




