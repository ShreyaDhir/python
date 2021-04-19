from karel.stanfordkarel import *

# File: shelter.py
# -----------------------------
# The warmup program defines a "main"
# function which should make Karel 
# move to the beeper, pick it up, and
# return home.
def main():
   move()
   # add your code here
   pick_it_up()
   return_to_start()
   
def pick_it_up():
   move()
   turn_right()
   move()
   turn_left()
   move()
   pick_beeper()

def return_to_start():
   turn_around()
   move()
   turn_right()
   move()
   turn_left()
   move()
   move()
   turn_around()
   
def turn_right():
   turn_left()
   turn_left()
   turn_left()
   
def turn_around():
   turn_left()
   turn_left()
   