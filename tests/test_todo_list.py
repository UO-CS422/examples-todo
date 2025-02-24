import unittest
from ..src.todo.todo_list import ToDoList

class TestToDoList(unittest.TestCase):

    def setUp(self):
        self.todo_list = ToDoList()

    def test_add_task(self):
        index = self.todo_list.add_task("Task 1")
        self.assertEqual(index, 0)
        self.assertEqual(self.todo_list.get_task(index), "Task 1")

    def test_add_task_invalid(self):
        with self.assertRaises(ValueError):
            self.todo_list.add_task("")

    def test_get_task(self):
        self.todo_list.add_task("Task 1")
        task = self.todo_list.get_task(0)
        self.assertEqual(task, "Task 1")

    def test_get_task_invalid_index(self):
        with self.assertRaises(IndexError):
            self.todo_list.get_task(0)

    def test_remove_task(self):
        self.todo_list.add_task("Task 1")
        task = self.todo_list.remove_task(0)
        self.assertEqual(task, "Task 1")
        with self.assertRaises(IndexError):
            self.todo_list.get_task(0)

    def test_remove_task_invalid_index(self):
        with self.assertRaises(IndexError):
            self.todo_list.remove_task(0)

if __name__ == '__main__':
    unittest.main()