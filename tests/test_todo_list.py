import pytest
from todo.todo_list import ToDoList

def test_get_task():
    todo = ToDoList()
    task = "Write unit tests"
    todo.add_task(task)
    assert todo.get_task(0) == task

def test_get_task_invalid_index():
    todo = ToDoList()
    with pytest.raises(IndexError, match="Task index out of range."):
        todo.get_task(1)  # No task at index 1


def test_remove_task_invalid_index():
    todo = ToDoList()
    with pytest.raises(IndexError, match="Task index out of range."):
        todo.remove_task(0)  # No task to remove

def test_todo_list_add_task():
    """
    GIVEN a todo list instance
    WHEN I call the add task method.
    THEN the task should be added to the todo list.
    """
    test_list = ToDoList()
    test_list.add_task("Write test cases")
    assert test_list.tasks[0] == "Write test cases"

def test_todo_list_remove_task():
    """
    GIVEN a todo list
    WHEN I call the remove task method
    THEN a task will be removed.
    """
    test_list = ToDoList()
    test_list.tasks = ["foo", "bar"]
    test_list.remove_task(1)
    assert test_list.tasks == ["foo"]

def test_todo_list_raise_value_error():
    """
    GIVEN I add a task to a todo list
    WHEN the task is non a valid string
    THEN a value error is raised.
    """
    test_list = ToDoList()
    with pytest.raises(ValueError):
        test_list.add_task(0)
