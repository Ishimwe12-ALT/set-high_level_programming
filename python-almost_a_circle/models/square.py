#!/usr/bin/python3
"""Defines the Square class inheriting from Rectangle."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent a Square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize Square instance."""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get/set size of Square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """Return string representation [Square] (<id>) <x>/<y> - <size>."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    def update(self, *args, **kwargs):
        """Assign positional/keyword arguments to Square attributes."""
        attrs = ["id", "size", "x", "y"]
        if args and len(args) > 0:
            for i, arg in enumerate(args):
                if i < len(attrs):
                    setattr(self, attrs[i], arg)
        elif kwargs:
            for key, value in kwargs.items():
                if key in attrs:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Return dictionary representation of Square."""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
