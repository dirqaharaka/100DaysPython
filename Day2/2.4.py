#Number manipulation and F string in Python

bmi = 84 / 1.65 ** 2
print(bmi)

print(int(bmi))

print(round(bmi))

print(round(bmi, 2))


score = 0

#user score a point
score += 1
print(score)


#f_string
print("Your score is " + str(score))


score = 0 
height = 1.8
is_winning = True

print(f"Your score is {score}, your height is {height}, You are winning is {is_winning}")