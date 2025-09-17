#Simple to-do list in python
import os
import json

def load_tasks():
    """Load tasks from file, or return empty list if file doesn't exist"""
    try:
        with open('tasks.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
def save_tasks(tasks):
    """Save tasks to file"""
    """We use open to interact with the file in a write/edit mode"""
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file, indent=2)
    """json.dump takes python and converts it to a json format"""

def display_tasks(tasks):
    """Show all tasks to the user"""
    if not tasks:
        print("No tasks yet! Add one to get started.")
        return
    print("\n--- Your To-Do List ---")
    #for I is for the position number like 1, 2 or 3. task is the dictionary, and enumerate is the list and we start at 1. 
    #enumerate gives you an index:item pair. 
    for i, task in enumerate(tasks, 1):
        status = "✓" if task['completed'] else "○"
        print(f"{i}. {status} {task['description']}")

def add_task(tasks):
    """Add a new task"""
    description = input("Enter a new task: ")
    new_task = {
        'description': description,
        'completed': False
    }
    tasks.append(new_task)
    print(f"Added: '{description}'")

def complete_task(tasks):
    """Mark a task as completed"""
    display_tasks(tasks)
    
    if not tasks:
        return
    
    try:
        task_num = int(input("Enter task number to mark complete: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]['completed'] = True
            print(f"Marked as complete: '{tasks[task_num - 1]['description']}'")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

def delete_task(tasks):
    """Delete a task"""
    display_tasks(tasks)
    
    if not tasks:
        return
    
    try:
        task_num = int(input("Enter task number to delete: "))
        if 1 <= task_num <= len(tasks):
            deleted_task = tasks.pop(task_num - 1)
            print(f"Deleted: '{deleted_task['description']}'")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

def show_menu():
    """Display the main menu"""
    print("\n=== TO-DO LIST ===")
    print("1. View tasks")
    print("2. Add task")
    print("3. Complete task")
    print("4. Delete task")
    print("5. Quit")

def main():
    """Main program loop"""
    # Load existing tasks
    tasks = load_tasks()
    
    while True:
        show_menu()
        choice = input("\nChoose an option (1-5): ")
        
        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
            save_tasks(tasks)
        elif choice == '3':
            complete_task(tasks)
            save_tasks(tasks)
        elif choice == '4':
            delete_task(tasks)
            save_tasks(tasks)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please enter 1-5.")

# Run the program
if __name__ == "__main__":
    main()
