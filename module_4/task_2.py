orig_list = input("original 10 random numbers via space: ").split()
def numbers(orig_list):
    new_list = []
    for i in range(1, len(orig_list)):
        if orig_list[i] > orig_list[i-1]:
            yield new_list.append(orig_list[i])
        print(new_list)
print(numbers(orig_list))
#не могу понять где ошибка, почему не работает