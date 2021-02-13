file = "task_2.txt"

with open(file, "r", encoding="UTF-8") as f:
    row = f.readlines()
print(f"number of rows in file = {len(row)}")
for i, words in enumerate(row, 1):
    print(f"{i} row has {len(words.split())} words")
