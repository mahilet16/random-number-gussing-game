
#number guessing game
import random
import guessgame
print(guessgame.logo)
print("Welcome to the number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty=input("Choose a difficulty. Type 'easy' or 'hard' :")

def cheek_answer():
    global guess
    guess=int(input("Make a guess: "))
    if guess>number:
        print("Too high.")
    elif guess<number:
        print("Too low.")
    elif guess==number:
        print(f"You got it! The answer was {number}.")
    else:
        print("you entered invalid number guess between 1-100.")
    

def game():
    global number
    number=random.randint(1,100)
    if difficulty=="hard":
        for i in range(5,0,-1):
            print(f"You have {i}  attempts remaining to guess the number.")
            cheek_answer()
            if guess==number:
                break    
            if guess!=number and i==1:
                print(f"you are out of guesses, you lose the number is {number}")
                break
            print("Guess again.")
    else:
        for i in range(10,0,-1):
            print(f"You have {i}  attempts remaining to guess the number.")
            cheek_answer()
            if guess==number:
                break
            if guess!=number and i==1:
                print("you are out of gesses, you lose")
    again=input("do u want to play again 'y' or 'n' ")    
    if again=="y":
        game()
game()           
 