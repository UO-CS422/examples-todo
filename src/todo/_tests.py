from todo_list import ToDoList
from todo_terminal import TodoTerminal

term = TodoTerminal()
list = ToDoList()

def test_insert():
    list.add_task("a")
    list.add_task("3")
    print(list.tasks)
    return
test_insert()