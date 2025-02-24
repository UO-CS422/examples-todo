import pytest

def test_display_menu():
    from todo.todo_terminal import TodoTerminal
    todo_terminal = TodoTerminal()
    assert todo_terminal.display_menu() == None

def test_view_tasks():
    from todo.todo_terminal import TodoTerminal
    todo_terminal = TodoTerminal()
    assert todo_terminal.view_tasks() == None

def test_add_task():
    from todo.todo_terminal import TodoTerminal
    todo_terminal = TodoTerminal()
    todo_terminal.add_task()
    assert todo_terminal.add_task() == None