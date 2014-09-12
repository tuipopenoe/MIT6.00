#!python2
# Tui Popenoe
# ps9.py 

from string import *

class Shape(object):
    def area(self):
        raise AttributeException("Subclasses should override this method.")

class Square(Shape):
    def __init__(self, h):
        """
        h: length of side of the square
        """
        self.side = float(h)
    def area(self):
        """
        Returns area of the square
        """
        return self.side**2
    def __str__(self):
        return 'Square with side ' + str(self.side)
    def __eq__(self, other):
        """
        Two squares are equal if they have the same dimension.
        other: object to check for equality
        """
        return type(other) == Square and self.side == other.side

class Circle(Shape):
    def __init__(self, radius):
        """
        radius: radius of the circle
        """
        self.radius = float(radius)
    def area(self):
        """
        Returns approximate area of the circle
        """
        return 3.14159*(self.radius**2)
    def __str__(self):
        return 'Circle with radius ' + str(self.radius)
    def __eq__(self, other):
        """
        Two circles are equal if they have the same radius.
        other: object to check for equality
        """
        return type(other) == Circle and self.radius == other.radius

class Triangle(Shape):
    def __init__(self, base, height):
        """
        base: base of the triangle
        height: height of the triangle
        """
        self.base = float(base)
        self.height = float(height)
    def area(self):
        return (0.5 * self.base * self.height)
    def __str__(self):
        return 'Triangle with base' + str(self.base) + 'and height' +
            str(self.height)
    def __eq__(self, other):
        """
        Two triangles are equal if they have the same radius.
        other: object to check for equality
        """
        return type(other) == Triangle and self.base == other.base
            and self.height == other.height

class ShapeSet:
    def __init__(self):
        """
        Initialize any needed variables
        """
        self.set = []
    def addShape(self, sh):
        """
        Add shape sh to the set; no two shapes in the set may be
        identical
        sh: shape to be added
        """
        for i in self.set:
            if sh.__eq__(i):
                return
        self.set.append(sh)
    def __iter__(self):
        """
        Return an iterator that allows you to iterate over the set of
        shapes, one shape at a time
        """
        return iter(self.set)
    def __str__(self):
        """
        Return the string representation for a set, which consists of
        the string representation of each shape, categorized by type
        (circles, then squares, then triangles)
        """
        for i in self.set:
            print(i.__str__())

def findLargest(shapes):
    """
    Returns a tuple containing the elements of ShapeSet with the
       largest area.
    shapes: ShapeSet
    """
    largest_area = 0
    largest_shapes = []
    for i in shapes:
        if i.area() > largest_area:
            largest_area = i.area()
            largest_shapes = [i]
        if i.area() == largest_area:
            largest_shapes.append(i)
    return largest_shapes

def readShapesFromFile(filename):
    """
    Retrieves shape information from the given file.
    Creates and returns a ShapeSet with the shapes found.
    filename: string
    """
    output = ShapeSet()
    with open(filename, 'r') as f:
        shapes = f.readlines().split(',')
        for i in range(0, len(shapes), 2):
            if shapes[i] == 'circle':
                output.addShape(Circle(shapes[i+1]))
            if shapes[i] == 'square':
                output.addShape(Square(shapes[i+1]))
            if shapes[i] == 'triangle':
                output.addShape(Triangle(shapes[i+1]))
    return output
