#!/usr/bin/python3
import unittest
import os
from models import storage
from models.base_model import BaseModel


class FileStorageTestCase(unittest.TestCase):
    def setUp(self):
        """clearing the content of the __objects first"""
        del_list = []
        for key in storage._FileStorage__objects.keys():
            del_list.append(key)
        for key in del_list:
            del storage._FileStorage__objects[key]

    def tearDown(self):
        """deleting the file to ensure a clean slate"""
        if os.path.exists('file.json'):
            os.remove('file.json')

    def test_obj_list_empty(self):
        """ensures that the __objects is empty at the start"""
        self.assertEqual(len(storage.all()), 0)

    def test_new_method(self):
        """checks that the new instance is added to the __objects"""
        base_model = BaseModel()
        for obj in storage._FileStorage__objects.values():
            self.assertEqual(obj, base_model)

    def test_save_method(self):
        """tests that it saves in a `file.json`"""
        base_model = BaseModel()
        base_model.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_reload_method(self):
        """tests that the instance is reinitialised"""
        storage.reload()
        for obj in storage._FileStorage__objects.values():
            self.assertEqual(obj, base_model)


if __name__ == '__main__':
    unittest.main()
