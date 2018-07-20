#CK

from src.pages.MainMenu import MainMenu

# | Router()
# |-----------------------------------------------
# | Class to route the application to each page,
# | by returning a page instance based on the
# | string inputted into the route() method.
# |-------------------------------------
class Router:
    def __init__(self, screen):
        self.screen = screen
        self.page = None

        self.routes = {"MainMenu":self.createMainMenu,
                       """The game's routes""":"""" go here"""}

    # | route()
    # |----------------------------------------------------
    # | Returns a new instance of the class relating to
    # | the route that was passed into the method
    # |-------------------------------------
    def route(self, route):
        self.page = route
        return self.routes[route]()

    def createMainMenu(self):
        return MainMenu(self.screen, self.page)

