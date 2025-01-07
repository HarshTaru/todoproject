import uuid
from datetime import datetime

class Task:
    """A class representing a task."""
    def __init__(self, description, due_date):
        if not description or not due_date:
            raise ValueError("Description and due date are required.")
        try:
            self.due_date = datetime.strptime(due_date, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError("Due date must be in YYYY-MM-DD format.")
        self.id = str(uuid.uuid4())
        self.description = description
        self.completed = False

    def __repr__(self):
        return f"Task(id={self.id}, description={self.description}, completed={self.completed}, due_date={self.due_date})"

