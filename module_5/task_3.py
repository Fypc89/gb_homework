file = "task_3.txt"
with open(file, "r", encoding="UTF-8") as f:
    lines = f.readlines()
av_salary = 0
for line in lines:
    line = line.split()
    av_salary += int(line[1])
    if int(line[1]) < 20000:
        print(f"{line[0]} has salary below 20000")
print(f"Average salary in the company is: {av_salary / len(lines)}")
