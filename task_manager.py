import json
import os 

TASKS_FILE = "tasks.json" 

def load_tasks():
if not os.path.exists(TASKS_FILE):
return []
with open(TASKS_FILE, "r") as file:
try:
return json.load(file)
except json.JSONDecodeError:
return [] 

def save_tasks(tasks):
with open(TASKS_FILE, "w") as file:
json.dump(tasks, indent=4) 

def add_task(title):
tasks = load_tasks()
task = {"id": len(tasks) + 1, "title": title, "completed": False}
tasks.append(task)
save_tasks(tasks)
print(f"✅ Task '{title}' successfully added!") 

def list_tasks():
tasks = load_tasks()
if not tasks:
print("📭 No tasks found.")
return
print("\n--- Current Tasks ---")
for task in tasks:
status = "💡 Done" if task["completed"] else "⏳ Pending"
print(f"{task['id']}. {task['title']} [{status}]")
print("---------------------\n") 

def complete_task(task_id):
tasks = load_tasks()
for task in tasks:
if task["id"] == task_id:
task["completed"] = True
save_tasks(tasks)
print(f"🎉 Task {task_id} marked as completed!")
return
print("❌ Task ID not found.") 

def main():
while True:
print("1. Add Task")
print("2. List Tasks")
print("3. Complete Task")
print("4. Exit")
choice = input("Choose an option (1-4): ") 

if choice == "1":
    title = input("Enter task title: ")
    if title.strip():
        add_task(title)
elif choice == "2":
    list_tasks()
elif choice == "3":
    try:
        task_id = int(input("Enter task ID to complete: "))
        complete_task(task_id)
    except ValueError:
        print("❌ Please enter a valid number.")
elif choice == "4":
    print("Goodbye!")
    break
else:
    print("❌ Invalid choice. Try again.")

if **name** == "**main**":
main()