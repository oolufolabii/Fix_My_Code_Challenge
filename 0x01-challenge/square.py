#!/usr/bin/python3
""" A python module for handling squares. """


class Square:
    """Class to represent the square"""

    def __init__(self, *args, **kwargs):
        """Init a new square"""
        self.width = 0
        self.height = 0

        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def PermiterOfMySquare(self):
        """Perimeter of the square"""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """String format/representation"""
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
