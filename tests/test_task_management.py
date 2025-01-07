import unittest
from datetime import date
from src.task_manager import TaskManager
from src.task_model import Task

class TestTaskManager(unittest.TestCase):
    """
    Unit test suite for the TaskManager class.

    This test suite includes tests for all major functionalities of the TaskManager,
    such as adding tasks, marking tasks as complete, listing tasks (filtered or unfiltered),
    and deleting tasks. It also tests error scenarios such as invalid task IDs and incorrect date formats.
    """

    def setUp(self):
        """
        Set up the task manager before each test.

        This method initializes a fresh TaskManager instance before each test case runs.
        It ensures that there are no side effects from previous tests, providing a clean slate.
        """
        self.manager = TaskManager()

    def test_add_task_valid(self):
        """
        Test adding a valid task.

        This test verifies that a valid task can be successfully added to the task manager. 
        It checks if the task attributes such as description, due date, completion status, 
        and ID are set correctly, and confirms the task is added to the task list.
        """
        task = self.manager.add_task("Buy groceries", "2023-06-01")
        self.assertEqual(task.description, "Buy groceries")
        self.assertEqual(task.due_date, date(2023, 6, 1))
        self.assertFalse(task.completed)
        self.assertIsNotNone(task.id)
        self.assertEqual(len(self.manager.tasks), 1)

    def test_add_task_invalid_due_date(self):
        """
        Test adding a task with an invalid due date.

        This test checks that adding a task with an incorrectly formatted due date raises
        a ValueError. The expected format for the due date is YYYY-MM-DD.
        """
        with self.assertRaises(ValueError):
            self.manager.add_task("Buy groceries", "06-01-2023")

    def test_mark_task_as_complete(self):
        """
        Test marking a task as complete.

        This test ensures that when the mark_task_as_complete method is called on a valid task,
        the task's `completed` attribute is correctly set to True.
        """
        task = self.manager.add_task("Buy groceries", "2023-06-01")
        self.assertFalse(task.completed)
        completed_task = self.manager.mark_task_as_complete(task.id)
        self.assertTrue(completed_task.completed)

    def test_mark_task_as_complete_task_not_found(self):
        """
        Test marking a non-existent task as complete.

        This test verifies that trying to mark a task as complete using an invalid task ID
        raises a ValueError. It ensures error handling when attempting to modify a non-existent task.
        """
        with self.assertRaises(ValueError):
            self.manager.mark_task_as_complete("non-existent-id")

    def test_list_all_tasks(self):
        """
        Test listing all tasks.

        This test verifies that the list_tasks method returns all tasks in the task manager,
        regardless of their completion status.
        """
        task1 = self.manager.add_task("Buy groceries", "2023-06-01")
        task2 = self.manager.add_task("Clean the house", "2023-06-02")
        task3 = self.manager.add_task("Walk the dog", "2023-06-03")
        
        tasks = self.manager.list_tasks()
        self.assertEqual(len(tasks), 3)
        self.assertIn(task1, tasks)
        self.assertIn(task2, tasks)
        self.assertIn(task3, tasks)

    def test_list_completed_tasks(self):
        """
        Test listing only completed tasks.

        This test checks that the list_tasks method, when filtered with "completed", 
        only returns tasks that have been marked as completed.
        """
        task1 = self.manager.add_task("Buy groceries", "2023-06-01")
        task2 = self.manager.add_task("Clean the house", "2023-06-02")
        self.manager.mark_task_as_complete(task1.id)
        
        completed_tasks = self.manager.list_tasks(filter_by="completed")
        self.assertEqual(len(completed_tasks), 1)
        self.assertEqual(completed_tasks[0], task1)

    def test_list_pending_tasks(self):
        """
        Test listing only pending tasks.

        This test verifies that the list_tasks method, when filtered with "pending", 
        returns only tasks that have not yet been marked as complete.
        """
        task1 = self.manager.add_task("Buy groceries", "2023-06-01")
        task2 = self.manager.add_task("Clean the house", "2023-06-02")
        self.manager.mark_task_as_complete(task1.id)
        
        pending_tasks = self.manager.list_tasks(filter_by="pending")
        self.assertEqual(len(pending_tasks), 1)
        self.assertEqual(pending_tasks[0], task2)

    def test_delete_task(self):
        """
        Test deleting a task.

        This test verifies that the delete_task method removes a task from the task manager.
        It checks that the task list size decreases after deletion, and confirms the task is no longer in the list.
        """
        task = self.manager.add_task("Buy groceries", "2023-06-01")
        self.assertEqual(len(self.manager.tasks), 1)
        self.manager.delete_task(task.id)
        self.assertEqual(len(self.manager.tasks), 0)

    def test_delete_task_task_not_found(self):
        """
        Test deleting a non-existent task.

        This test verifies that attempting to delete a task with an invalid task ID raises a ValueError.
        """
        with self.assertRaises(ValueError):
            self.manager.delete_task("non-existent-id")

    def test_task_not_found_on_mark_complete(self):
        """
        Test marking a task complete that doesn't exist.

        This test checks that attempting to mark a non-existent task as complete raises a ValueError.
        """
        with self.assertRaises(ValueError):
            self.manager.mark_task_as_complete("invalid-id")

if __name__ == "__main__":
    unittest.main()
