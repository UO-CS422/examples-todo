import unittest
from todo.todo_list import ToDoList

def todo():
    return ToDoList()

def test_initialize(todo):
    assert isinstance(todo, ToDoList)
    assert todo.tasks.empty()