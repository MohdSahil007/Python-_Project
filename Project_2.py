#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 2. To-Do List Application

import os

# Function to load tasks from a file
def load_tasks(filename='tasks.txt'):
    tasks = []
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            for line in f:
                task, status = line.strip().split(',')
                tasks.append({'task': task, 'status': status})
    return tasks

# Function to save tasks to a file
def save_tasks(tasks, filename='tasks.txt'):
    with open(filename, 'w') as f:
        for task in tasks:
            f.write(f"{task['task']},{task['status']}\n")

# Function to display tasks
def display_tasks(tasks):
    print("\nTo-Do List:")
    for idx, task in enumerate(tasks, 1):
        status = "Done" if task['status'] == 'complete' else "Not Done"
        print(f"{idx}. {task['task']} - {status}")
    print()

# Function to add a task
def add_task(tasks):
    new_task = input("Enter the new task: ")
    tasks.append({'task': new_task, 'status': 'incomplete'})

# Function to edit a task
def edit_task(tasks):
    display_tasks(tasks)
    task_num = int(input("Enter the task number to edit: ")) - 1
    if 0 <= task_num < len(tasks):
        new_task = input("Enter the new task description: ")
        tasks[task_num]['task'] = new_task
    else:
        print("Invalid task number.")

# Function to delete a task
def delete_task(tasks):
    display_tasks(tasks)
    task_num = int(input("Enter the task number to delete: ")) - 1
    if 0 <= task_num < len(tasks):
        tasks.pop(task_num)
    else:
        print("Invalid task number.")

# Function to mark a task as complete
def mark_complete(tasks):
    display_tasks(tasks)
    task_num = int(input("Enter the task number to mark as complete: ")) - 1
    if 0 <= task_num < len(tasks):
        tasks[task_num]['status'] = 'complete'
    else:
        print("Invalid task number.")

# Main function to run the task manager
def task_manager():
    tasks = load_tasks()
    
    while True:
        print("\nOptions:")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Edit Task")
        print("4. Delete Task")
        print("5. Mark Task as Complete")
        print("6. Save and Exit")

        choice = input("Select an option (1-6): ")

        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            edit_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            mark_complete(tasks)
        elif choice == '6':
            save_tasks(tasks)
            print("Tasks saved. Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

# Run the task manager
task_manager()


# In[ ]:




