# Exercise 4.7 Rewrite the grade program from the previous chapter using a func-
# tion called computegrade that takes a score as its parameter and returns a grade
# as a string.


try:
    score = float(raw_input("Please enter score between 0.0 and 1.0: "))
except:
    score = "Not A Number"

def computegrade(score_to_grade):
    if score < 0.6 and score >= 0.0:
        grade = "F"
        return  grade
    elif score >= 0.6 and score < 0.7:
        grade = "D"
        return  grade
    elif score >= 0.7 and score < 0.8:
        grade = "C"
        return  grade
    elif score >= 0.8 and score < 0.9:
        grade = "B"
        return  grade
    elif score >= 0.9 and score <= 1.0:
        grade = "A"
        return  grade
    else:
        grade = "Bad Score"
        return grade

result = computegrade(score)
print result
