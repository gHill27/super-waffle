#Welcome to the amazing world of alcholol. Take a seat and some burnetts. You're gonna need it to read this terrible code....
import pygame
import random
import time
import Bartender_Classes

"""SCREENS"""
START = 1
STATS = 2
LEADERBOARD = 3
SETTINGS = 4
BREWING = 5
current_screen = START

bob = "amazing"




pygame.init()
SCREEN = pygame.display.set_mode((500,500), pygame.HWSURFACE)
RUNNING = True
while RUNNING:
    SCREEN.fill((0,0,0))
    SCREEN.fill
    for event in pygame.event.get():
        if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
            RUNNING = False
    pygame.display.update()
pygame.quit()


def display_start():
    pass


while True: 
    if current_screen == START:
        display_start()
