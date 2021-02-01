def my_sum ():
    fin_sum = 0
    b = False
    while b == False:
        number = input('Input numbers or A to stop: ').split()
        res = 0
        for el in range(len(number)):
            if number[el] == 'A':
                b = True
                break
            else:
                res = res + int(number[el])
        fin_sum = fin_sum + res
        print(f'Current sum is {fin_sum}')
    print(f'Your final sum is {fin_sum}')

my_sum()
