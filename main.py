import pygame
import game
import asteroids
from ship import Ship

class PygameApp(game.Game):

    def __init__(self, width, height, frame_rate):
        game.Game.__init__(self, "Asteroids", width, height, frame_rate)
        self._game = asteroids.Asteroids(width, height)
        return

    def game_logic(self, keys, newkeys, buttons, newbuttons, mouse_position, dt):
        x = mouse_position[ 0 ]
        y = mouse_position[ 1 ]

        if pygame.K_a in keys or pygame.K_LEFT in keys:
            self._game.turn_ship_left(5.0)

        if pygame.K_d in keys or pygame.K_RIGHT in keys:
            self._game.turn_ship_right(5.0)

        if pygame.K_w in keys or pygame.K_UP in keys:
            self._game.accelerate_ship(2.0)
            
        if pygame.K_s in keys or pygame.K_DOWN in keys:
            self._game.accelerate_ship(-2.0)
        if pygame.K_SPACE in newkeys:
            self._game.fire()

        if 1 in newbuttons:
            print("button clicked")

        self._game.evolve(dt)
        return

    def paint(self, surface):
        self._game.draw(surface)
        return

def main():
    pygame.font.init()
    game = PygameApp(1400, 700, 30)
    game.main_loop()

if __name__ == "__main__":
    main()
