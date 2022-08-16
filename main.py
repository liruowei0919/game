#!/usr/bin/python
# -*- encoding: utf-8 -*-


# IDEA
# Import and Initialization
import pygame
from objects.Screen import Screen

import objects.Screen
from objects.Game import Game

pygame.init()

# Display configuration
screen = Screen('Hit the Mole!', 800, 600)
# Entities
game = Game(screen)
# Run Game
game.start()


#if __name__ == '__main__':
#    game.start()

print("x")


