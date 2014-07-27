import pygame
from pygame.locals import *
import relay
import thread
import Player
import Enemy
import sys
import utils
import Bullets

def run():
    screen = utils.screen
    player = Player.Player()
    enemy = Enemy.Enemy()
    bullet = Bullets.Bullets()
    pygame.display.set_caption("Zombie Survival Online")
    font = pygame.font.init()
    font = pygame.font.Font("font.otf", 25)
    thread.start_new_thread(relay.recv, ())
    clock = pygame.time.Clock()
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == K_SPACE:
                player.shoot()
            elif event.type == pygame.QUIT:
                sys.exit()
        screen.fill((255,255,255))
        
        player.update()
        enemy.update()
        bullet.update()
        if utils.health > 0:
            key = pygame.key.get_pressed()
            if key[K_a] or key[K_LEFT]:
                player.move(-10, 0)
            if key[K_w] or key[K_UP]:
                player.move(0, -10)
            if key[K_s] or key[K_DOWN]:
                player.move(0, 10)
            if key[K_d] or key[K_RIGHT]:
                player.move(10, 0)
            screen.blit(font.render("Health: "+str(utils.health), -1, (0, 0, 0)), (50, 25))
        else:
            screen.blit(font.render("Dead!", -1, (0,0,0)), (50, 25))
        screen.blit(font.render("Combinded Kills: "+str(utils.kills), -1, (0,0,0)), (50, 50))
        for player_ in utils.players:
            pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(utils.players[player_]['x'], utils.players[player_]['y'], 16, 16))

        pygame.display.update()

if __name__ == "__main__":
    run()
