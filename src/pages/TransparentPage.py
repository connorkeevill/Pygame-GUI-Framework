# CK

import pygame
from src.pages.Page import Page
from src.resources import colours

# | TransparentPage()
# |------------------------------------------------------
# | Class for a page with a semi-transparent background,
# | e.g a paused screen showing the game behind it.
# |--------------------------------------------
class TransparentPage(Page):
    def __init__(self, surface, pageName, opacity=7):
        Page.__init__(self, surface, pageName)

        self.opacity = opacity

        # | Generate the semi transparent background to make a page of this nature
        self.backgroundSurface = self.createBackgroundSurface()

    def draw(self):
        self.surface.blit(self.backgroundSurface, (0, 0))
        self.drawObjects()


    # | createBackGroundSurface()
    # |----------------------------------------------------------------
    # | Creates the surface to be the background for this page. Needed
    # | to allow a semi-transparent background to be displayed here.
    # |----------------------------------------------------------
    def createBackgroundSurface(self):
        backgroundSurface = pygame.Surface((self.surface.get_width(), self.surface.get_height()))
        backgroundSurface.fill(colours.grey)
        backgroundSurface.set_alpha(self.opacity)

        return backgroundSurface
