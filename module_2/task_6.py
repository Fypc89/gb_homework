dict1 = {}
name = input("name:")
price = input("price:")
qty = input("qty:")
unit = input("unit:")
dict1.update({"name": name, "price": price, "qty": qty, "unit": unit})
print("-------------")
dict2 = {}
name = input("name:")
price = input("price:")
qty = input("qty:")
unit = input("unit:")
dict2.update({"name": name, "price": price, "qty": qty, "unit": unit})
print("-------------")
dict3 = {}
name = input("name:")
price = input("price:")
qty = input("qty:")
unit = input("unit:")
print("-------------")
dict3.update({"name": name, "price": price, "qty": qty, "unit": unit})
final_list = [(1, dict1), (2, dict2), (3, dict3)]
print(final_list)
print("-------------")
print("-------------")
final_dict = {"name":[dict1.get("name"), dict2.get("name"), dict3.get("name")],
              "pice":[dict1.get("price"), dict2.get("price"), dict3.get("price")],
              "qty": [dict1.get("qty"), dict2.get("qty"), dict3.get("qty")],
              "unit":[dict1.get("unit"), dict2.get("unit"), dict3.get("unit")]}
print(final_dict)
