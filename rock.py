'''Rock: adds the ability to evolve (update) like a rock to the Polygon class.
Data Members:
    _spin_rate: The rate that the rock spins.  Measured in degrees per second(positive or negative)
Rock Methods
    __init__use contructor chaining to initialize the Polygon data members
        set the object's polygon to the shape of a random rock
        Not moving, Rotation randomly selected from 0.0 to 359.9, spin rate for the rock to a random floating point
        range -90 degrees per second to +90 degrees per second.
        accelerated a random amount from 10 to 20 pixels per second.
    createRandomPolygon:
        creates a list of 2-tuples with the coordinates of the outline of a random rock shape.returns the point list.
        The angles of the points must be equally spread around a circle
            For example, if there are 5 points, then the points will be 360 / 5 = 72 degrees apart
            Each point's distance from the origin is randomly chosen to be between 70% and 130% of the radius.
    evolve causes the rock to move and spin.
'''

import math
from random import randrange
from polygon import Polygon

class Rock(Polygon):
    
    def __init__(self, x, y, world_width, world_height):
        super().__init__(x, y, 0,0, randrange(0,360), world_width, world_height)
        
        self._spin_rate = randrange(-90,90)
        
        self.accelerate(randrange(10,20))
        self.set_polygon(self.createRandomPolygon(randrange(20,50), randrange(10,15)))
        
        #velocity = math.sqrt( (self.getDX()**2) + (self.get_dy()**2))
        
        return
    
    def createRandomPolygon(self, r, number_of_points):
        polygon_points = []
        degrees = 360 / number_of_points
        theta = 0
        
        while theta < 360:
        
            r2 = randrange((r*60),(r*120)) / 100
            x = r2*math.cos(math.radians(theta))
            y = r2*math.sin(math.radians(theta))
            polygon_points.append((x,y))
            theta+=degrees

        return polygon_points
    
    def getSpinRate(self):
        return self._spin_rate
    
    def setSpinRate(self, spin_rate):
        self._spin_rate = spin_rate
    
    def evolve(self, dt):
        self.rotate(self.getSpinRate()*dt)
        self.move(dt)
        return