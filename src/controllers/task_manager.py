import uuid
from datetime import datetime
from models.task_model import Task

class TaskManager:
    """
    A class for managing tasks.

    This class provides functionality to add, update, list, and delete tasks, with an 
    emphasis on modularity and clean code. Tasks are stored in memory.
    """

    def __init__(self):
        """
        Initializes the TaskManager.

        Attributes:
            tasks (list): A list to store Task objects.
        """
        self.tasks = []

    def add_task(self, description, due_date):
        """
        Adds a new task to the task manager.

        Args:
            description (str): A brief description of the task.
            due_date (str): The due date for the task in YYYY-MM-DD format.

        Returns:
            Task: The newly added task.

        Raises:
            ValueError: If description or due_date is invalid (handled by the Task class).
        """
        try:
            task = Task(description, due_date)
            self.tasks.append(task)
            return task
        except ValueError as e:
            # Handle specific errors related to invalid task attributes
            print(f"Error adding task: {e}")
            raise  # Re-raise the exception for further handling

    def mark_task_as_complete(self, task_id):
        """
        Marks a task as complete.

        Args:
            task_id (str): The unique ID of the task to mark as complete.

        Returns:
            Task: The updated task with its completed flag set to True.

        Raises:
            ValueError: If the task with the given ID is not found.
        """
        try:
            task = self._find_task_by_id(task_id)
            if not task:
                raise ValueError("Task not found.")
            task.completed = True
            return task
        except ValueError as e:
            # Handle task not found error
            print(f"Error marking task as complete: {e}")
            raise  # Re-raise the exception

    def list_tasks(self, filter_by=None):
        """
        Lists tasks, with optional filtering by completion status.

        Args:
            filter_by (str, optional): The completion status to filter by.
                - "completed": Lists only completed tasks.
                - "pending": Lists only pending tasks.
                - None: Lists all tasks (default).

        Returns:
            list: A list of tasks filtered by the specified completion status.
        """
        try:
            if filter_by == "completed":
                return [task for task in self.tasks if task.completed]
            elif filter_by == "pending":
                return [task for task in self.tasks if not task.completed]
            return self.tasks
        except Exception as e:
            # General exception handling in case of unexpected errors
            print(f"Error listing tasks: {e}")
            return []

    def delete_task(self, task_id):
        """
        Deletes a task by its unique ID.

        Args:
            task_id (str): The unique ID of the task to delete.

        Returns:
            bool: True if the task was successfully deleted.

        Raises:
            ValueError: If the task with the given ID is not found.
        """
        try:
            task = self._find_task_by_id(task_id)
            if not task:
                raise ValueError("Task not found.")
            self.tasks.remove(task)
            return True
        except ValueError as e:
            # Handle task not found error
            print(f"Error deleting task: {e}")
            raise  # Re-raise the exception

    def _find_task_by_id(self, task_id):
        """
        Finds a task by its unique ID.

        Args:
            task_id (str): The unique ID of the task to find.

        Returns:
            Task: The task object if found, or None if not found.
        """
        try:
            return next((task for task in self.tasks if task.id == task_id), None)
        except Exception as e:
            # Handle any unexpected errors in finding a task
            print(f"Error finding task: {e}")
            return None
