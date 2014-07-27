import utils
import pygame
import relay
import uuid

class Player:
    def update(self):
       self.animate() 
    
    def move(self, x, y):
    
        utils.player.x += x
        utils.player.y += y
        if x > 0:
            utils.direction = "right"
        elif x < 0:
            utils.direction = "left"
        elif y > 0:
            utils.direction = "down"
        elif y < 0:
            utils.direction = "up"

        if utils.player.x <= 0:
            utils.player.x -= x
        elif utils.player.x >= 800 - 32:
            utils.player.x -= x
        elif utils.player.y <= 0:
            utils.player.y -= y
        elif utils.player.y >= 600 - 32:
            utils.player.y -= y

        relay.relay({"type":"player", "x":utils.player.x, "y":utils.player.y, "id":utils.id_, "health":utils.health})
    
    def shoot(self):
    
        relay.relay({"type":"bullet", "x":utils.player.x, "y":utils.player.y, "direction":utils.direction, "id":uuid.uuid4().hex})

    def animate(self):
        pygame.draw.rect(utils.screen, (0,0,255), utils.player)
