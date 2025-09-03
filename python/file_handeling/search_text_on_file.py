with open("my_general_pass.txt", "r") as file:
    text=input("Enter text to search: ")
    if text in file.read():
        print("found")