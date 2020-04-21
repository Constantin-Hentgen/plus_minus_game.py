from random import randint
import os

print("WELCOME TO THE PlusMinus GAME!")
game = input("Do you want to play?  ")

while game == "yes":
    hide = randint(0,100)
    retry = int(input("Enter a retry number:  "))
    while retry<0:
        retry = int(input("Enter a valid value for the retry number:  "))
    test=int(input("Enter a value:  "))
    for i in range(1,retry):
        if test < hide:
            test=int(input("Value too low, retry:  "))
        elif test > hide:
            test=int(input("Value too high, retry:  "))
        else:
            print("You've won, GG WP")
            i=retry
    if i >= retry:
        print("You lose :(")
    game=input("In fact, you can't retry because the game ended ! Do you want to play again?  ")

os.system('Pause')
