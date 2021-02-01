def int_func(words):
    result = ""
    for el in words:
        el = el[0].upper() + el[1:]
        result += el + " "
    return result


fin_res = input("type your words: ")
print(int_func(fin_res.split()))
