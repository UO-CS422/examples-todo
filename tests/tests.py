import unittest
from todo.todo_list import ToDoList

class ToDoList:
    """A class to manage a simple to-do list."""
    def __init__(self) -> None:
        self.tasks = []

    def add_task(self, task: str) -> int:
        if not isinstance(task, str) or not task.strip():
            raise ValueError("Task must be a non-empty string.")
        self.tasks.append(task)
        return len(self.tasks) - 1

    def get_task(self, index: int) -> str:
        if index < 0 or index >= len(self.tasks):
            raise IndexError("Task index out of range.")
        return self.tasks[index]

    def remove_task(self, index: int) -> str:
        if index < 0 or index >= len(self.tasks):
            raise IndexError("Task index out of range.")
        return self.tasks.pop(index)

if __name__ == '__main__':
    unittest.main()