import unittest
from unittest.mock import patch, MagicMock
from io import StringIO
from todo.todo_terminal import TodoTerminal

class TestTodoTerminal(unittest.TestCase):
    def setUp(self):
        self.terminal = TodoTerminal()

    @patch('sys.stdout', new_callable=StringIO)
    def test_view_tasks(self, mock_stdout):
        # Empty list
        self.terminal.view_tasks()
        self.assertIn("No tasks available", mock_stdout.getvalue())
        
        # With tasks
        self.terminal.todo_list.add_task("Test task")
        mock_stdout.truncate(0)
        mock_stdout.seek(0)
        self.terminal.view_tasks()
        self.assertIn("0: Test task", mock_stdout.getvalue())

    @patch('builtins.input', return_value="New task")
    @patch('sys.stdout', new_callable=StringIO)
    def test_add_task(self, mock_stdout, mock_input):
        self.terminal.add_task()
        self.assertEqual(self.terminal.todo_list.tasks, ["New task"])
        self.assertIn("Task added", mock_stdout.getvalue())

    @patch('builtins.input', side_effect=["0"])
    @patch('sys.stdout', new_callable=StringIO)
    def test_remove_task(self, mock_stdout, mock_input):
        self.terminal.todo_list.add_task("Test task")
        self.terminal.remove_task()
        self.assertEqual(self.terminal.todo_list.tasks, [])
        self.assertIn("Removed task", mock_stdout.getvalue())

if __name__ == "__main__":
    unittest.main()