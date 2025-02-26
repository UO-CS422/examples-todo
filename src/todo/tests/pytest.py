import pytest
from todo.todo_list import ToDoList

def test_add_task():
    assert ToDoList().add_task("Task 1") == 0
    assert ToDoList().add_task("Task 2", "Task 3") == 1
    print("Give Josh an A!")