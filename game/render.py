from pygame import font, draw, mouse
from game.modules.button import *


def load_store(window, store, gameConf):
    store.read()
    mapping = store.mapping
    for pos in mapping['play1']:
        draw.circle(window, 'black', pos, 10)
        store.play1.append(pos)
        store.position.remove(pos)
        gameConf.isWin(store.play1, pos)
    for pos in mapping['play2']:
        draw.circle(window, 'white', pos, 10)
        store.play2.append(pos)
        store.position.remove(pos)
        gameConf.isWin(store.play2, pos)
    gameConf.reload = False


def render_chessboard(window, windowConf):
    ft = font.SysFont('SimHei', 20)
    for i in range(windowConf.grid):
        text = ft.render(str(i + 1), True, 'black')
        text1 = ft.render(chr(i + 65), True, 'black')
        window.blit(text, (
            (windowConf.grid+1)*windowConf.grid_size, windowConf.grid_size*(i+1)-5
        ))
        window.blit(text1, (
            windowConf.grid_size*i +
            30, (windowConf.grid+1)*windowConf.grid_size-5
        ))
        draw.line(window, 'black', (20, 20+i *
                                    windowConf.grid_size), (20+windowConf.grid_size*windowConf.grid,
                                                            20+i*windowConf.grid_size), 1)
        draw.line(window, 'black', (20+i*windowConf.grid_size, 20), (
            20+i*windowConf.grid_size, 20+windowConf.grid_size*windowConf.grid
        ), 1)
        if i == 0:
            draw.line(window, 'black', (20, 20 + i * windowConf.grid_size),
                      (20+windowConf.grid_size*windowConf.grid, 20+i*windowConf.grid_size), 4)
            draw.line(window, 'black', (20 + i * windowConf.grid_size, 20),
                      (20+i*windowConf.grid_size, 20 + windowConf.grid_size*windowConf.grid), 4)
        if i == windowConf.grid-1:
            draw.line(window, 'black', (20, 20+(i+1)*windowConf.grid_size),
                      (20+(i+1)*windowConf.grid_size, 20+(i+1)*windowConf.grid_size), 4)
            draw.line(window, 'black', (20+(i+1)*windowConf.grid_size, 20),
                      (20+(i+1)*windowConf.grid_size, 20+(i+1)*windowConf.grid_size), 4)


def render_btn(back_btn, window, windowConf):
    if back_btn.click(mouse.get_pos()):
        back_btn = Button('返回', 'white', (windowConf.grid+3) *
                          windowConf.grid_size, windowConf.grid_size*6)
    else:
        back_btn = Button('返回', 'red', (windowConf.grid+3) *
                          windowConf.grid_size, windowConf.grid_size*6)
    back_btn.display(window)


def render_status(window, windowConf, gameConf):
    text = ''
    ft = font.SysFont('SimHei', 30)
    if gameConf.count % 2 == 0:
        text = '你的回合'
    elif gameConf.count % 2 == 1:
        text = '等待对手'
    else:
        text = '游戏结束'
    window.blit(ft.render(text, True, 'red'), ((windowConf.grid+3) *
                windowConf.grid_size, windowConf.grid_size*4))
