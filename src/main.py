from datetime import date
from controllers.task_manager import TaskManager

def display_task(task):
    """
    Helper function to display a task in a formatted manner.

    Args:
        task (Task): The task object to be displayed.
    
    This function prints the task's ID, description, due date, and its status 
    (whether it is "Completed" or "Pending"). It also prints a separator line 
    for better readability.
    """
    # Determine the task's completion status
    status = "Completed" if task.completed else "Pending"
    
    # Print task details
    print(f"Task ID: {task.id}")
    print(f"Description: {task.description}")
    print(f"Due Date: {task.due_date}")
    print(f"Status: {status}")
    print("-" * 40)  # Separator for formatting

def main():
    """
    Main function that demonstrates how to use the TaskManager class.

    This function:
    - Initializes a TaskManager instance.
    - Adds a few tasks to the task manager.
    - Marks a task as complete.
    - Lists all tasks, completed tasks, and pending tasks.
    - Deletes a task and shows the updated list of tasks.
    """
    # Initialize TaskManager
    manager = TaskManager()

    # Add some tasks to the task manager
    task1 = manager.add_task("Buy groceries", "2025-02-10")
    task2 = manager.add_task("Clean the house", "2025-02-12")
    task3 = manager.add_task("Complete Python project", "2025-02-15")

    # Display all tasks
    print("All Tasks:")
    # Iterate through all tasks and display each one
    for task in manager.list_tasks():
        display_task(task)

    # Mark the first task as complete
    print("\nMarking Task 1 as complete...")
    # Change the status of task1 to completed
    manager.mark_task_as_complete(task1.id)
    
    # Display tasks again with updated status
    print("\nAll Tasks After Marking Task 1 as Complete:")
    for task in manager.list_tasks():
        display_task(task)

    # List only completed tasks
    print("\nCompleted Tasks:")
    # Filter and display only completed tasks
    for task in manager.list_tasks(filter_by="completed"):
        display_task(task)

    # List only pending tasks
    print("\nPending Tasks:")
    # Filter and display only pending tasks
    for task in manager.list_tasks(filter_by="pending"):
        display_task(task)

    # Delete a task (Task 2)
    print("\nDeleting Task 2...")
    # Delete task2 from the task manager
    manager.delete_task(task2.id)

    # Display all tasks after deletion
    print("\nAll Tasks After Deleting Task 2:")
    # Show remaining tasks after deletion
    for task in manager.list_tasks():
        display_task(task)

# Run the main function when the script is executed
if __name__ == "__main__":
    main()
