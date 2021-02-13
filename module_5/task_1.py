file = "my_file.txt"

with open(file, "w", encoding="UTF-8") as f:
    while True:
        row = input("type your row and hit enter: ")
        if row == "":
            break
        f.write(f"{row}\n")
