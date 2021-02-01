def my_func(el1, el2, el3):
    if el1 >= el3 and el2 >= el3:
        print("the sum is:", el1 + el2)
    elif el1 >= el2 and el3 >= el2:
        print("the sum is:", el1 + el3)
    else:
        print("the sum is:", el2 + el3)
my_func(int(input("Number1: ")), int(input("Number2: ")), int(input("Number3: ")))
