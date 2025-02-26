import unittest
from todo.todo_list import ToDoList

def todo():
    return ToDoList()

def test_initialize(todo):
    assert isinstance(todo, ToDoList)
    assert todo.tasks.empty()

def test_todo_list_add_task():
    test_list = ToDoList()
    test_list.add_task("task 1")
    assert test_list.tasks[0] == "task 1"