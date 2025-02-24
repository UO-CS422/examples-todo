import pytest

def test_add_task():
    from todo.todo_list import ToDoList
    todo_list = ToDoList()
    assert todo_list.add_task("Task 1") == 0
    assert todo_list.add_task("Task 2") == 1

def test_remove_task():
    from todo.todo_list import ToDoList
    todo_list = ToDoList()
    todo_list.add_task("Task 1")
    todo_list.add_task("Task 2")
    assert todo_list.remove_task(0) == "Task 1"
    assert todo_list.remove_task(0) == "Task 2"

def test_get_task():
    from todo.todo_list import ToDoList
    todo_list = ToDoList()
    todo_list.add_task("Task 1")
    todo_list.add_task("Task 2")
    assert todo_list.get_task(0) == "Task 1"
    assert todo_list.get_task(1) == "Task 2"