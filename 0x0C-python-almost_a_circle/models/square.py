#!/usr/bin/python3
"""Square Module"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize Square instance

        Args:
            size (int): size of the square
            x (int): x coordinate of the square
            y (int): y coordinate of the square
            id (int): id of the square
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size"""
        self.width = value
        self.height = value

    def __str__(self):
        """Return the string representation of the square"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """Update the square attributes"""
        if args:
            attrs = ["id", "size", "x", "y"]
            for i, value in enumerate(args):
                setattr(self, attrs[i], value)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representation of the square"""
        return {'id': self.id, 'size': self.width,
                'x': self.x, 'y': self.y}
