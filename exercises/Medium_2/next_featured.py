"""
C - 
O
D
E
"""

people = {"Jack":30, "John": 25, "Betty": 25, "Anna":30}
sorted_people = sorted(people.items(), key=lambda item: (item[1], item[0]))
print(sorted_people)
# [('Betty', 25), ('John', 25), ('Anna', 30), ('Jack', 30)]