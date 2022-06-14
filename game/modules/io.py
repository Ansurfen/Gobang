import time
import random


def getFileName():
    now = time.localtime()
    head = time.strftime("%Y%m%d", now)
    seed = time.strftime("%H%M%S", now)
    random.seed(seed)
    body = ''
    base = 'abcdefghigklmnopqrstuvwxyzABCDEFGHIGKLMNOPQRSTUVWXYZ0123456789'
    for i in range(0, 12):
        body += base[random.randint(0, len(base) - 1)]
    return head+body


def writeFile(filename, data):
    fp = open(filename, 'w')
    fp.write(data)
    fp.close()


def readFile(filename):
    return open(filename, 'r')
