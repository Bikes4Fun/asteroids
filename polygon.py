import pygame
from math import sqrt

import rotatable
class Polygon(rotatable.Rotatable):
    
    def __init__(self, x, y, dx, dy, rotation, world_width, world_height):
        super().__init__(x, y, dx, dy, rotation, world_width, world_height)
        
        self._original_polygon = []
        self._color = (255, 255, 255)
        return
    
    def get_polygon(self):
        return self._original_polygon
    
    def get_color(self):
        return self._color
    
    def get_radius(self):
        if len(self.get_polygon()) == 0:
            return 0
        total_distance = 0.
        for points in self.get_polygon():
            x2,y2 = points
            d = sqrt(((0-x2)**2)+((0-y2)**2))
            total_distance += d
        radius = (total_distance / len(self.get_polygon()))
        return radius
    
    def set_polygon(self, point_list):
        self._original_polygon = point_list
    
    def set_color(self, color):
        self._color = color
    
    def draw(self, surface):
        '''polygon(surface, color, points, width) '''
        point_list = self._original_polygon[::]
        point_list = self.list_rotated_translated_points(point_list)
        pygame.draw.polygon(surface, self.get_color(), point_list, 1)