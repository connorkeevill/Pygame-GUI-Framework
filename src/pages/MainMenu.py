#CK

from src.pages.Page import Page

class MainMenu(Page):
    def __init__(self, surface, pageName):
        Page.__init__(self, surface, pageName)

        """
        This is the first page that will be opened when the application starts, 
        buttons, title and other objects can be added here.
        """