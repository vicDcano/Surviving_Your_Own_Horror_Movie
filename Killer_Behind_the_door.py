import time
import GameOver

def behindDoorSceneOne():


    print("The killer is behind your door.")

    time.sleep(3)

    print("The killer is slowly turning the doorknob")

    time.sleep(3)

    print("You did not survive")

    GameOver.PlayAgain()
