# Exercise 3.3 Write a program to prompt for a score between 0.0 and 1.0. If the
# score is out of range print an error. If the score is between 0.0 and 1.0, print a
# grade using the following table:
# Score       GRADE
# >= 0.9      A
# >= 0.8      B
# >= 0.7      C
# >= 0.6      D
# < 0.6       F

try:
    score = float(raw_input("Please enter score between 0.0 and 1.0: "))
except:
    score = "Not A Number"
    # print score
    # print type(score)
if type(score) == 'float':
    if score < 0.6 and score >= 0.0:
        print "F"
    elif score >= 0.6 and score < 0.7:
        print "D"
    elif score >= 0.7 and score < 0.8:
        print "C"
    elif score >= 0.8 and score < 0.9:
        print "B"
    elif score >= 0.9 and score <= 1.0:
        print "A"
    else:
        print "Out of range"
else:
    print "Please enter numbers only"




