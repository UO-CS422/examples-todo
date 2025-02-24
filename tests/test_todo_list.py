import nose
from src/todo/todo_list import ToDoList

@raises(IndexError)
def test_empty_class():
    empty = ToDoList()
    empty.remove_task(3)

def test_add_get():
    li = ToDoList()
    li.add_task(1)
    li.add_task(2)
    li.add_task(3)
    assert(li.get_task(1) == 1)
    assert(li.get_task(2) == 2)
    assert(li.get_task(3) == 3)
