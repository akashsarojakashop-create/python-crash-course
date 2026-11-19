
name = input("Your name: ")
with open("my_diary.txt", "w") as file:
    file.write("My name is " + name)

print("Saved!")

with open("my_diary.txt", "r") as file:
    data = file.read()
    print("Your diary says:", data)

extra = input("Write one more line: ")
with open("my_diary.txt", "a") as file:
    file.write("\n" + extra)

print("Added!")