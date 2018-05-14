# CK

import pygame
import os
from src import Helpers
from src.Router import Router

os.environ['SDL_VIDEO_CENTERED'] = '1'  # | This centers the window
pygame.init()

screenWidth = 0  # | The width of the window
screenHeight = 0  # | The height of the window
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("""The caption""")

FPS = 0  # | The FPS to use
clock = pygame.time.Clock()

pages = ["""The pages that are in this game"""]

router = Router(screen)

page = router.route("MainMenu")
pageToResume = None

while True:
    page.update()
    page.draw()

    for event in pygame.event.get():
        action = page.handleEvent(event)

        """Page changes go here"""

        Helpers.checkForQuit(event)

    pygame.display.update()
    clock.tick(FPS)

