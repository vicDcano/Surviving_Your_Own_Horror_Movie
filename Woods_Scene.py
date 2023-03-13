import time
import random
import GameOver

def woods(userName):

    number_two = random.randint(1,50)

    if number_two % 2 !=0:
        print("The killer pops up and slashes your arm.")

        time.sleep(5)

        GameOver.PlayAgain()

    else:
        print("The killer tries to stab you but you were faster than them.")
        time.sleep(5)