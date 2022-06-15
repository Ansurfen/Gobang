import socket


class styleConfig:
    def __init__(self):
        self.default()

    def default(self):
        self.window_bg_color = 'white'
        self.chessboard_bg_color = (238, 154, 73)
        self.timer_color = (0, 128, 0)


class windowConfig:
    def __init__(self):
        self.default()

    def default(self):
        self.grid = 15
        self.grid_size = 30


class gameConfig:
    def __init__(self):
        self.default()

    def default(self):
        self.survive = True
        self.online = True
        self.multiplayer = True
        self.reload = False
        self.count = 0
        self.goals = 4
        self.socket = None
        self.ip = ''
        self.port = -1

    def isWin(self, play, pos):
        direction = [[-1, -1], [-1, 0], [0, 1], [1, 1]]
        for i in range(4):
            x, y = direction[i][0], direction[i][1]
            cnt = 0
            for j in range(len(play)):
                for k in range(1, self.goals+1):
                    if (pos[0] + x * 30 * k, pos[1] + y * 30 * k) == play[j]:
                        cnt += 1
                    if (pos[0] - x * 30 * k, pos[1] - y * 30 * k) == play[j]:
                        cnt += 1
                    if cnt == self.goals:
                        self.count = 0.5

    def connect(self):
        if self.socket == None and self.ip != '' and self.port != -1:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect((self.ip, self.port))
            self.socket.setblocking(True)


styleConf = styleConfig()
windowConf = windowConfig()
gameConf = gameConfig()
