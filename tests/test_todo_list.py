import pytest
from todo.todo_list import ToDoList

def test_add_task():
    todo = ToDoList()
    task = "Write unit tests"
    index = todo.add_task(task)
    assert index == 0
    assert todo.tasks == [task]

def test_add_task_invalid():
    todo = ToDoList()
    with pytest.raises(ValueError, match="Task must be a non-empty string."):
        todo.add_task("")  # Testing with an empty string

def test_get_task():
    todo = ToDoList()
    task = "Write unit tests"
    todo.add_task(task)
    assert todo.get_task(0) == task

def test_get_task_invalid_index():
    todo = ToDoList()
    with pytest.raises(IndexError, match="Task index out of range."):
        todo.get_task(1)  # No task at index 1

def test_remove_task():
    todo = ToDoList()
    task = "Write documentation"
    todo.add_task(task)
    removed_task = todo.remove_task(0)
    assert removed_task == task
    assert len(todo.tasks) == 0

def test_remove_task_invalid_index():
    todo = ToDoList()
    with pytest.raises(IndexError, match="Task index out of range."):
        todo.remove_task(0)  # No task to remove
from todo.todo_list import ToDoList

def test_constructor():
    list = ToDoList()
    assert list.tasks == []

def test_add():
    list = ToDoList()
    list.add_task("test")
    assert list.tasks == ["test"]

def test_get():
    list = ToDoList()
    list.add_task("test")
    assert list.get_task(0) == "test"

def test_remove():
    list = ToDoList()
    list.add_task("test")
    list.remove_task(0)
    assert list.tasks == []
