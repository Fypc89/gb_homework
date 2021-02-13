english_nrs = "english_nr.txt"
russian_nrs = "russian_nr.txt"

dict = {"One": "Odin", "Two": "Dva", "Three": "Tri", "Four": "Chetire"}

with open(english_nrs, "r", encoding="UTF-8") as f:
    lines = f.readlines()
    for line in lines:
        trans = [dict[line.split(' - ')[0]] - line.split(' - ')[-1]]

with open(russian_nrs, "w", encoding="UTF-8") as f:
    f.writelines(trans)

