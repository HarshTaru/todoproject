import unittest
from datetime import date
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from src.task_model import Task

class TestTask(unittest.TestCase):
    """
    A test suite for the Task class.

    This suite includes tests for creating tasks, handling invalid input, 
    and verifying the string representation of tasks.
    """

    def test_task_creation_valid(self):
        """
        Test creating a task with valid inputs.

        Verifies that:
        - The task is created successfully.
        - The description, due date, and default completion status are correct.
        - A unique ID is assigned to the task.
        """
        task = Task("Buy groceries", "2021-06-01")
        self.assertEqual(task.description, "Buy groceries")
        self.assertEqual(task.due_date, date(2021, 6, 1))
        self.assertFalse(task.completed)
        self.assertIsNotNone(task.id)

    def test_task_creation_invalid_due_date_format(self):
        """
        Test creating a task with an invalid due date format.

        Verifies that:
        - A ValueError is raised when the due date is not in YYYY-MM-DD format.
        - The exception message is as expected.
        """
        with self.assertRaises(ValueError) as context:
            Task("Buy groceries", "06-01-2021")
        self.assertEqual(str(context.exception), "Due date must be in YYYY-MM-DD format.")

    def test_task_creation_missing_description(self):
        """
        Test creating a task with a missing description.

        Verifies that:
        - A ValueError is raised when the description is empty.
        - The exception message is as expected.
        """
        with self.assertRaises(ValueError) as context:
            Task("", "2021-06-01")
        self.assertEqual(str(context.exception), "Description and due date are required.")

    def test_task_creation_missing_due_date(self):
        """
        Test creating a task with a missing due date.

        Verifies that:
        - A ValueError is raised when the due date is empty.
        - The exception message is as expected.
        """
        with self.assertRaises(ValueError) as context:
            Task("Buy groceries", "")
        self.assertEqual(str(context.exception), "Description and due date are required.")

    def test_task_representation(self):
        """
        Test the string representation of a task.

        Verifies that:
        - The __repr__ method correctly formats the task's attributes into a string.
        """
        task = Task("Buy groceries", "2021-06-01")
        expected_repr = f"Task(id={task.id}, description=Buy groceries, completed=False, due_date=2021-06-01)"
        self.assertEqual(repr(task), expected_repr)

if __name__ == "__main__":
    unittest.main()
