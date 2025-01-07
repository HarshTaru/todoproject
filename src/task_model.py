import uuid
from datetime import datetime

class Task:
    """A class representing a task."""
    def __init__(self, description, due_date):
        """
        Initializes a new Task instance.

        Args:
            description (str): A brief description of the task.
            due_date (str): The due date for the task in YYYY-MM-DD format.

        Raises:
            ValueError: If description or due_date is missing.
            ValueError: If due_date is not in the correct YYYY-MM-DD format.
        """
        # Ensure both description and due_date are provided
        if not description or not due_date:
            raise ValueError("Description and due date are required.")
        # Ensure due_date is in the correct format
        try:
            self.due_date = datetime.strptime(due_date, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError("Due date must be in YYYY-MM-DD format.")
        
        # Initialize the task attributes

        # Generate a unique identifier for the task
        self.id = str(uuid.uuid4())

        # Set the task description
        self.description = description

        # Set the task completion status
        self.completed = False

    def __repr__(self):
        """
        Provides a string representation of the Task instance.

        Returns:
            str: A string showing the task's ID, description, completion status, and due date.
        """

        return f"Task(id={self.id}, description={self.description}, completed={self.completed}, due_date={self.due_date})"

