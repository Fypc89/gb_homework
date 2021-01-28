# task_3 homework 2:
#
# method_1:
month = int(input('Please enter month number: '))
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
          "November", "December"]
for i in months:
    m = months[month - 1]
print(f"Your month is: {m}")
#
# method_2:
month = input('Please enter a different month number: ')
months = {"1": "January", "2": "February", "3": "March", "4": "April", "5": "May", "6": "June", "7": "July",
              "8": "August", "9": "September", "10": "October", "11": "November", "12": "December"}
print("You months is:", months.get(month))
