#!/usr/bin/python3
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def test_instance_creation_with_id(self):
        b1 = Base(12)
        self.assertEqual(b1.id, 12)

    def test_instance_creation_without_id(self):
        b2 = Base()
        self.assertEqual(b2.id, 1)

    def test_instance_creation_with_multiple_instances(self):
        b3 = Base()
        b4 = Base()
        self.assertEqual(b3.id, 2)
        self.assertEqual(b4.id, 3)

    def test_to_json_string_empty_list(self):
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_non_empty_list(self):
        self.assertEqual(Base.to_json_string([{'id': 1}]), '[{"id": 1}]')

    def test_to_json_string_none(self):
        self.assertEqual(Base.to_json_string(None), '[]')

    def test_save_to_file(self):
        Base.save_to_file([Base(1), Base(2)])
        with open("Base.json", "r") as file:
            self.assertEqual(file.read(), '[{"id": 1}, {"id": 2}]')

    def test_save_to_file_empty_list(self):
        Base.save_to_file([])
        with open("Base.json", "r") as file:
            self.assertEqual(file.read(), '[]')

    def test_save_to_file_none(self):
        Base.save_to_file(None)
        with open("Base.json", "r") as file:
            self.assertEqual(file.read(), '[]')

    def test_from_json_string_empty_string(self):
        self.assertEqual(Base.from_json_string(""), [])

    def test_from_json_string_empty_list(self):
        self.assertEqual(Base.from_json_string("[]"), [])

    def test_from_json_string_non_empty_list(self):
        self.assertEqual(Base.from_json_string('[{"id": 1}]'), [{'id': 1}])

    def test_from_json_string_none(self):
        self.assertEqual(Base.from_json_string(None), [])

    def test_create_rectangle(self):
        r = Base.create(**{'id': 89})
        self.assertEqual(r.id, 89)

    def test_create_square(self):
        s = Base.create(**{'id': 89, 'size': 4})
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 4)

    def test_load_from_file(self):
        Base.save_to_file([Base(1), Base(2)])
        objs = Base.load_from_file()
        self.assertEqual(len(objs), 2)
        self.assertEqual(objs[0].id, 1)
        self.assertEqual(objs[1].id, 2)

    def test_load_from_file_empty_file(self):
        Base.save_to_file([])
        objs = Base.load_from_file()
        self.assertEqual(len(objs), 0)

    def test_load_from_file_nonexistent_file(self):
        objs = Base.load_from_file()
        self.assertEqual(len(objs), 0)


if __name__ == "__main__":
    unittest.main()
