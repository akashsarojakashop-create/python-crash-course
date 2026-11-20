task = input("what is task today:")

with open("my_task.txt","a") as file:
    file.write(task+"\n")

print("task saved!")

print("\n---your all task---")
with open("my_task.txt","r") as file:
 print(file.read())


