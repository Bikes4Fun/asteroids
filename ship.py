'''Ship: adds the ability to evolve (update) like a ship to the Polygon class.
Data Members:
    None
Ship Methods:
    __init__ uses contructor chaining to initialize the Polygon data members
        sets the object's polygon to the shape of the ship.
        The ship should not be moving and should have a rotation of 0.
    
    evolve causes the ship to move.
'''

from polygon import Polygon
from bullet import Bullet

class Ship(Polygon):
    
    def __init__(self, x, y, world_width, world_height):
        super().__init__(x, y, 0, 0, 0, world_width, world_height)
        shape = [(10,0),(-10,10),(-5,0),(-10,-10)]
        self.set_polygon(shape)
        return
    
    def fire(self):
        bX,bY = self.get_polygon()[0]
        cX,cY = self.rotate_and_translate_point(bX,bY)
        return Bullet(cX, cY, self.get_dx(), self.get_dy(), self.get_rotation(), self.get_world_width(), self.get_world_height())
        
    def evolve(self, dt):
        self.move(dt)
        return

