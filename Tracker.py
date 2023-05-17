import pandas as pd

# Function to add a new task
def add_task(tasks):
    task_name = input("Enter the task name: ")
    tasks.append(task_name)
    task_index = len(tasks) - 1
    print(f"Task added successfully! Index: {task_index}")

# Function to delete a task
def delete_task(tasks):
    task_index = int(input("Enter the index of the task to delete: "))

    if task_index >= 0 and task_index < len(tasks):
        del tasks[task_index]
        print("Task deleted successfully!")
    else:
        print("Invalid task index!")

# Function to update a task
def update_task(tasks):
    task_index = int(input("Enter the index of the task to update: "))

    if task_index >= 0 and task_index < len(tasks):
        new_task_name = input("Enter the updated task name: ")
        tasks[task_index] = new_task_name
        print("Task updated successfully!")
    else:
        print("Invalid task index!")

# Function to display tasks
def display_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        df = pd.DataFrame(tasks, columns=["Task"])
        print(df)

# Main menu
def main():
    tasks = []
    
    while True:
        print("Task Manager")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Update Task")
        print("4. Display Tasks")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            delete_task(tasks)
        elif choice == "3":
            update_task(tasks)
        elif choice == "4":
            display_tasks(tasks)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")

# Entry point of the program
if __name__ == "__main__":
    main()




