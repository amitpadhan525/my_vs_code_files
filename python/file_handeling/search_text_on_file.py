with open("my_text_file.txt", "r") as file:
    text=input("Enter text to search: ")
    if text in file.read():
        print("found")