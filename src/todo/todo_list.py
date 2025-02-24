class ToDoList:
    """A class to manage a simple to-do list."""

    def __init__(self) -> None:
        """Initialize the to-do list with an empty tasks list."""
        self.tasks = []

    def add_task(self, task: str) -> int:
        """
        Add a new task to the to-do list.

        Args:
            task (str): The task description to add.

        Returns:
            int: The index of the added task in the list.

        Raises:
            ValueError: If the task is not a non-empty string.
        """
        if not isinstance(task, str) or not task.strip():
            raise ValueError("Task must be a non-empty string.")
        self.tasks.append(task)
        return len(self.tasks) - 1  # Returns the index of the added task

    def get_task(self, index: int) -> str:
        """
        Retrieve a task by its index from the to-do list.

        Args:
            index (int): The index of the task to retrieve.

        Returns:
            str: The task description at the specified index.

        Raises:
            IndexError: If the index is out of the range of the task list.
        """
        if index < 0 or index >= len(self.tasks):
            raise IndexError("Task index out of range.")
        return self.tasks[index]

    def remove_task(self, index: int) -> str:
        """
        Remove a task by its index from the to-do list.

        Args:
            index (int): The index of the task to remove.

        Returns:
            str: The removed task description.

        Raises:
            IndexError: If the index is out of the range of the task list.
        """
        if index < 0 or index >= len(self.tasks):
            raise IndexError("Task index out of range.")
        return self.tasks.pop(index)