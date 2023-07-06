from circle import Circle

'''
    bullets are initialized with an age of 0.
    they are immediately accelerated '100' and moved '.2' to avoid instant collision with the ship.
    'Circle' receieves the following parameters: (self, x, y, dx, dy, rotation, radius, world_width, world_height)
    evolve moves the bullet.  Adds dt to the age of the bullet.  If the bullet is more than 6 seconds old, makes it inactive.
'''

class Bullet(Circle):
    def __init__(self,x,y,dx,dy,rotation,world_width,world_height):
        super().__init__(x, y, dx, dy, rotation, 3, world_width, world_height)
        self._bullet_age = 0
        self.accelerate(100) 
        self.move(.2)

    def get_age(self):
        return self._bullet_age

    def set_age(self,age):
        self._bullet_age+=age
        return

    def evolve(self,dt):
        #a = (self.get_age()+dt)
        self.set_age(dt)
        if self.get_age() > 6:
            self.set_active(False)
        self.move(dt)
