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

page = router.route("""Insert the name of the starting page here""")
pageToResume = None

# | Main game loop
while True:
    page.update()
    page.draw()

    # | Loop to allow the current page to handle each event there may be
    for event in pygame.event.get():
        action = page.handleEvent(event)

        if action in pages: # | If the action is a valid page

            if action == "Pause": # | Pause and store the page if needed
                page.pause()
                pageToResume = page

            page = router.route(action) # | Route to the new page

        elif action == "Resume": # | Resume to the previous page
            page = pageToResume
            page.unpause()

        Helpers.checkForQuit(event)

    pygame.display.update()
    clock.tick(FPS)

