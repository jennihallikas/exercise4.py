"""
# 1 1-1000
number = 1
while number <= 1000:
    modulo = number % 3
    if modulo == 0:
     print(str(number))
    number = number+1

# 2 Write a program that converts inches to centimeters until the user inputs a negative value. Then the program ends.
inches = float(input("Enter length in inches: "))
while inches >= 0:
    centimetres = inches * 2.54
    print(f"The length in centimetres is: {centimetres:.2f}")
    inches = float(input("Enter the length in inches: "))

#3 Write a program that asks the user to enter numbers until they enter an empty string to quit.
# Finally, the program prints out the smallest and largest number from the numbers it received.
number = int(input("Enter a number: "))
largest = number
smallest = number
while number !="":
 if number <= smallest:
    smallest = number
 if number >= largest:
    largest = number
 number = (input("Enter next number or leave an empty string to quit."))
 if number == "":
     break
print (f"Smallest number is: {smallest: .2f} and largest number is: {largest: .2f}")

inputnum = input("Enter a number:")
if inputnum != "":
    smallest = int(inputnum)
    largest = int(inputnum)
    while inputnum != "":
        if int(inputnum) < smallest:
            smallest = int(inputnum)
        if int(inputnum) > largest:
            largest = int(inputnum)
        inputnum = input("Enter a number:")

    print("Smallest number is: ", smallest)
    print("The largest number is: ", largest)
else:
    print("Please input at least 1 number.")


import random

# 4 Write a game where the computer draws a random integer between 1 and 10.
# The user tries to guess the number until they guess the right number.
# After each guess the program prints out a text:
# Too high, Too low or Correct. Notice that the computer must not change the number between guesses.

randomnum = random.randint(1,10)
userguess= int(input("Guess a number between 1-10."))
while userguess != randomnum:
        if userguess < randomnum:
            print("Too low.")
        elif userguess > randomnum:
            print("Too high.")
        userguess = int(input("Guess another number."))
print("Yay, your answer is correct!")

import random

randomnum = random.randint(1,10)
guess = int(input("Please insert your guess."))
def checknumber(guess)
    while randomnum != guess:
        if guess < randomnum:
            print("Your guess is too low")
        elif guess > randomnum:
            print("Your guess is too high")
        elif guess == randomnum:
            print("Your guess is correct")
        int(input("Guess another number."))
checknumber

#5 Username and password
username = "python"
password = "rules"
attempt = 0
passw = ""
username = ""
while not (passw == password and user == username):  # everything needs to be defined always
    attempt += 1 # keeps repeating it until you get it right
    user = (input("Please write your username: "))
    passw = (input("Please write your password: "))
    if attempt == 5: # when attempts reach 5, program will finish
        print("Access denied.")
        break
    elif user == username and passw == password:
        print("Welcome") # if the user puts the correct username and password
    else:
        print("Try again.")
"""
# 5 Pi

import random
interval = int(input("Please insert Points number."))

circle_points = 0
square_points = 0


for i in range(interval ** 2):

    rand_x = random.uniform(-1, 1)
    rand_y = random.uniform(-1, 1)

    origin_dist = rand_x ** 2 + rand_y ** 2

    if origin_dist <= 1:
        circle_points += 1

    square_points += 1

    pi = 4 * circle_points / square_points


print("Final Estimation of Pi=", pi)





