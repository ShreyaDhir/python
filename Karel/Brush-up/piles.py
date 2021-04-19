from karel.stanfordkarel import *

# File: piles.py
# -----------------------------
# The warmup program defines a "main"
# function which should make Karel
# pick up all the beepers in the world.
def main():
   move()
   # add your code here
   pick_beepers()
   move()
   pick_beepers()
   move()
   pick_beepers()
   
def pick_beepers():
   for i in range(10):
     pick_beeper()
   move()