import pygame
import socket
import uuid

id_ = uuid.uuid4().hex
screen = pygame.display.set_mode((800, 600))
players = {}
player = pygame.Rect(800 / 2, 600 / 2, 16, 16)
enemies = []
bullets = {}
direction = "right"
data = ("100.1.73.128", 5555)
max_enemies = 10
health = 100
kills = 0
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
