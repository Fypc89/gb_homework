from itertools import count

start = int(input("enter first number: "))
end = int(input("enter last number: "))

for el in count(start):
    if el > end:
        break
    print(el)

from itertools import cycle

for el in cycle([5, 10, 15]):
    iter_nr = input("enter 'N' to continue iteration and 'Q' to stop: ")
    if iter_nr == "Q" or iter_nr == "q":
        break
    print(el)
