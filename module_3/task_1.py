while True:
    def my_func(a, b):
        try:
            return print("%.2f" % (a / b))
        except ZeroDivisionError:
            return print("Can't divide on ZERO, try again")
    my_func(float(input("Type first number: ")), float(input("Type second number: ")))