#!/usr/bin/python3
"""A module of class base"""


import json
import turtle  # Import the turtle module for drawing

class Base:
    __nb_objects = 0  # Class variable to keep track of the number of objects created

    def __init__(self, id=None):
        """
        Constructor for the Base class.

        Args:
            id (int): Optional ID for the object. If not provided, a new ID is generated.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Convert a list of dictionaries to a JSON-formatted string.

        Args:
            list_dictionaries (list): List of dictionaries to be converted.

        Returns:
            str: JSON-formatted string representing the list of dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Save a list of objects to a JSON file.

        Args:
            list_objs (list): List of objects to be saved.
        """
        filename = cls.__name__ + ".json"
        obj_list = []

        if list_objs is not None:
            for obj in list_objs:
                obj_list.append(obj.to_dictionary())

        with open(filename, 'w') as file:
            file.write(cls.to_json_string(obj_list))

    @staticmethod
    def from_json_string(json_string):
        """
        Convert a JSON-formatted string to a list of dictionaries.

        Args:
            json_string (str): JSON-formatted string.

        Returns:
            list: List of dictionaries.
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Create an object from a dictionary.

        Args:
            **dictionary: Keyword arguments representing the attributes of the object.

        Returns:
            obj: Instance of the class with attributes set based on the provided dictionary.
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)  # Create a dummy instance
        elif cls.__name__ == "Square":
            dummy = cls(1)  # Create a dummy instance
        dummy.update(**dictionary)  # Update the dummy instance with real values
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Load objects from a JSON file.

        Returns:
            list: List of objects loaded from the file.
        """
        filename = cls.__name__ + ".json"
        obj_list = []

        try:
            with open(filename, 'r') as file:
                content = file.read()
                obj_dicts = cls.from_json_string(content)
                for obj_dict in obj_dicts:
                    obj_list.append(cls.create(**obj_dict))
        except FileNotFoundError:
            pass

        return obj_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Save a list of objects to a CSV file.

        Args:
            list_objs (list): List of objects to be saved.
        """
        filename = cls.__name__ + ".csv"

        with open(filename, 'w') as file:
            if list_objs is not None:
                for obj in list_objs:
                    if cls.__name__ == "Rectangle":
                        file.write("{},{},{},{},{}\n".format(obj.id, obj.width, obj.height, obj.x, obj.y))
                    elif cls.__name__ == "Square":
                        file.write("{},{},{},{}\n".format(obj.id, obj.size, obj.x, obj.y))

    @classmethod
    def load_from_file_csv(cls):
        """
        Load objects from a CSV file.

        Returns:
            list: List of objects loaded from the file.
        """
        filename = cls.__name__ + ".csv"
        obj_list = []

        try:
            with open(filename, 'r') as file:
                for line in file:
                    values = line.strip().split(',')
                    if cls.__name__ == "Rectangle":
                        obj = cls(int(values[1]), int(values[2]), int(values[3]), int(values[4]), int(values[0]))
                    elif cls.__name__ == "Square":
                        obj = cls(int(values[1]), int(values[2]), int(values[3]), int(values[0]))
                    obj_list.append(obj)
        except FileNotFoundError:
            pass

        return obj_list

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Draw rectangles and squares using the turtle module.

        Args:
            list_rectangles (list): List of Rectangle objects to be drawn.
            list_squares (list): List of Square objects to be drawn.
        """
        screen = turtle.Screen()
        screen.bgcolor("white")
        pen = turtle.Turtle()
        pen.speed(2)

        for rect in list_rectangles:
            pen.penup()
            pen.goto(rect.x, rect.y)
            pen.pendown()
            for _ in range(2):
                pen.forward(rect.width)
                pen.left(90)
                pen.forward(rect.height)
                pen.left(90)

        for square in list_squares:
            pen.penup()
            pen.goto(square.x, square.y)
            pen.pendown()
            for _ in range(4):
                pen.forward(square.size)
                pen.left(90)

        turtle.done()

if __name__ == "__main__":
    pass
