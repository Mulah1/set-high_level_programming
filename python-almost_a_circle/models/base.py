#!/usr/bin/python3
"""Defines the Base model class."""
import json
import csv


class Base:
    """Base model for managing id attributes across all classes."""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file."""
        filename = cls.__name__ + ".json"
        list_dicts = []
        if list_objs is not None:
            list_dicts = [obj.to_dictionary() for obj in list_objs]
        with open(filename, "w") as f:
            f.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Return the list of the JSON string representation json_string."""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes already set."""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = cls()
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Return a list of instances from a JSON file."""
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as f:
                json_string = f.read()
        except IOError:
            return []
        list_dicts = cls.from_json_string(json_string)
        return [cls.create(**d) for d in list_dicts]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serialize instances to a CSV file."""
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            if list_objs is not None:
                for obj in list_objs:
                    if cls.__name__ == "Rectangle":
                        writer.writerow([obj.id, obj.width, obj.height,
                                         obj.x, obj.y])
                    elif cls.__name__ == "Square":
                        writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """Deserialize instances from a CSV file."""
        filename = cls.__name__ + ".csv"
        list_objs = []
        try:
            with open(filename, "r", newline="") as f:
                reader = csv.reader(f)
                for row in reader:
                    if cls.__name__ == "Rectangle":
                        d = {
                            "id": int(row[0]),
                            "width": int(row[1]),
                            "height": int(row[2]),
                            "x": int(row[3]),
                            "y": int(row[4])
                        }
                    elif cls.__name__ == "Square":
                        d = {
                            "id": int(row[0]),
                            "size": int(row[1]),
                            "x": int(row[2]),
                            "y": int(row[3])
                        }
                    list_objs.append(cls.create(**d))
        except IOError:
            pass
        return list_objs
