#!python2
# Tui Popenoe
# test_ps9.py

from ps9 import *
from random impor randint

def test_shape_area():
    """Test the area method on the shape class."""
    shape = Shape()
    assertRaises(AttributeException, shape.area)

def test_init_square():
    """Test the init method on the square class."""
    x = randint(1, 10)
    square = Square(x)
    assertEqual(square.side, x)

def test_area_square():
    """Test the area method on the square class."""
    x = randint(1, 10)
    square = Square(x)
    assertEqual(x**2, square.area)

def test_str_square():
    """Test the __str__ method on the square class."""
    x = randint(1, 10)
    square = Square(x)
    assertEqual('Square with side %s' % str(x), ,square.__str__())

def test_eq_square():
    """Test the __eq__ method on the square class."""
    x = randint(1, 10)
    square1 = Square(x)
    square2 = Square(x)
    assert(square1 == square2)

def test_init_circle():
    """Test the init method on the circle class."""
    x = randint(1, 10)
    circle = Circle(x)
    assertEqual(circle.radius, x)

def test_area_circle():
    """Test the area method on the circle class."""
    x = randint(1, 10)
    circle = Circle(x)
    assertEqual(3.14159 * (x ** 2), circle.area())

def test_str_circle():
    """Test the __str__ method on the square class."""
    x = randint(1, 10)
    circle = Circle(x)
    assertEqual('Circle with radius %s' % x, circle.__str__())

def test_eq_circle():
    """Test the __eq__ method on the circle class."""
    x = randint(1, 10)
    circle1 = Circle(x)
    circle2 = Circle(x)
    assert(circle1 == circle2)

def test_init_triangle():
    """Test the init method on the triangle class."""
    x = randint(1, 10)
    y = randint(1, 10)
    triangle = Triangle(x, y)
    assertEqual(x, triangle.base)
    assertEqual(y, triangle.height)

def test_area_triangle():
    """Test the area method on the triangle class."""
    x = randint(1, 10)
    y = randint(1, 10)
    triangle = Triangle(x, y)
    assertEqual(0.5 * x * y, triangle.area())

def test_str_triangle():
    """Test the str method on the triangle class."""
    x = randint(1, 10)
    y = randint(1, 10)
    triangle = Triangle(x, y)
    assertEqual('Triangle with base %s and height %s' % (x, y),
        triangle.__str__())

def test_eq_triangle():
    """Test the eq method on the triangle class."""
    x = randint(1, 10)
    y = randint(1, 10)
    triangle1 = Triangle(x, y)
    triangle2 = Triangle(x, y)
    assert(triangle1 == triangle2)
