import time
import random
import DidYouSurviveYourOwnHorrorMovie

def PlayAgain():
    print('Do you want to play again? y/n:')
    playAgain = str(input(">"))

    playAgain = playAgain.lower()

    # a while loop to make this game start over if the player wants it to be
    if playAgain == 'y':
        DidYouSurviveYourOwnHorrorMovie.main()
    elif playAgain == 'n':
        exit()
