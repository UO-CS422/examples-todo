import pytest
from todo.todo_list import ToDoList

def test_add_task():
    todo = ToDoList()
    index = todo.add_task("Buy groceries")
    assert index == 0
    assert todo.get_task(0) == "Buy groceries"

def test_add_task_invalid():
    todo = ToDoList()
    with pytest.raises(ValueError):
        todo.add_task("")

def test_get_task():
    todo = ToDoList()
    todo.add_task("Read a book")
    assert todo.get_task(0) == "Read a book"

def test_get_task_invalid_index():
    todo = ToDoList()
    with pytest.raises(IndexError):
        todo.get_task(0)

def test_remove_task():
    todo = ToDoList()
    todo.add_task("Workout")
    removed = todo.remove_task(0)
    assert removed == "Workout"
    assert len(todo.tasks) == 0

def test_remove_task_invalid_index():
    todo = ToDoList()
    with pytest.raises(IndexError):
        todo.remove_task(0)
