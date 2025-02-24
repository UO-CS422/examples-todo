from todo.todo_list import ToDoList

import pytest

def test_add_task():
    test_list = ToDoList()
    res = test_list.add_task("new_task_1")
    assert res == 0


def test_get_task():
    test_list = ToDoList()
    test_list.add_task("new_task")
    res = test_list.get_task(0)
    assert res == "new_task"

def test_remove_task():
    test_list = ToDoList()
    test_list.add_task("new_task")
    res = test_list.remove_task(0)
    assert res == "new_task"