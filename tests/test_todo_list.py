import unittest
from src.todo.todo_list import ToDoList

class TestToDoList(unittest.TestCase):
    def setUp(self):
        self.todo = ToDoList()  # Shorter variable name, common in testing
        # Pre-populate with some tasks for multiple tests
        self.default_tasks = ["Buy groceries", "Walk dog", "Do laundry"]
        
    def populate_default_tasks(self):
        """Helper method to populate list with default tasks"""
        return [self.todo.add_task(task) for task in self.default_tasks]

    def test_add_task(self):
        """Test basic task addition and retrieval"""
        idx = self.todo.add_task("Buy groceries")
        self.assertEqual(idx, 0)
        self.assertEqual(self.todo.get_task(idx), "Buy groceries")

    def test_batch_add_tasks(self):
        """Test adding multiple tasks in sequence"""
        indices = self.populate_default_tasks()
        
        # Test both indices and content
        self.assertEqual(indices, list(range(len(self.default_tasks))))
        self.assertEqual(len(self.todo.tasks), len(self.default_tasks))
        
        # Use zip for cleaner comparison
        for idx, (expected, actual) in enumerate(zip(self.default_tasks, self.todo.tasks)):
            self.assertEqual(expected, actual)

    def test_invalid_task_input(self):
        """Test edge cases for task addition"""
        invalid_inputs = [
            "",                 # Empty string
            " " * 4,           # Whitespace
            None,              # None
            123,               # Non-string
            [],                # Wrong type
            "\n\t",           # Special chars
        ]
        
        for bad_input in invalid_inputs:
            with self.assertRaises(ValueError, msg=f"Failed to catch invalid input: {bad_input}"):
                self.todo.add_task(bad_input)

    def test_task_removal(self):
        """Test task removal and list integrity"""
        self.populate_default_tasks()
        
        # Remove from middle and verify list structure
        removed = self.todo.remove_task(1)
        self.assertEqual(removed, "Walk dog")
        self.assertEqual(self.todo.tasks, ["Buy groceries", "Do laundry"])
        
        # Remove from start
        removed = self.todo.remove_task(0)
        self.assertEqual(removed, "Buy groceries")
        self.assertEqual(len(self.todo.tasks), 1)

    def test_index_bounds(self):
        """Test index boundary conditions"""
        self.todo.add_task("Test task")
        
        invalid_indices = [-1, 1, 99]
        
        for idx in invalid_indices:
            # Test both get and remove operations
            with self.assertRaises(IndexError):
                self.todo.get_task(idx)
            with self.assertRaises(IndexError):
                self.todo.remove_task(idx)

if __name__ == '__main__':
    unittest.main() 