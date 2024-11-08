def show_menu():
    print("\n--- To-Do List ---")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    return choice

# Function to view tasks
def view_tasks(tasks):
    if len(tasks) == 0:
        print("\nNo tasks found.")
    else:
        print("\nTo-Do List:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")

# Function to add a task
def add_task(tasks):
    task = input("Enter the task description: ")
    tasks.append(task)
    print(f"Task '{task}' added to the list.")

# Function to delete a task
def delete_task(tasks):
    if len(tasks) == 0:
        print("\nNo tasks to delete.")
        return
    view_tasks(tasks)
    try:
        task_idx = int(input("Enter the task number to delete: ")) - 1
        if 0 <= task_idx < len(tasks):
            deleted_task = tasks.pop(task_idx)
            print(f"Task '{deleted_task}' deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Main program loop
def main():
    tasks = ["Walk Dog", "Buy Groceries", "Play Football"]
  # Initialize the task list
    print("Starting To-Do List application...")  # For debugging
    while True:
        choice = show_menu()  # Show the menu and get the user's choice
        
        if choice == 1:
            view_tasks(tasks)
        elif choice == 2:
            add_task(tasks)
        elif choice == 3:
            delete_task(tasks)
        elif choice == 4:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

# Ensure the main function is called
if __name__ == "__main__":
    main()
