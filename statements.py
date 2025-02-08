#check for even or odd number
number = int(input("Enter a number: "))

if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")
print()

#Compare two numbers and compare which one is larger
num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))

if num1 > num2:
    print(f"{num1} is greater than {num2}")
elif num2 > num1:
    print(f"{num2} is greater than {num1}")
else:
    print("They are equal...")
print()

#Grade classification
grade = int(input("Enter number from 0-100: "))
if grade >= 60 and grade <= 79:
    print(f"Your score is {grade}% and you got a B. Good Job!")
elif grade >= 40 and grade <= 59:
    print(f"Your score is {grade}% and you got a C. Keep going!")
elif grade >= 20 and grade <= 39:
    print(f"Your score is {grade}% and you got a D. Work hard!")
elif grade >= 0 and grade <= 19:
    print(f"Your score is {grade}% and you got a F. Get help!")
else:
    print(f"Your score is {grade}% and you got an A. Excellent Job!")