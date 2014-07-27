import socket
import utils
import json
import pygame

def relay(data):
    sock = utils.sock
    sock.sendto(json.dumps(data), utils.data)


def recv():
    sock = utils.sock
    sock.connect(utils.data)
    while True:
        data = sock.recv(1024)
        if data:
            data = data.split("\n")[0]
            data = json.loads(data)
            print data
            if data['type'] == "player":
                utils.players[data['id']] = data
            elif data['type'] == "bullet":
                utils.bullets[data['id']] = data
            elif data['type'] == "enemy":
                utils.enemies.append([pygame.Rect(data['x'], data['y'], 16, 16), data['health']])
