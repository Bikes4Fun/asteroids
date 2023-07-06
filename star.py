'''Star Class
Star Data Members
    mBrightness an integer value.  The current star brightness, in the range 0 to 255.
Star Methods
    __init__ uses constructor chaining to initialize all Circle data members.  Stars have no speed, rotation of 0, and radius of 2.  Initializes the brightness to a random value.
    setBrightness updates the data member, but only if the new brightness is within the range specified above.  If the brightness changes, update the color as well.
    evolve Tries to changes the brightness by adding 10, subtracting 10, or doing nothing, each with equal probability.'''

from random import randrange, choice
from circle import Circle

class Star(Circle):

    def __init__(self,x,y,world_width,world_height):
        super().__init__(x, y, 0, 0, 0, 2, world_width, world_height)
        self.mBrightness = (10)
        
    def getBrightness(self):
        return self.mBrightness
    
    def setBrightness(self,brightness):
        if 15 <= brightness <= 240:
            r = brightness + (randrange(-10,10))
            g = brightness - 10
            b = brightness + 10
            self.mBrightness = (brightness)
            self.set_color((r,g,b))
    
    def evolve(self,dt):
        self.setBrightness(self.getBrightness()-(randrange(-10,10)))
        #self.setBrightness(randomchoice(-10,0,10))
        
