##got to build the suspense as we need to import time

import time
import random
import Killer_Behind_the_door
import Woods_Scene

def main():

    user_survive = False

    print("Hello there!!")
    time.sleep(1)
    print("Please tell us your name:")
    userName = str(input(">"))

    number_one = random.randint(1,100)

    if number_one % 2 != 0:
        Killer_Behind_the_door.behindDoorSceneOne()

    else:
        print(userName,", you find yourself lost in the woods.")

        time.sleep(5)

        Woods_Scene.woods(userName)


main()