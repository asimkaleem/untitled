__author__ = 'asim'
total_count = 0
total_sum = 0
highest_num = 0
lowest_num = -1

while True:
    try:
        inpt = raw_input(" Enter a Number: ")
        if inpt != 'done':
            num = float(inpt)
            total_count = total_count + 1
            total_sum = total_sum + num

            if num > highest_num:
                highest_num = num
            elif num < highest_num:
                lowest_num = num
            average = total_sum/total_count
            print "here is what you gave ", num

        elif inpt == 'done':
            print "we are done taking inputs"
            print "Total counts: ", total_count
            print "Total Sum: ", total_sum
            print "Total Average: ", average
            print "Highest Number entered: ", highest_num
            print "Lowest Number entered: ", lowest_num
            break
    except:
        print "Bad Data"




