from game import engine
from game.store import *
from game.config import *
from game.modules.io import getFileName


def start(any, filename, isReload):
    if filename == '':
        filename = getFileName()
    store.path = './map/' + filename
    gameConf.reload = isReload
    gameConf.goals = any.goals.get()
    gameConf.multiplayer = any.mutilplayer.get()
    gameConf.online = any.online.get()
    windowConf.grid = any.grid.get()
    gameConf.port = any.port.get()
    gameConf.ip = any.ip.get()
    if gameConf.port != -1 and gameConf.ip != '':
        gameConf.online = True
    any.app.withdraw()
    engine.launch()
    any.app.deiconify()
