__author__ = 'asim'
fruit = 'banana'
len_of_fruit = len(fruit)
index = len_of_fruit
while index > 0:
    letter = fruit[index-1]
    print letter
    index = index-1
    print "Index after decrement:", index



