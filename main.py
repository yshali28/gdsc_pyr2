"""A kanban board is used to track the status and priorities of various subtasks to be done in a software project.
Implement the following features:
Implement a basic kanban board to be used from a command line interface with 3 statuses (Todo, In progress, and Done)
Addition and removal of tasks to each, and moving them between statuses
Assignees and Reporters
Add more status fields to the Kanban Board
Support for multiple boards for different projects
Allow priorities and sorting by priority (High, Medium, Low)
Brownie points:

Usage of a mouse within the CLI to have drag and drop functionality.

Please make use of an appropriate storage solution to persist tasks, boards, and statuses across runs"""
import csv

# Define the CSV file path
CSV_FILE = 'kanban_tasks.csv'

# Function to load tasks from CSV
def load_tasks():
    tasks = []
    try:
        with open(CSV_FILE, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                tasks.append(row)
    except FileNotFoundError:
        pass
    return tasks

# Function to save tasks to CSV
def save_tasks(tasks):
    with open(CSV_FILE, 'w', newline='') as file:
        fieldnames = ['id', 'title', 'status', 'assignee', 'reporter', 'priority']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(tasks)

# Function to display tasks
def display_tasks(tasks):
    for task in tasks:
        print(f"{task['id']}: {task['title']} [{task['status']}]")

# Function to add a task
def add_task(tasks):
    title = input("Enter task title: ")
    assignee = input("Enter assignee: ")
    reporter = input("Enter reporter: ")
    priority = input("Enter priority (High, Medium, Low): ")
    task = {'id': len(tasks) + 1, 'title': title, 'status': 'Todo', 'assignee': assignee, 'reporter': reporter, 'priority': priority}
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully.")

# Function to move a task
def move_task(tasks):
    display_tasks(tasks)
    task_id = int(input("Enter task id to move: "))
    new_status = input("Enter new status (Todo, In Progress, Done): ")
    for task in tasks:
        if int(task['id']) == task_id:
            task['status'] = new_status
            break
    save_tasks(tasks)
    print("Task moved successfully.")

# Main function
def main():
    tasks = load_tasks()
    while True:
        print("\nKanban Board:")
        display_tasks(tasks)
        print("\nOptions:")
        print("1. Add Task")
        print("2. Move Task")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            move_task(tasks)
        elif choice == '3':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
