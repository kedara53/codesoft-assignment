import json
import os

# Initialize the task list
tasks = []

# Load tasks from file if it exists
if os.path.exists('tasks.json'):
    with open('tasks.json', 'r') as file:
        tasks = json.load(file)

def save_tasks():
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file)

def add_task(description):
    task = {
        'id': len(tasks) + 1,
        'description': description,
        'completed': False
    }
    tasks.append(task)
    save_tasks()
    print(f"Task added: {description}")

def view_tasks():
    if not tasks:
        print("No tasks found.")
        return
    for task in tasks:
        status = "Completed" if task['completed'] else "Not Completed"
        print(f"ID: {task['id']}, Description: {task['description']}, Status: {status}")

def update_task(task_id, description=None, completed=None):
    for task in tasks:
        if task['id'] == task_id:
            if description:
                task['description'] = description
            if completed is not None:
                task['completed'] = completed
            save_tasks()
            print(f"Task updated: ID {task_id}")
            return
    print(f"Task not found: ID {task_id}")

def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    save_tasks()
    print(f"Task deleted: ID {task_id}")

def main():
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            description = input("Enter task description: ")
            add_task(description)
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            try:
                task_id = int(input("Enter task ID to update: "))
                description = input("Enter new description (leave blank to keep current): ")
                completed_input = input("Is the task completed? (yes/no/leave blank to keep current): ")
                completed = None
                if completed_input.lower() == 'yes':
                    completed = True
                elif completed_input.lower() == 'no':
                    completed = False
                update_task(task_id, description if description else None, completed)
            except ValueError:
                print("Invalid input. Please enter a valid task ID.")
        elif choice == '4':
            try:
                task_id = int(input("Enter task ID to delete: "))
                delete_task(task_id)
            except ValueError:
                print("Invalid input. Please enter a valid task ID.")
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == '__main__':
    main()
