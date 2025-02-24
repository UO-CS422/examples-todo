import pytest
from todo_list import ToDoList

@pytest.fixture
def todo():
    return ToDoList()

def test_constructor(todo):
    assert isinstance(todo, ToDoList)
    assert todo.tasks == []

def test_add_task(todo):
    index = todo.add_task("New Task One")
    assert index == 0
    assert todo.tasks == ["New Task One"]

    index = todo.add_task("New Task Two")
    assert index == 1
    assert todo.tasks == ["New Task One", "New Task Two"]