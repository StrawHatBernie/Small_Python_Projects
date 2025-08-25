import random
# taking in range for random number
number1, number2 = input("Enter two numbers: ").split()
num1_int = int(number1)
num2_int = int(number2)
# generate random number
random_num = int(random.randrange(num1_int, num2_int))
# ask for guess
guess = int(input(f"Guess a number between {number1} and {number2}: "))
# check guess with random number
while(guess != random_num):
    if(guess >= random_num):
        guess = int(input("Guess is too high, guess again: "))
    elif(guess <= random_num):
        guess = int(input("Guess is too low, guess again: "))
print(f'Correct guess, good job! The number was {random_num}')
