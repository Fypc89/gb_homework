def fact(n):
    new_nr = 1
    for i in range(1, n + 1):
        new_nr *= i
        yield new_nr

for el in fact(int(input("enter your factorial number: "))):
    print(el)
