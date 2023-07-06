import pygame
from random import randrange
from ship import Ship
from rock import Rock
from star import Star
from bullet import Bullet

'''Asteroids: overall game class that creates and controls all objects.
Data Members:
    _world_width, _world_height the dimensions of the window, in pixels.
    _ship the Ship object created. _rocks a list of all Rock objects created. _objects a list of all objects created.
Methods:
    __init__ Sets the data members, including a Ship and 10 Rocks.
    get_ship, get_rocks and get_objects return the appropriate data members.
    -turn_ship_left reduces the ship’s rotation by delta_rotation.
    -turn_ship_right increases the ship’s rotation by delta_rotation.
    -accelerate_ship accelerates the ship by delta_velocity.
    -evolve evolves all objects by dt.
    -draw draws all objects.'''

class Asteroids():

    def __init__(self, world_width, world_height):
        self._world_width = world_width
        self._world_height = world_height
        self._ship = Ship(world_width / 2,world_height / 2,world_width,world_height)
        self._rocks = []  
        self._stars = []
        self._bullets = []
        
        '''make rocks'''
        for i in range(8):
            x = randrange(0,world_width)
            y = randrange(0,world_height)
            rock = Rock(x,y,world_width,world_height)
            self._rocks.append(rock)
        
        '''make stars'''
        for i in range(30):
            x = randrange(0,world_width)
            y = randrange(0,world_height)
            self._stars.append(Star(x,y,world_width,world_height))
        
        self._objects = [self._ship] + self._rocks + self._stars + self._bullets
        return

    def get_world_width(self):
        return self._world_width
    def get_world_height(self):
        return self._world_height
    def get_ship(self):
        return self._ship
    def get_rocks(self):
        return self._rocks
    def get_stars(self):
        return self._stars
    def get_bullets(self):
        return self._bullets
    def get_objects(self):
        return self._objects

    def turn_ship_left(self, delta_rotation):
        self._ship.rotate(-delta_rotation)
        #return delta_rotation

    def turn_ship_right(self, delta_rotation):
        self._ship.rotate(delta_rotation)
        #return delta_rotation

    def accelerate_ship(self, delta_velocity):
        self._ship.accelerate(delta_velocity)
         
    def fire(self):
        '''make bullets by calling fire inside ship. append bullet list and all objects list'''
        if len(self.get_bullets())<3:
            b = self._ship.fire()
            self._bullets.append(b)
            self._objects.append(b)

    def collide_ship_and_bullets(self):
        for bullet in self._bullets:
            if self._ship.hits(bullet):
                self._ship.set_active(False)
                bullet.set_active(False)

    def collide_ship_and_rocks(self):
        for rock in self._rocks:
            if self._ship.hits(rock):
                self._ship.set_active(False)
                rock.set_active(False)
        return

    def collide_rocks_and_bullets(self):
        for rock in self._rocks:
            for bullet in self._bullets:
                if rock.hits(bullet):
                    rock.set_active(False)
                    bullet.set_active(False)       
        return

    def remove_inactive_items(self):
        active_bullets = []
        active_rocks = []
        for b in self._bullets:
            if b.get_active():
                active_bullets.append(b)
        for r in self._rocks:
            if r.get_active():
                active_rocks.append(r)
        self._bullets = active_bullets
        self._rocks = active_rocks
        
        active_objects = []
        for o in self._objects:
            if o.get_active():
                active_objects.append(o)
        return


    def evolve(self, dt):
        '''Be sure that all objects evolve. If any bullet collides with the ship, the ship and bullet should become inactive. If any bullet collides with any rock, the rock and bullet should become inactive. If any rock collides with the ship, the ship and bullet should become inactive. Remove any inactive rocks and bullets from the lists. Use the methods outlined above, in the correct order.'''
        if self._ship.get_active() == False:
            self._ship.set_active(False)
            return
        self.evolve_all_objects(dt)
        self.collide_ship_and_bullets()
        self.collide_ship_and_rocks()
        self.collide_rocks_and_bullets()
        self.remove_inactive_items()
        return
        
    def evolve_all_objects(self,dt):
        for items in self.get_objects():
            items.evolve(dt)
        return
    
    def draw(self, surface):
        surface.fill((0,0,0))
        for items in self._objects:
            if items.get_active():
                items.draw(surface)
        return
