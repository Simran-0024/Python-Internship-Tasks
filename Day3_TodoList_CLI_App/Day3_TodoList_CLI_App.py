work_list=['Task 1', 'Task 2', 'Task 3', 'Task 4', 'Task 5']

while True:
    reply=input("What would you like to do? (add_task-->a / remove_task-->b / exit-->e / view_list-->v): ").strip().lower()
    if len(work_list) == 0:
        print("Your work list is empty.")
    elif reply=="a":
      task= input("Enter the task you want to add: ")
      work_list.append(task)
      print(f"'{task}' has been added to your work list.")
    elif reply=="b":
      task= input("Enter the task you want to remove: ")
      if task in work_list:
          work_list.remove(task)
          print(task ,"has been removed from your work list.")
      else:
          print(task, "is not in your work list.")
    elif reply=="v":
      print("Your current work list:")
      for task in work_list:
          print(task)
    elif reply=="e":
      print("Exiting the application. Goodbye!")
      exit()
    