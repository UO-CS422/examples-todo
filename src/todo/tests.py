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