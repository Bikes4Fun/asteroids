'''Bullet Class
Bullet Data Members: _bullet_age the number of seconds the bullet has been in existence.

Bullet Methods: __init__ uses constructor chaining to initialize all Circle data members.
    Bullets all have a radius of 3.
    Initializes the age of the bullet to 0.
    Accelerates the bullet 100.0 units.
    Moves the bullet 0.1 seconds worth of movement.
    Without this, it will hit the ship.
    set_age updates the data member, assuming the parameter is correct.
    evolve moves the bullet.  Adds dt to the age of the bullet.  If the bullet is more than 6 seconds old, makes it inactive.
'''

from circle import Circle

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

    def evolve(self,dt):
        #a = (self.get_age()+dt)
        self.set_age(dt)
        if self.get_age() > 6:
            self.set_active(False)
        self.move(dt)
