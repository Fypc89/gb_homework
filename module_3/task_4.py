#method_1
def my_func(x, y):
    res = x ** (y * -1)
    res = 1 / res
    print(res)
my_func(float(input("Positive number: ")), int(input("Negative number: ")))
#method_2
def my_func(x, y):
    res = 1
    for n in range(y * -1):
        res = res * x
    return 1 / res
print(my_func(float(input("Positive number: ")), int(input("Negative number: "))))
