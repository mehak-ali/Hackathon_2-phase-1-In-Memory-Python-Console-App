from src.logic.todo import (
    add_task,
    get_all_tasks,
    update_task_description,
    set_task_status,
    delete_task,
    TaskNotFoundError,
)

def display_menu():
    print("\nTodo List Menu:")
    print("1. Add a new task")
    print("2. View all tasks")
    print("3. Update a task description")
    print("4. Mark a task as complete")
    print("5. Mark a task as incomplete")
    print("6. Delete a task")
    print("7. Exit")

def get_user_choice():
    while True:
        try:
            choice = int(input("Enter your choice: "))
            if 1 <= choice <= 7:
                return choice
            else:
                print("Invalid choice. Please enter a number between 1 and 7.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main_loop():
    while True:
        display_menu()
        choice = get_user_choice()

        if choice == 1:
            description = input("Enter task description: ")
            try:
                task = add_task(description)
                print(f"Task added: ID {task['id']}, Description: {task['description']}")
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == 2:
            tasks = get_all_tasks()
            if not tasks:
                print("No tasks in the list.")
            else:
                print("\n--- Current Tasks ---")
                for task in tasks:
                    status = "✓" if task['completed'] else " "
                    print(f"[{status}] ID: {task['id']}, Description: {task['description']}")
                print("---------------------")
        elif choice == 3:
            try:
                task_id = int(input("Enter the ID of the task to update: "))
                new_description = input("Enter new description: ")
                task = update_task_description(task_id, new_description)
                print(f"Task ID {task['id']} updated. New Description: {task['description']}")
            except ValueError:
                print("Invalid input. Please enter a valid task ID.")
            except TaskNotFoundError as e:
                print(f"Error: {e}")
        elif choice == 4: # Mark complete
            try:
                task_id = int(input("Enter the ID of the task to mark as complete: "))
                task = set_task_status(task_id, True)
                print(f"Task ID {task['id']} marked as COMPLETE.")
            except ValueError:
                print("Invalid input. Please enter a valid task ID.")
            except TaskNotFoundError as e:
                print(f"Error: {e}")
        elif choice == 5: # Mark incomplete
            try:
                task_id = int(input("Enter the ID of the task to mark as incomplete: "))
                task = set_task_status(task_id, False)
                print(f"Task ID {task['id']} marked as INCOMPLETE.")
            except ValueError:
                print("Invalid input. Please enter a valid task ID.")
            except TaskNotFoundError as e:
                print(f"Error: {e}")
        elif choice == 6:
            try:
                task_id = int(input("Enter the ID of the task to delete: "))
                delete_task(task_id)
                print(f"Task ID {task_id} deleted.")
            except ValueError:
                print("Invalid input. Please enter a valid task ID.")
            except TaskNotFoundError as e:
                print(f"Error: {e}")
        elif choice == 7:
            print("Exiting Todo List. Goodbye!")
            break

if __name__ == "__main__":
    main_loop()