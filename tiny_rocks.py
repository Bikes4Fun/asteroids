#possible extension to allow rocks to 'explode' when they've been hit.



def collide_rocks_and_bullets(self):
    for rock in self.mRocks:
        for bullet in self.mBullets:
            if rock.hits(bullet):
                self.makeTinyRocks(rock)    
                rock.set_active(False)
                bullet.set_active(False)


def makeTinyRocks(self,rock):
    '''rock is a rock object that has been hit by bullet and passed to tinyrock to 'explode' '''
    point_list = rock.get_polygon() #list of the rocks tuple coordinates 
    tiny_rocks = [] #empty list to become a new list coordinates representing 'tiny rocks', made from each point in the has-been-hit rock.
    r = rock.get_radius()
    for new_rock in point_list:
        x,y = new_rock
        rock.Rock()
        rock.createRandomPolygon(r*.5,(randrange(20,30)))
    for set_rock in tiny_rocks:
        (x, y, dx, dy, rotation, world_width, world_height)
        rock.set_polygon(set_rock)
        
                
    
'''make rocks'''
for i in range(8):
    x = randrange(0,world_width)
    y = randrange(0,world_height)
    rock = Rock(x,y,world_width,world_height)
    self.mRocks.append(rock)
