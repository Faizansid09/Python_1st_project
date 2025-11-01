#To Do List
task=[]

flag=True
while flag:
    print("To do List")
    print("1. Add a  new list")
    print("2. View All Existing Task") 
    print("3. Delete a task")   
    print("4 .Exit")

    choice=int(input("Enter Choice 1-4:  "))
    if choice==1:
            t=input("Enter new Task: ")
            task.append(t)
            print("Added Sucessfully")
    elif choice ==2:
            if len(task)==0:
                print("No task available")
            else:
                i=1
                for l in task:
                    print(i,".",l)
                    i+=1
    elif choice ==3:
         if len(task)==0:
            print("No task to delete")
         else:
            i=1
            for l in task:
                    print(i,".",l)
                    i+=1
            print("Enter the task to be deleted: ")
            num=int(input())
            if num>=1 and num<len(task):
                      task.pop(num-1)
                      print("Task deleted sucessfully")
                      i=1
                      for l in task:
                         print(i,".",l)
                         i+=1
    elif choice==4:
          print("Exiting...")
          flag=False
    else:
          ("Enter Valid Choice ")