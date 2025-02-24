import unittest
from todo.todo_list import ToDoList

class TestToDoList(unittest.TestCase):
    def setUp(self):
        self.todo_list = ToDoList()

    def test_add_task(self):
        index = self.todo_list.add_task("Buy groceries")
        self.assertEqual(index, 0)
        self.assertEqual(self.todo_list.tasks, ["Buy groceries"])
        
        with self.assertRaises(ValueError):
            self.todo_list.add_task("")

    def test_get_task(self):
        self.todo_list.add_task("Buy groceries")
        self.assertEqual(self.todo_list.get_task(0), "Buy groceries")
        
        with self.assertRaises(IndexError):
            self.todo_list.get_task(5)

    def test_remove_task(self):
        self.todo_list.add_task("Buy groceries")
        self.todo_list.add_task("Clean house")
        
        removed = self.todo_list.remove_task(0)
        self.assertEqual(removed, "Buy groceries")
        self.assertEqual(self.todo_list.tasks, ["Clean house"])
        
        with self.assertRaises(IndexError):
            self.todo_list.remove_task(1)

if __name__ == "__main__":
    unittest.main()