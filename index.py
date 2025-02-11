class TodoList:
    def _init_(self):
        self.tasks = []

    def display_tasks(self):
        if not self.tasks:
            print("Your to-do list is empty!")
        else:
            print("\nYour To-Do List:")
            for idx, task in enumerate(self.tasks, start=1):
                print(f"{idx}. {task}")
    
    def add_task(self):
        task = input("Enter the task you want to add: ")
        self.tasks.append(task)
        print(f"Task '{task}' added to your to-do list.")

    def update_task(self):
        self.display_tasks()
        try:
            task_index = int(input("\nEnter the number of the task you want to update: ")) - 1
            if 0 <= task_index < len(self.tasks):
                new_task = input("Enter the updated task: ")
                self.tasks[task_index] = new_task
                print(f"Task {task_index + 1} updated to '{new_task}'.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

    def delete_task(self):
        self.display_tasks()
        try:
            task_index = int(input("\nEnter the number of the task you want to delete: ")) - 1
            if 0 <= task_index < len(self.tasks):
                removed_task = self.tasks.pop(task_index)
                print(f"Task '{removed_task}' removed from your to-do list.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    todo_list = TodoList()

    while True:
        print("\n----- To-Do List Menu -----")
        print("1. View all tasks")
        print("2. Add a new task")
        print("3. Update an existing task")
        print("4. Delete a task")
        print("5. Exit")
        
        choice = input("\nPlease select an option (1-5): ")

        if choice == '1':
            todo_list.display_tasks()
        elif choice == '2':
            todo_list.add_task()
        elif choice == '3':
            todo_list.update_task()
        elif choice == '4':
            todo_list.delete_task()
        elif choice == '5':
            print("Exiting the to-do list. Goodbye!")
            break
        else:
            print("Invalid option. Please choose a number between 1 and 5.")

if __name__ == "__main__":
    main()