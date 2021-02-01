# task 2, homework 2
lst = input("Enter your list using space:").split()
list1 = []
for i in range(0, len(lst), 2):
    list1.append(lst[i])
list2 = []
for i in range(1, len(lst), 2):
    list2.append(lst[i])
list3 = []
if len(list1) % 2 == 0:
    for i in range(len(list2)):
        list3.append(list2[i])
        list3.append(list1[i])
else:
    for i in range(len(list2)):
        list3.append(list2[i])
        list3.append(list1[i])
    list3.append(list1[-1])
print(list3)
