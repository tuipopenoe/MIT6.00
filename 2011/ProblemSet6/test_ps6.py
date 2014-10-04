#!python2
# Tui Popenoe
# test_ps6.py

import random
from ps6 import *

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
    """Test the is tile cleaned method in the rectangular room class."""
    random_x = random.randint(50, 100)
    random_y = random.randint(50, 100)
    room = RectangularRoom(random_x, random_y)
    pos_x = random.randint(1, 50)
    pos_y = random.randint(1, 50)
    pos = Position(random_x, random_y)
    room.cleanTileAtPosition(random_x, random_y)
    self.assertEqual(not room.tiles[pos_x][pos_y])

def test_get_num_tiles():
    """Test the get num tiles method in the rectangular room class."""
    random_x = random.randint(50, 100)
    random_y = random.randint(50, 100)
    room = RectangularRoom(random_x, random_y)
    self.assertEqual(random_x * random_y, room.getNumTiles())

def test_get_num_cleaned_tiles():
    """Test the get num cleaned tiles method in the rectangular room class."""
    random_x = random.randint(50, 100)
    random_y = random.randint(50, 100)
    room = RectangularRoom(random_x, random_y)
    count = 0
    for i in range(random_x):
        for j in range(random_y):
            k = random.random()
            if k < 0.50:
                room.tiles[i][j] = True
                count += 1
    self.assertEqual(room.getNumCleanedTiles(), count)

def test_get_random_position():
    """Test the get random position method in the rectangular room class."""
    room = RectangularRoom(1, 1)
    pos = room.getRandomPosition()
    self.assertEqual(pos.getX(), 1)
    self.assertEqual(pos.getY(), 1)

def test_is_position_in_room():
    """Test the is position in room method in the rectangular room class."""
    random_x = random.randint(10, 20)
    random_y = random.randint(10, 20)
    room = RectangularRoom(random_x, random_y)
    out_pos = Position(random_x + 1, random_y + 1)
    in_pos = Position(random_x -1, random_y -1)
    self.assertFalse(room.isPositionInRoom(out_pos))
    self.assertTrue(room.isPositionInRoom(in_pos))

def test_get_robot_position():
    """Test the get robot position method in the robot class."""
    random_x = randint(10, 20)
    random_y = randint(10, 20)
    random_speed = randint(5, 10)
    room = RectangularRoom(random_x, random_y)
    robot = Robot(room, random_speed)
    self.assertEqual(robot.pos, robot.getRobotPosition())

def test_get_robot_direction():
    """Test the get robot direction method in the robot class."""
    random_x = randint(10, 20)
    random_y = randint(10, 20)
    random_speed = randint(5, 10)
    room = RectangularRoom(random_x, random_y)
    robot = Robot(room, random_speed)
    self.assertEqual(robot.dir, robot.getRobotDirection())

def test_set_robot_position():
    """Test the set robot position method in the robot class."""
    random_x = randint(10, 20)
    random_y = randint(10, 20)
    random_speed = randint(5, 10)
    room = RectangularRoom(random_x, random_y)
    robot = Robot(room, random_speed)
    pos = Position(5, 5)
    robot.setRobotPosition(pos)
    self.assertEqual(pos, robot.pos)

def test_set_robot_direction():
    """Test the set robot direction method in the robot class."""
    random_x = randint(10, 20)
    random_y = randint(10, 20)
    random_speed = randint(5, 10)
    room = RectangularRoom(random_x, random_y)
    robot = Robot(room, random_speed)
    new_dir = random.randint(0, 360)
    robot.setRobotDirection(new_dir)
    self.assertEqual(new_dir, robot.dir)

def test_update_position_and_clean():
    """Tests the update position and clean method in the standard robot class"""
    