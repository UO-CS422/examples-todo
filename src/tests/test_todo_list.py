import pytest
from todo.todo_list import ToDoList

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

def test_add_task_invalid(todo):
    with pytest.raises(ValueError, match="Task must be a non-empty string."):
        todo.add_task("")
    with pytest.raises(ValueError, match="Task must be a non-empty string."):
        todo.add_task("    ")
    with pytest.raises(ValueError, match="Task must be a non-empty string."):
        todo.add_task(None)

def test_get_task(todo):
    todo.add_task("Task 1")
    todo.add_task("Task 2")

    assert todo.get_task(0) == "Task 1"
    assert todo.get_task(1) == "Task 2"

def test_get_task_invalid(todo):
    with pytest.raises(IndexError, match="Task index out of range."):
        todo.get_task(0)  # No tasks added yet
    todo.add_task("Task 1")
    with pytest.raises(IndexError, match="Task index out of range."):
        todo.get_task(2)

def test_remove_task(todo):
    todo.add_task("Task A")
    todo.add_task("Task B")

    removed = todo.remove_task(0)
    assert removed == "Task A"
    assert todo.tasks == ["Task B"]

def test_remove_task_invalid(todo):
    with pytest.raises(IndexError, match="Task index out of range."):
        todo.remove_task(0)  # No tasks added yet

    todo.add_task("Task X")
    with pytest.raises(IndexError, match="Task index out of range."):
        todo.remove_task(1)

if __name__ == "__main__":
    pytest.main()