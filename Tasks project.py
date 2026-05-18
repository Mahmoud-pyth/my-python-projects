today_tasks = input("Enter you tasks for today separated by a comma: ").split(", ")
done_tasks = []
ongoing_tasks = []
for task in today_tasks:
 print(f"\ntask\n")
 done = input(f"Did you finish {task} already: (yes or no)")
 if done.lower() == "yes":
  print("Nice jop!")
  done_tasks.append(task)
 else:
  print("Try not to put it off")
  ongoing_tasks.append(task)
 print("_______")
progress = input("Do you want to see your today's progress? (yes or no)")
if progress.lower() == "yes":
 print(f"The tasks you done: {done_tasks}")
 print(f"The ongoing tasks: {ongoing_tasks}")
else:
 input("Press 'Enter' to exit.")
