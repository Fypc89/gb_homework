from sys import argv
def salary(hours, rate, bonus):
    return f"the salary is: {int(hours) * int(rate) + int(bonus)}"
script, hours, rate, bonus = argv
print(salary(hours, rate, bonus))
#to run code in pycharm: print(salary(input("hours:"), input("rate: "), input("bonus: ")))
