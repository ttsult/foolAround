import random


def guess(x):

    random_number = random.randint(1, x) # computer gives us a random number

    guess = 0 # initalize the guess variable 

    chances = 3 # you have three guesses until the game is over 

    activated = False # utilized to determine if the input is valid or not 

    while (guess != random_number): # go until you get it right 
        guess = int(input(f'Guess a number between 1 and {x}: '))  # initalize the user's input 

        if (guess > x or guess < 1): # this part checks if the user's input is valid or not 
            print('Invalid Input, Please try again')
        else: 
            activated = True  # if activated is True, that means the program recieved a valid input

        if (guess < random_number and activated == True): # if the guess is over the actual number 
            print('Sorry, guess again. Too low. ')

            chances -= 1

            if (chances == 1):  # syntax case 
                print(f'This is your last chance!')
            else :
                print(f'You have {chances} chances remaining!')  

        elif (guess > random_number and activated == True):
            print('Sorry, guess again. Too high.')
            
            chances -= 1

            if (chances == 1):
                print(f'This is your last chance!')
            else:
                print(f'You have {chances} chances remaining!') 
                
        if (chances == 0): # end of the game case 
            print('GAMEOVER, YOU LOSE!!!')
            print(f'The Number was {random_number}')
            break 
    if (chances > 0): # if you complete the game before you run out of chances, then you WIN!
        print(f'Yay. CONGRATS. You have guessed the number {random_number} correctly')
    

guess(10)


