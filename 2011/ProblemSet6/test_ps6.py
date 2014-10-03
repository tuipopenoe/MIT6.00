#!python2
# Tui Popenoe
# test_ps6.py

import random
import ps6

def test_getX():
    """Test the get x method in the position class."""
    random_x = random.randint(0, 100)
    random_y = random.randint(0, 100)
    pos = ps6.Position(random_x, random_y)
    self.assertEqual(random_x, pos.getX())

def test_getY():
    """Test the get y method in the position class."""
    random_x = random.randint(0, 100)
    random_y = random.randint(0, 100)
    pos = ps6.Position(random_x, random_y)
    self.assertEqual(random_y, pos.getY())

def test_get_new_position():
    """Test the get new position method in the position class."""
    random_x = random.randint(0, 100)
    random_y = random.randint(0, 100)
    random_angle = random.randint(0, 360)
    random_speed = random.randint(0, 100)
    pos = ps6.Position(random_x, random_y)
    #TODO
    self.assertTrue(isinstance(pos, ps6.Position))

def test_clean_tile_at_position():
    """Test the clean tile at position method in the rectangular room class."""
    random_x = random.randint(50, 100)
    random_y = random.randint(50, 100)
    room = ps6.RectangularRoom(random_x, random_y)
    pos_x = random.randint(1, 50)
    pos_y = random.randint(1, 50)
    pos = Position(random_x, random_y)
    room.cleanTileAtPosition(pos)
    self.assertTrue(room.tiles[pos_x][pos_y])

def test_is_tile_cleaned():
    """Test the is tile cleaned method in the rectangular room."""
    random_x = random.randint(50, 100)
    random_y = random.randint(50, 100)
    room = ps6.RectangularRoom(random_x, random_y)
    pos_x = random.randint(1, 50)
    pos_y = random.randint(1, 50)
    pos = Position(random_x, random_y)
    room.cleanTileAtPosition(random_x, random_y)
    self.assertEqual(not room.tiles[pos_x][pos_y])