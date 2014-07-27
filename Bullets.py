import utils
import pygame

class Bullets:
    def update(self):
        remove = []
        for bullet in utils.bullets:
            check = self.animate(bullet)
            if check:
                remove.append(check)                                                                                                                                                                   

        for x in remove:
            del utils.bullets[x['id']]

    def animate(self, bullet):
        bullet = utils.bullets[bullet]
        if bullet['direction'] == "left":
            if bullet['x'] <= 0:
                return bullet
            else:
                bullet['x'] -= 25

        elif bullet['direction'] == "right":
            if bullet['x'] >= 800:
                return bullet
            else:
                bullet['x'] += 25


        elif bullet['direction'] == "down":
            if bullet['y'] >= 800:
                return bullet
            else:
                bullet['y'] += 25
        else:
            if bullet['y'] <= 0:
                return bullet
            else:
                bullet['y'] -= 25
        
        pygame.draw.rect(utils.screen, (0,0,0), pygame.Rect(bullet['x'], bullet['y'], 5, 5))
            
