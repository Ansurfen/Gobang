import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from mvc.constants import *
from mvc.routes import *


class Client:
    def __init__(self):
        self.app = ttk.Window('Gobang', 'journal', size=(250, 250))
        self.default()
        self.useRoutes()
        self.app.mainloop()

    def default(self):
        self.pages = {}
        self.grid = ttk.IntVar(self.app, value=15)
        self.goals = ttk.IntVar(self.app, value=4)
        self.mutilplayer = ttk.BooleanVar(self.app, value=True)
        self.online = ttk.BooleanVar(self.app, value=False)
        self.ip = ttk.StringVar(self.app, value='')
        self.port = ttk.IntVar(self.app, value=-1)

    def useRoutes(self):
        self.pages[HOME_PAGE] = HomePage(self)
        self.pages[OFFLINE_PAGE] = OfflinePage(self)
        self.pages[ONLINE_PAGE] = OnlinePage(self)
        self.pages[SELECT_PAGE] = SelectPage(self)
