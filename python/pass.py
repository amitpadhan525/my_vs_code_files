i=1000
with open("my_general_pass.txt", "w") as file:
    for i in range(1000,10000):
        file.write(f"amit@{i}\n")