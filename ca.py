
'''create a simple number guessing game. write a python program that use user input number between 1 and 100 and asks the user to guess it. the user will have 5 attempts to guess the number. for each guess tell user if the number is higher, lower or correct. use loop to handle the Guess and conditionals statement for feedback.'''

number=int(input("Enter a number between 1 and 100: "))
guess=0
count=0
while count<5:
    guess=int(input("Enter your guess: "))
    count+=1
    if guess<number:
        print("Your guess is lower than the number.")
        print(" ")
    elif guess>number:
        print("Your guess is higher than the number.")
        print(" ")
    else:
        print(" ")
        print("Congratulations! You guessed the number")
        print(" ")
        break
else:
    print(" ")
    print("You have exceeded the number of attempts. The number was",number)
    print(" ")
  