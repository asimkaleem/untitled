width = 17
height = 12.0


print "width/2 =", width/2
#this will  8

print "width/2 =", width/2.0
#this will  8.5

print "Heigth/3= ",height/3
#this will  4.0

print 1 + 2 * 5
#this will 11

temp_celsius = raw_input("Please enter temp in Celsius: ")
try:
    cel = float(temp_celsius)
    print "Temp in Farenheit will be ", (cel)*1.8 + 32.00
except:
    print " Please enter numbers"





