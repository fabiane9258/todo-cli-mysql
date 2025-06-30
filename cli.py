from todo import add_task, list_tasks, delete_task

def show_menu():
    print("\n📝 To-Do CLI")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Delete Task")
    print("4. Exit")

def main():
    while True:
        show_menu()
        choice = input("Enter choice: ").strip()

        if choice == "1":
            desc = input("Enter task description: ")
            add_task(desc)
            print("✅ Task added.")

        elif choice == "2":
            tasks = list_tasks()
            if not tasks:
                print("📭 No tasks found.")
            else:
                for t in tasks:
                    print(f"[{t[0]}] {t[1]}")

        elif choice == "3":
            task_id = input("Enter task to delete: ")
            delete_task(task_id)
            print("🗑️ Task deleted.")

        elif choice == "4":
            print("👋 Goodbye!")
            break

        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()



            
