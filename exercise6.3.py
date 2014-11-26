__author__ = 'asim'
sentence = raw_input("Please enter the string: ")
letter_to_count = raw_input("Please enter letter to count: ")

def wordcount(string, letter):
    count = 0
    for letters in string:
        if letters == letter:
            count = count + 1
    return count

print wordcount(sentence,letter_to_count)



