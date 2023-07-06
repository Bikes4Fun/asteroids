'''Circle Data Members
    _radius is a number measured in pixels.  The radius of the circle.
    _color is a PyGame color, a 3-tuple of integers in the range 0-255 describing the red, green and blue channels of the color.

Circle Methods
    __init__ uses constructor chaining to initialize the Rotatable data members, and sets the object's radius from the paramater, and sets the color to white.
    set_radius updates the data member, but only if the new value is at least 1.
    set_color updates the data member.  It assumes the new color is valid.
    draw Uses the PyGame functions to draw the circle described by the Movable position and the radius.'''

import pygame
import rotatable

class Circle(rotatable.Rotatable):
    
    def __init__(self, x, y, dx, dy, rotation, radius, world_width, world_height):
        super().__init__(x, y, dx, dy, rotation, world_width, world_height)
        self._radius = radius
        self._color = (255, 255, 255)
        return
    
    def get_radius(self):
        return self._radius
        
    def get_color(self):
        return self._color
    
    def set_radius(self, r):
        if r >= 1:
            self._radius = r
    
    def set_color(self, color):
        self._color = color
    
    def draw(self, surface):
        '''pygame.draw.circle(surface, color, center, radius)'''
        pygame.draw.circle(surface, self.get_color(), (self.get_x(), self.get_y()), self.get_radius())
