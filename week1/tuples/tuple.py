from collections import defaultdict

class_list = (("VII", 1), ("V", 1), ("V", 2), ("VI", 1), ("VI", 2), ("VI", 3))

id_list = defaultdict(list)

for c, i in class_list:
    id_list[c].append(i)

print(id_list)
