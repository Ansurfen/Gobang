import sys
import os
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from mvc.constants import *
from mvc.controller import *


def to(any, cur, dst):
    any.pages[dst].pack()
    any.pages[cur].pack_forget()


def HomePage(any):
    home_page = ttk.Frame(any.app)
    ttk.Button(home_page, text='离线游戏', command=lambda: to(
        any, HOME_PAGE, OFFLINE_PAGE)).pack()
    ttk.Button(home_page, text='在线游戏', command=lambda: to(
        any, HOME_PAGE, ONLINE_PAGE)).pack()
    home_page.pack(side=TOP)
    return home_page


def OfflinePage(any):
    files = os.listdir('./map/')
    offline_page = ttk.Frame(any.app)
    for f in files:
        ttk.Button(offline_page, text=f[:len(f)-4],
                   command=lambda arg=(any, f, True): start(arg[0], arg[1], arg[2])).pack(fill=BOTH)
    ttk.Button(offline_page, text='新游戏', command=lambda: to(
        any, OFFLINE_PAGE, SELECT_PAGE)).pack(side=LEFT)
    ttk.Button(offline_page, text='返还', command=lambda: to(
        any, OFFLINE_PAGE, HOME_PAGE)).pack(side=LEFT)
    return offline_page


def OnlinePage(any):
    online_page = ttk.Frame(any.app)
    ttk.Label(online_page, text="IP地址", width=8).pack()
    ttk.Entry(online_page, textvariable=any.ip).pack()
    ttk.Label(online_page, text="端口号", width=8).pack()
    ttk.Entry(online_page, textvariable=any.port).pack()
    ttk.Button(online_page, text='开始游戏', command=lambda arg=(
        any, '', False): start(arg[0], arg[1], arg[2])).pack()
    ttk.Button(online_page, text='返还', command=lambda: to(
        any, ONLINE_PAGE, HOME_PAGE)).pack()
    return online_page


def SelectPage(any):
    select_page = ttk.Frame(any.app)
    ttk.Label(select_page, text="格数", width=8).pack()
    ttk.Entry(select_page, textvariable=any.grid).pack()
    ttk.Label(select_page, text="目标", width=8).pack()
    ttk.Entry(select_page, textvariable=any.goals).pack()
    ttk.Checkbutton(select_page, bootstyle="success-round-toggle",
                    variable=any.mutilplayer, text='多人游戏').pack()
    ttk.Button(select_page, text='开始游戏', command=lambda arg=(
        any, '', False): start(arg[0], arg[1], arg[2])).pack()
    ttk.Button(select_page, text='返还', command=lambda: to(
        any, SELECT_PAGE, HOME_PAGE)).pack()
    return select_page
