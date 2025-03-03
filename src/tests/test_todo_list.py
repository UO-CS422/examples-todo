from todo.todo_list import ToDoList

def test_constructor():
    list = ToDoList()
    assert len(list.tasks) == 0

def test_add_task():
    list = ToDoList()
    assert len(list.tasks) == 0
    list.add_task("Item 1")
    assert len(list.tasks) == 1
    list.add_task("Item 2")
    assert len(list.tasks) == 2

def test_add_task_returns_index():
    list = ToDoList()
    idx_1 = list.add_task("Item 1")
    assert idx_1 == 0
    idx_2 = list.add_task("Item 2")
    assert idx_2 == 1

def test_get_task():
    list = ToDoList()
    idx = list.add_task("Item 1")
    assert list.get_task(idx) == "Item 1"

def test_get_task_multiple():
    list = ToDoList()
    idx_1 = list.add_task("Item 1")
    idx_2 = list.add_task("Item 2")
    idx_3 = list.add_task("Item 3")
    assert list.get_task(idx_2) == "Item 2"
    
def test_remove_task():
    list = ToDoList()
    assert len(list.tasks) == 0
    idx = list.add_task("Item 1")
    assert len(list.tasks) == 1
    list.remove_task(idx)
    assert len(list.tasks) == 0
