import unittest
from todo.todo_list import TodoList, TodoItem

class TestTodoList(unittest.TestCase):

    def setUp(self):
        self.todo_list = TodoList()

    def test_add_item(self):
        item = TodoItem("Test task")
        self.todo_list.add_item(item)
        self.assertIn(item, self.todo_list.items)

    def test_remove_item(self):
        item = TodoItem("Test task")
        self.todo_list.add_item(item)
        self.todo_list.remove_item(item)
        self.assertNotIn(item, self.todo_list.items)

    def test_complete_item(self):
        item = TodoItem("Test task")
        self.todo_list.add_item(item)
        self.todo_list.complete_item(item)
        self.assertTrue(item.completed)

if __name__ == '__main__':
    unittest.main()