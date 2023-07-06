import math
import movable
class Rotatable(movable.Movable):
    
    def __init__(self, x, y, dx, dy, rotation, world_width, world_height):
        super().__init__(x, y, dx, dy, world_width, world_height)
        self._rotation = rotation
        return
    
    def get_rotation(self):
        return self._rotation
    
    def rotate(self, delta_rotation):
        updated_rotation = (self._rotation+delta_rotation)
        if not 0 <= updated_rotation < 360:
            updated_rotation = abs(updated_rotation)-360
        self._rotation = abs(updated_rotation) 
    
    def delta_v_to_xy(self, rotation, delta_v):
        '''Receives (rotation) in degrees, and (delta_velocity) in pixels per second.
            Returns a 2-tuple of the amount of velocity change in the horizontal and vertical directions.
            convert degrees to radians.
            calculate the cosine and sine values of angles.'''
        radians = math.radians(rotation)
        x = math.cos(radians)*delta_v
        y = math.sin(radians)*delta_v
        return (x,y)
    
    def accelerate(self, delta_v):
        x,y = self.delta_v_to_xy(self.get_rotation(), delta_v)
        if (self._dx+x) > 0:
            self._dx+=x
        if (self._dy+y) > 0:
            self._dy+=y 
    
    def rotate_point(self, x, y):
        '''receives x and y, the coordinates of an arbitrary point.
        returns new values for x and y as a 2-tuple.
        The new values are rotated about the origin based on the object’s current rotation.'''
        r = math.sqrt(x*x+y*y)
        theta = math.atan2(y,x)
        theta += math.radians(self._rotation)
        x2 = r*math.cos(theta)
        y2 = r*math.sin(theta)
        return (x2, y2)
    
    def translate_point(self, x, y):
        '''receives x and y, the coordinates of an arbitrary point.
        Returns new values for x and y as a 2-tuple.
        The new values are calculated by adding the object’s _x and _y values.'''
        x+=self._x
        y+=self._y
        return (x, y)
    
    def rotate_and_translate_point(self, x, y):
        '''receives x and y, the coordinates of an arbitrary point.
        It returns new values for x and y as a 2-tuple.
        The new values are calculated by first rotating the point
        then translating the rotated coordinates.'''
        x2,y2 = self.rotate_point(x,y)
        x3,y3 = self.translate_point(x2,y2)
        return (x3, y3)
    
    def list_rotated_translated_points(self, point_list):
        new_list = []
        for points in point_list:
            x,y = points
            new_list.append((self.rotate_and_translate_point(x, y)))
        return new_list


'''
Rotatable:
    adds the ability to rotate objects.
        implements the accelerate method, making it possible to change the motion of objects.

Rotatable Data Members:
    _rotation is the object's orientation, measured in degrees.
        0 degrees is to the right, 90 degrees is down, etc.
    Note that this is not the direction of travel.
        Direction of travel is controlled by _dx and _dy which are in Movable.

Rotatable Methods:
    __init__:
        Uses contructor chaining to initialize the Movable data members.
        Sets the object's rotation, assuming the input values are all valid.
        
    rotate:(passes)
        Receives (delta_rotation) which may be positive or negative,
        
        Rotation is at least 0 and less than 360.
                -10 degrees should be updated to 350.
                -375 degrees should be updated to 15 degrees.
        return??
    
    delta_v_to_xy:
        Receives (rotation) in degrees, and (delta_velocity) in pixels per second.
        Returns a 2-tuple of the amount of velocity change in the horizontal and vertical directions.
            convert degrees to radians.
            calculate the cosine and sine values of angles.
'''
