from ..src.todo.todo_terminal import ToDoTerminal
import unittest


class TestToDoListTerminal(unittest.TestCase):

    def setUp(self):
        self.todo_terminal = ToDoTerminal()

    def test_display_meun(self):
        self.todo_terminal.display_menu()

'''I want to go home so i will finish this later'''


if __name__ == '__main__':
    unittest.main()

