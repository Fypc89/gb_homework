# task 4, homework 2:
words = input("Enter a few words here: ").split()
counter = 0
for i in words:
    counter += 1
    print(counter, i[:10])