"""
This is a Python file to demonstrate PyDoc formatting.
To add comments to a class or method, place the comment directly underneath the class or method.
If you are adding comments to an actual Python file, add the comment at the very beginning. (like here)
The comments must be enclosed in triple quotes as seen here.


This is my suggested format:

Summary: Quick summary of the class/method. Ideally no longer than about 70 columns.
Attributes:
    (data type) [variables of that data type separated by commas]
    (data type) [variables of that data type separated by commas]
Parameters:
    (data type) [variables of that data type separated by commas]
        OR 
    self
Parameter Notes (if necessary):
    Place any special notes on the behavior of parameters here if necessary.
Returns:
    (data type) [variables of that data type separated by commas]
        OR
    None
Return Notes (if necessary):
    Place any special notes on the behavior of returned values here if necessary.
"""
from math import pi

class Circle:
    """
    Summary: The Circle class creates an object with various circle properties.
     Attributes:
        (number) x, y, radius, circumference
        (string) name
    Methods:
        (void) toString - prints out the object attributes
    """
    def __init__(self, x, y, radius, name):
        """
        Summary: Initializes a Circle. 
        Parameters:
            (number) x, y, radius
        Returns: 
            None
        """
        self.name
        self.x = x
        self.y = y
        self.radius = radius
        self.area = pi * (radius ** 2)
        self.circumference = 2 * pi * radius

    def toString(self):
        """
        Summary: Prints out Circle attributes to console. 
        Parameters:
            Self
        Returns: 
            None
        """
        print "Name: " + self.name
        print "Origin: (" + str(self.x) + ", " + str(self.y) + ")"
        print "Radius: " + str(self.radius)
        print "Area: " + str(self.circumference)