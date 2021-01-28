# task_5, homework 2:
my_list = [7, 5, 3, 3, 2]
user_n = int(input("enter your number:"))
for el in my_list:
    if el < user_n:
        i = my_list.index(el)
        my_list.insert(i, user_n)
        print(my_list)
        break
for el in my_list[-1::]:
    if el >= user_n:
        i = my_list.index(el)
        b = i + 1
        my_list.insert(b, user_n)
        print(my_list)
        break
