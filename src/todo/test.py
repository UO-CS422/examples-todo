import unittest
from todo_list import ToDoList
class test_todo_list(unittest.TestCase):

    def test_init(self):
        test_list = ToDoList()
        self.assertEqual(test_list.tasks, [])

if __name__ == '__main__':
    unittest.main()