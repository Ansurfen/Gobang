import pygame
import tkinter.messagebox as msgbox
from game.config import *
from game.render import *
from game.store import *
from game.modules.timer import *
from game.modules.button import *
from game.modules.mode import *


def launch():
    pygame.init()
    pygame.display.set_caption('Gobang')
    window = pygame.display.set_mode(((windowConf.grid+8)*windowConf.grid_size,
                                      (windowConf.grid+2)*windowConf.grid_size))
    window.fill(styleConf.window_bg_color)
    pygame.draw.rect(window, styleConf.chessboard_bg_color, (20, 20,
                     windowConf.grid_size*windowConf.grid, windowConf.grid*windowConf.grid_size))
    render_chessboard(window, windowConf)
    pygame.display.update()
    clockController = Timer()
    pygame.time.set_timer(clockController.TIMEOUT, 1000)
    timeFont = pygame.font.SysFont(None, 60)
    timeText = timeFont.render(
        clockController.toString(), True, styleConf.timer_color)
    back_btn = Button('返回', 'red', (windowConf.grid+3) *
                      windowConf.grid_size, windowConf.grid_size*6)
    back_btn.display(window)
    if gameConf.online:
        gameConf.connect()
        Thread(target=syncData, args=(
            gameConf, store, window,), daemon=True).start()
    while gameConf.survive:
        clockController.clock.tick(60)
        if gameConf.reload:
            load_store(window, store, gameConf)
        render_btn(back_btn, window, windowConf)
        render_status(window, windowConf, gameConf)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameConf.survive = False
                exit()
            if event.type == MOUSEBUTTONDOWN or (not gameConf.multiplayer and gameConf.count % 2 == 1 and not gameConf.online):
                if gameConf.multiplayer and not gameConf.online:
                    multiplayer_offline(window, windowConf,
                                        gameConf, store, event)
                elif not gameConf.multiplayer and not gameConf.online:
                    single_player_offline(
                        window, windowConf, gameConf, store, event)
                elif gameConf.online:
                    multiplayer_online(window, windowConf,
                                       gameConf, store, event)
            if event.type == clockController.TIMEOUT:
                if gameConf.count == 0.5:
                    pygame.time.set_timer(clockController.TIMEOUT, 0)
                clockController.add()
                timeText = timeFont.render(
                    clockController.toString(), True, styleConf.timer_color)
        if pygame.mouse.get_pressed()[0]:
            if back_btn.click(pygame.mouse.get_pos()):
                if msgbox.askyesno('确认操作', '保存并退出？'):
                    store.write()
                    print(store.path)
                    store.default()
                    gameConf.default()
                    windowConf.default()
                    styleConf.default()

                    break
        window.fill('white', ((windowConf.grid+3)*windowConf.grid_size, windowConf.grid_size +
                    15, (windowConf.grid+5)*windowConf.grid_size, windowConf.grid_size*2))
        window.blit(timeText, ((windowConf.grid+3) *
                    windowConf.grid_size, windowConf.grid_size+15))
        pygame.display.update()
    pygame.quit()
