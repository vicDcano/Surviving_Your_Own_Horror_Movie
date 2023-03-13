import time
import random
import DidYouSurviveYourOwnHorrorMovie

def PlayAgain():
    print('Do you want to play again? y/n:')
    playAgain = str(input(">"))

    playAgain = playAgain.lower()

    # a while loop to make this game start over if the player wants it to be

    while playAgain == playAgain == 'y':
        DidYouSurviveYourOwnHorrorMovie.main()

    if playAgain == "n":
        exit()
