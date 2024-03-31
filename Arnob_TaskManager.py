class Task:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = False  # Initially, the task is not completed

    def mark_as_completed(self):
        self.completed = True  # Mark the task as completed

    def __str__(self):
        status = "Completed" if self.completed else "Not Completed"
        # Return the task details in a formatted string
        return f"Title: {self.title}\nDescription: {self.description}\nDue Date: {self.due_date}\nStatus: {status}\n"


class TaskManager:
    def __init__(self):
        self.tasks = []  # Initialize an empty list to store tasks

    def add_task(self, task):
        self.tasks.append(task)  # Add a task to the task list

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            for index, task in enumerate(self.tasks, start=1):
                print(f"Task {index}:")
                print(task)  # Display task details for each task in the list

    def mark_task_completed(self, task_index):
        if 0 < task_index <= len(self.tasks):
            self.tasks[task_index - 1].mark_as_completed()  # Mark the selected task as completed
            print("Task marked as completed.")
        else:
            print("Invalid task index.")

def main():
    task_manager = TaskManager()

    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date: ")
            new_task = Task(title, description, due_date)
            task_manager.add_task(new_task)
            print("Task added successfully.")

        elif choice == '2':
            print("Tasks:")
            task_manager.view_tasks()

        elif choice == '3':
            task_manager.view_tasks()
            task_index = int(input("Enter the task number to mark as completed: "))
            task_manager.mark_task_completed(task_index)

        elif choice == '4':
            print("Exiting Task Manager. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 to 4.")

if __name__ == "__main__":
    main()
