import utils
import relay
import random
import pygame
import math

class Enemy:
    def update(self):
        if len(utils.enemies) < utils.max_enemies:
            top_bottom = random.randint(0, 1)
            left_right = random.randint(0, 1)
            sides_top = random.randint(0, 1)
            if sides_top == 1 and top_bottom == 1: # Bottom
                enemy = {"x":random.randint(0, 800), "y":800, "health":100}
            elif sides_top == 1 and top_bottom == 0: # Top
                enemy = {"x":random.randint(0, 800), "y":0, "health":100}

            elif sides_top == 0 and top_bottom == 1: # Left
                enemy = {"x":random.randint(0, 800), "y":0, "health":100}

            else:
                enemy = {"x":random.randint(0, 800), "y":800, "health":100}
            enemy['type'] = "enemy" 
            relay.relay(enemy)

        for index,  enemy in enumerate(utils.enemies):
            try:
                self.collide(index)
            except:
                pass
            self.animate(index)



    def collide(self, index):
        enemy = utils.enemies[index]
        remove = []
        for bullet in utils.bullets:
            bul = bullet
            b = utils.bullets[bullet]
            bullet = pygame.Rect(b['x'], b['y'], 5, 5)
            if bullet.colliderect(enemy[0]):
                enemy[1] -= 50
                if enemy[1] <= 0:
                    utils.enemies.pop(index)
                    utils.kills += 1
                    utils.max_enemies += 1
                remove.append(bul)

        for bullet in remove:
            utils.bullets.pop(bullet)


        for player in utils.players:
            player = utils.players[player]
            player_ = pygame.Rect(player['x'], player['y'], 16, 16)
            if enemy[0].colliderect(player_):
                utils.enemies.pop(index)
                utils.kills += 1
                utils.max_enemies += 1
                player['health'] -= 10
                if player['id'] == utils.id_:
                    utils.health -= 10
                

    def animate(self, index):
        try:
            enemy = utils.enemies[index][0]
        except:
            return
        x = enemy.x
        y = enemy.y
        closest =  self.closest(x, y)
        if closest:
            if closest['x'] > x:
                enemy.x += 2
            else:
                enemy.x -= 2

            if closest['y'] > y:
                enemy.y += 2
            else:
                enemy.y -= 2
        pygame.draw.rect(utils.screen, (255, 0,0), enemy)
    def closest(self, x, y):
        closest = 100000
        goTo = None
        for player in utils.players:
            distance = math.sqrt((utils.players[player]['x'] - x)**2 + (utils.players[player]['y'] - y)**2)
            if distance < closest and utils.players[player]['health'] > 0:
                closest = distance
                goTo = utils.players[player]

        return goTo


        
    
