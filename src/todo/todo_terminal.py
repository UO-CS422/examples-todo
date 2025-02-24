from todo_list import ToDoList

class TodoTerminal:
    """A terminal application for managing a To-Do list."""
    
    def __init__(self):
        """Initialize the TodoTerminal with an empty ToDoList."""
        self.todo_list = ToDoList()
    
    def display_menu(self):
        """Display the main menu options."""
        print("\nTo-Do List Application")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")

    def view_tasks(self):
        """Display all tasks in the to-do list."""
        print("\nCurrent Tasks:")
        if not self.todo_list.tasks:
            print("No tasks available.")
        else:
            for index, task in enumerate(self.todo_list.tasks):
                print(f"{index}: {task}")

    def add_task(self):
        """Prompt the user to add a new task."""
        task = input("Enter the task description: ")
        try:
            index = self.todo_list.add_task(task)
            print(f"Task added at index {index}.")
        except ValueError as e:
            print(f"Error: {e}")

    def remove_task(self):
        """Prompt the user to remove a task by index."""
        self.view_tasks()
        try:
            index = int(input("Enter the index of the task to remove: "))
            removed_task = self.todo_list.remove_task(index)
            print(f"Removed task: {removed_task}")
        except (ValueError, IndexError) as e:
            print(f"Error: {e}")

    def run(self):
        """Run the main application loop."""
        while True:
            self.display_menu()
            choice = input("Choose an option (1-4): ")
            
            if choice == "1":
                self.view_tasks()
            elif choice == "2":
                self.add_task()
            elif choice == "3":
                self.remove_task()
            elif choice == "4":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    app = TodoTerminal()
    app.run()