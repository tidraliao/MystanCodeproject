"""
File: Steeplechase.py
Name: Tidra
---------------------------------
TODO:
"""

from karel.stanfordkarel import *


def main():
    """
    Karel crosses hurdles in a 12x12 world
    with a for loop 
    """
    for i in range(11):
        if front_is_clear():
            move()
        else:
            jump()


def jump():
    """
    pre-condition:Karel is on the left side of the wall,facing East.
    post-condition:Karel is on the right side of the wall.
    """
    up()
    cross()
    down()


def up():
    """
    pre-condition:Karel is on the left side of the wall,facing East.
    post-condition:Karel is at the upper left of the wall facing north.
    """
    # alternative
    # while not front_is_clear():
    #     turn_left()
    #     move()
    #     turn_right()

    turn_left()
    while not right_is_clear():
        move()


def turn_right():
    #Karel will turn left three times.
    turn_left()
    turn_left()
    turn_left()


def cross():
    """
    pre-condition:Karel is at the upper left of the wall facing north.
    post-condition:Karel is at the upper right of the wall facing south.
    """
    turn_right()
    move()
    turn_right()



def down():
    """
    pre-condition:Karel is at the upper right of the wall facing south.
    post-condition:Karel is at the downside right of the wall facing East.
    """
    while front_is_clear():
        move()
    turn_left()



# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
