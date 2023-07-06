'''Movable: Handles objects that have a location and may be able to move.
Data Members:
    _x and _y: the object's coordinates.Window coordinates measured in pixels._x greater or EQUAL to 0 and less than _world_width._y greater or EQUAL to 0 and less than _world_height.
    _dX and _dY: the object's speed. horizontal and vertical directions. measured in pixels per second.
    _world_width and _world_height: Dimensions of the window measured in pixels.
    _active boolean value, whether the object is active or not.
Methods:
    move: updates values of _x and _y using speeds _dX and _dY and elapsed time, dt.if object moves off window,updates coordinates to appear on other side of window.
    hits: returns true if this object's "circular" area overlaps with that of the other object.  Use the circle collision technique discussed in class.
    accelerate, evolve, draw: abstract methods only raise 'not implemented' error.'''

from math import sqrt

class Movable:

    def __init__(self, x, y, dx, dy, world_width, world_height):
        if x>= 0 and x< world_width:
            self._x = x
        
        if y >= 0 and y < world_height:
            self._y = y
            
        self._dx = dx
        self._dy = dy
        self._world_width = world_width
        self._world_height = world_height
        self._active = True
        return
    
    def get_x(self):
        return self._x
    
    def get_y(self):
        return self._y
    
    def get_dx(self):
        return self._dx
    
    def get_dy(self):
        return self._dy
    
    def get_world_width(self):
        return self._world_width
    
    def get_world_height(self):
        return self._world_height
    
    def move(self, dt):
        x2 = self.get_x()+(self.get_dx()*dt)
        y2 = self.get_y()+(self.get_dy()*dt)
        
        if x2 < 0:
            x2+=self._world_width
        
        if x2 >= self._world_width:
            x2-=self._world_width
        
        if y2 < 0:
            y2+=self._world_height
        
        if y2 >= self._world_height:
            y2-=self._world_height
        
        self._x = x2
        self._y = y2
        return
    
    def get_active(self):
        return self._active
        
    def set_active(self, active):
        self._active = active
    
    def hits(self, other):
        '''if the distance between(my center + my radius) and (your center + your radius)is greater than 0, then our boundaries don't touch.'''
        x = (self.get_x()-other.get_x())**2
        y = (self.get_y()-other.get_y())**2
        distance = sqrt(x+y)
        if distance <= (self.get_radius() + other.get_radius()):
            return True
        return False
    
    def accelerate(self,dt):
        raise NotImplementedError

    def evolve(self, dt):
        raise NotImplementedError
    
    def draw(self, surface):
        raise NotImplementedError
    
    def get_radius(self):
        raise NotImplementedError
