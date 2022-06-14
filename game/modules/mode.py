from pygame import draw, display
import random
import socket
from threading import Thread
import json


def connectServer():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("127.0.0.1", 8080))
    s.setblocking(True)
    return s


def syncData(gameConf, store, window):
    while gameConf.socket != None:
        display.update()
        data = gameConf.socket.recv(1024)
        json_data = json.loads(data.decode('utf-8'))
        gameConf.count = json_data['count']
        if gameConf.count % 2 == 0:
            tmpl = json_data['play2'].split(',')
            pos = (int(tmpl[0][1:]), int(tmpl[1][:len(tmpl[1])-1]))
            draw.circle(window, 'black', pos, 10)
            store.play2.append(pos)
            store.position.remove(pos)
            gameConf.isWin(store.play2, pos)
        if gameConf.count % 2 == 1:
            tmpl = json_data['play1'].split(',')
            pos = (int(tmpl[0][1:]), int(tmpl[1][:len(tmpl[1])-1]))
            draw.circle(window, 'white', pos, 10)
            store.play1.append(pos)
            store.position.remove(pos)
            gameConf.isWin(store.play1, pos)
        display.update()


def multiplayer_online(window, windowConf, gameConf, store, event):
    x, y = event.pos
    for pos in store.position:
        if (pos[0] - 10) < x < (pos[0] + 10) and (pos[1] - 10) < y < (pos[1] + 10):
            data = '(' + str(pos[0]) + ',' + str(pos[1]) + ')'
            gameConf.socket.send(data.encode('utf-8'))


def multiplayer_offline(window, windowConf, gameConf, store, event):
    x, y = event.pos
    for pos in store.position:
        if (pos[0] - 10) < x < (pos[0] + 10) and (pos[1] - 10) < y < (pos[1] + 10):
            if gameConf.count % 2 == 0:
                draw.circle(window, 'black', pos, 10)
                store.play1.append(pos)
                store.position.remove(pos)
                gameConf.isWin(store.play1, pos)
            if gameConf.count % 2 == 1:
                draw.circle(window, 'white', pos, 10)
                store.play2.append(pos)
                store.position.remove(pos)
                gameConf.isWin(store.play2, pos)
            window.fill('white', ((windowConf.grid+3) *
                                  windowConf.grid_size, windowConf.grid_size*4, (windowConf.grid+3) *
                                  windowConf.grid_size+50, windowConf.grid_size*4+50))
            gameConf.count += 1


def single_player_offline(window, windowConf, gameConf, store, event):
    if gameConf.count % 2 == 0:
        x, y = event.pos
        for pos in store.position:
            if (pos[0] - 10) < x < (pos[0] + 10) and (pos[1] - 10) < y < (pos[1] + 10):
                draw.circle(window, 'black', pos, 10)
                store.play1.append(pos)
                store.position.remove(pos)
                gameConf.isWin(store.play1, pos)
                window.fill('white', ((windowConf.grid+3) *
                                      windowConf.grid_size, windowConf.grid_size*4, (windowConf.grid+3) *
                                      windowConf.grid_size+50, windowConf.grid_size*4+50))
                gameConf.count += 1
    elif gameConf.count % 2 == 1:
        pos = store.position[random.randint(0, len(store.position)-1)]
        draw.circle(window, 'white', pos, 10)
        store.play2.append(pos)
        store.position.remove(pos)
        gameConf.isWin(store.play2, pos)
        window.fill('white', ((windowConf.grid+3) *
                              windowConf.grid_size, windowConf.grid_size*4, (windowConf.grid+3) *
                              windowConf.grid_size+50, windowConf.grid_size*4+50))
        gameConf.count += 1
        display.update()
