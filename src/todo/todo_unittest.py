import unittest
from todo_list import ToDoList

class test_TodoList(unittest.TestCase):
    def test_add_task(self):
        index1 = TodoList.add_task("fun thing")
        #should be zero indexed
        self.assertEqual(index1, 0)
        index2 = TodoList.add_task("fun thing2")
        self.assertEqual(index2, 1)

if __name__ == '__name__':
    unittest.main(testRunner=unittest.TextTestRunner(resultclass=test_TodoList))
