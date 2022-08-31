#!/usr/bin/python
# -*- encoding: utf-8 -*-
import time
import seaborn


# IDEA
# Import and Initialization
import pygame
from objects.Screen import Screen
start = time.time()
import objects.Screen
from objects.Game import Game

pygame.init()

# Display configuration
screen = Screen('Hit the Mole!', 800, 600)
# Entities
game = Game(screen)
# Run Game
end = time.time()
print("the program takes %f.4 to run" % (end-start))
game.start()


#if __name__ == '__main__':
#    game.start()

print("x")


