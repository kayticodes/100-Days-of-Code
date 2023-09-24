# A file for practice challenges to go
import random

# Rock Paper sizzors
print("Let's play Rock Paper Sissors!")
player = str.lower(input("what's your move? R, P, or S? "))
comp = random.randint(1, 3)

if player == "r":
    print("you chose rock")
    if comp == 1:
        print("The computer also chose rock - it's a draw!")
    if comp == 2:
        print("The computer chose paper - the computer wins!")
    if comp == 3:
        print("The computer chose sissors - You Win!")
        

# Flip a coin game
# print("Welcome to this flipping game!")
# random_int = random.randint(1, 10)
# if random_int % 2 == 0:
#     print("heads")
# else:
#     print("tails")



# Find odd or even challenge
# num = input("please enter an integer: ")
# if int(num) % 2 == 0:
#     print(f"{num} is an even integer.")
# else:
#     print(f"{num} is an odd integer.")

# Practice Challenge
# yrs = 90 - int(input("What is your current age? "))
# print(yrs)
# days = yrs * 365
# weeks = yrs * 52
# months = yrs * 12
# print(f"you have {days} days, {weeks} weeks, and {months} months left. ")

# Practice with strings
# num = input("please provide a 2 digit number: ")
# first = int(num[0])
# second = int(num[1])
# print(first + second)