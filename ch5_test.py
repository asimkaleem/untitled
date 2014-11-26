# coding=utf-8
#example 5.1
#
# n = 5
# while n > 0:
#     print "hello there", n
#     print "printing condition", n > 0
#     n = n-1
# print "Blastof"

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#example 5.1
# n = 10
# while True:
#     print n, '\n'
#     n = n - 1
# print 'Done!'

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# while True:
#     line = raw_input('> ')
#     if line == 'done':
#         break
#     print line
# print 'Done!'

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# while True:
#     line = raw_input('> ')
#     if line[0] == '#':
#         continue
#     if line == 'done':
#         break
#     print line
# print 'Done!'

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# friends = ['Joseph', 'Glenn', 'Sally']
# for friend in friends:
#     print 'Happy New Year:', friend
# print 'Done!'

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# count = 0
# for itervar in [3, 41, 12, 9, 74, 15]:
#     count = count + 1
# print 'Count: ', count

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# total = 0
# for itervar in [1, 2, 3, 4, 5, 6, 7]:
#     print "Total: ", total
#     total += itervar
# print "Total: ", total

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# largest = None
# print "Before: ", largest
# for itervar in [3, 41, 12, 9, 74, 15]:
#     if largest is None or itervar > largest:
#         largest = itervar
#     print "Loop", itervar, "    Largest So far:", largest
# print "Largest: ", largest

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# smallest = None
# print "Before: ", smallest
# for itervar in [3, 41, 12, 9, 74, 15,0]:
#     if smallest is None or itervar < smallest:
#         smallest = itervar
#     print "Loop", itervar, "    Smallest so far:", smallest
# print "Smallest: ", smallest
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Exercise 5.1 Write a program which repeatedly reads numbers until the user en-
# ters “done”. Once “done” is entered, print out the total, count, and average of
# the numbers. If the user enters anything other than a number, detect their mistake
# using try and except and print an error message and skip to the next number.

# total = 0
# count = 0
# average = 0
#
# while True:
#     number = raw_input("Please number or" + " done" + " to give the results : ")
#     if number != 'done':
#         try:
#             number = float(number)
#             total = total + number
#             count = count + 1
#             average = total/count
#         except:
#             print "Please enter numbers"
#
#     elif number == 'done':
#         print "Total:", total
#         print "Count:", count
#         print "AVG:", average
#         break
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Exercise 5.2 Write another program that prompts for a list of numbers as above
# and at the end prints out both the maximum and minimum of the numbers instead
# of the average.

# largest = None
# smallest = None
# temp = None
#
#
# while True:
#     number = raw_input("Please number or" + " done" + " to give the results : ")
#     if number != 'done':
#         try:
#             if temp == None:
#                 temp = float(number)
#                 largest = temp
#                 smallest = temp
#             elif float(number)>=largest:
#                 largest = float(number)
#             elif float(number)<=smallest:
#                 smallest = float(number)
#         except:
#             print "Please enter numbers"
#     elif number == 'done':
#         print "Maximum:", largest
#         print "Minimum:", smallest
#         break


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is
# entered, print out the largest and smallest of the numbers. If the user enters anything other than a valid number
# catch it with a try/except and put out an appropriate message and ignore the number. Enter the numbers from the book
# for problem 5.1 and Match the desired output as shown.
# largest = None
# smallest = None
# temp = None
#
# while True:
#     num = raw_input("Enter a number: ")
#     if num == "done":
#         break
#     elif num != 'done':
#         try:
#             if temp == None:
#                 temp = int(num)
#                 largest = temp
#                 smallest = temp
#             elif int(num)>=largest:
#                 largest = int(num)
#             elif int(num)<=smallest:
#                 smallest = int(num)
#         except:
#             print "Please enter numbers only"
#
# print "Maximum", largest
# print "Minimum", smallest

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# if smallest is None :
#     smallest = value











