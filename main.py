# main.py

from todo_list import ToDoList
from storage import Storage

def print_menu():
    print("\nTo-Do List Manager")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Mark Task as Completed")
    print("4. Clear All Tasks")
    print("5. Mark Task as Pending")
    print("6. Exit")

def main():
    todo_list = ToDoList()
    todo_list.tasks = Storage.load_tasks()

    while True:
        print_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            todo_list.add_task(title, description)
            Storage.save_tasks(todo_list.tasks)
            print("Task added successfully!")
        elif choice == '2':
            todo_list.list_tasks()
        elif choice == '3':
            task_id = int(input("Enter task ID to mark as completed: "))
            if todo_list.mark_task_completed(task_id):
                Storage.save_tasks(todo_list.tasks)
                print("Task marked as completed!")
            else:
                print("Task ID not found.")
        elif choice == '4':
            todo_list.clear_tasks()
            Storage.save_tasks(todo_list.tasks)
            print("All tasks cleared!")
        elif choice == '5':
            task_id = int(input("Enter task ID to mark as pending: "))
            if todo_list.mark_task_pending(task_id):
                Storage.save_tasks(todo_list.tasks)
                print("Task marked as pending!")
            else:
                print("Task ID not found.")
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
