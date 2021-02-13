file = "task_5.txt"

with open(file, "w", encoding="UTF-8") as f:
    numbers = input("Please input some numbers separated by space:")
    f.write(numbers)

with open(file, "r", encoding="UTF-8") as f:
    numbers_str = f.read()
    print(sum([int(el) for el in numbers_str.split()]))