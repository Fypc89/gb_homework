#task 1:
a = "word "
b = "to sentence"
c = a + b
print(c)
value_1 = int(input("Enter your number:"))
value_2 = (input("Enter your word:"))
print(f'Here is your data: {value_1}, {value_2}')
print("------------------------------")
#task_2:
value = int(input("Enter number of seconds:"))
h = value // 3600
min = value % 3600 // 60
sec = value % 3600 % 60
print(f'The time is: {h}:{min}:{sec}')
print("------------------------------")
#task_3:
n = int(input("type number between 1 to 9:"))
n = str(n)
nn = n + n
nnn = n + n + n
result = int(n) + int(nn) + int(nnn)
print(f"{n} + {nn} + {nnn} =",result)
print("------------------------------")
#task_4:
user_number = int(input("Enter any number above zero:"))
high_num = 0
while user_number > high_num:
    new_num = user_number % 10
    user_number = user_number // 10
    if new_num > high_num:
        high_num = new_num
print(f'The highest digit is:',high_num)
print("------------------------------")
#task_5:
revenue = int(input("whats your revenue:"))
expenses = int(input("what are your expenses:"))
if revenue > expenses:
    print("Congrats, you are in profit!")
    margin = (revenue - expenses) / revenue * 100
    print(f'Your profit margin is: {margin:.2f}%')
    team = int(input('Type the number of employees you have:'))
    profit_per_one = (revenue - expenses) / team
    print(f'Your profit per person is {profit_per_one:.2f}')
else:
    print("Sadly you're in loss")
print("------------------------------")
#task 6:
result = int(input("first day result(km):"))
target = int(input("your target(km):"))
counter = 0
while target > result:
    result = result + result * 0.1
    counter = counter + 1
print('It will take you', counter, 'days to reach target')
print("------------------------------")
print("THE END....")
