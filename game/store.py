from game.modules.io import *
from game.config import gameConf, windowConf, styleConf


class storeInterface:
    def __init__(self):
        self.default()

    def default(self):
        self.position = []
        self.play1 = []
        self.play2 = []
        self.mapping = {}
        self.path = ''
        for i in range(0, windowConf.grid):
            for j in range(0, windowConf.grid+1):
                self.position.append(
                    (20+i*windowConf.grid_size, windowConf.grid_size*j+20))

    def load_map(self):
        self.mapping = readFile(self.path)

    def write(self):
        line = 'play1:\n'
        for t in self.play1:
            line += ' '.join(str(x) for x in t)
            line += '\n'
        line += 'play2:\n'
        for t in self.play2:
            line += ' '.join(str(x) for x in t)
            line += '\n'
        if self.path == '':
            self.path = "./map/"+getFileName()+".txt"
        elif '.txt' not in self.path:
            self.path += '.txt'
        writeFile(self.path, line)

    def read(self):
        fp = readFile(self.path)
        line = fp.readline()
        name = ""
        while line:
            if ':' in line:
                name = line.strip().split(':')[0]
                self.mapping[name] = []
                line = fp.readline()
                continue
            tuples = line.strip().split(' ')
            if len(tuples) != 1:
                self.mapping[name].append((int(tuples[0]), int(tuples[1])))
            line = fp.readline()
        fp.close()


store = storeInterface()
