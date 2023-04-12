import random
students = {"Кутилина", "Петров", "Поликарпова", "Аги", "Лавриненко", "Семенов"}
languages = {"Английский", "Корейский", "Немецкий", "Китайский"}
k = {}

for i in students:
    chis = random.randint(1,3)
    k[i] = random.sample(list(languages), chis)

lang = set()
for i in k:
    lang = lang.union(set(k[i]))

ch = [i for i in k if "Китайский" in k[i]]
print("Люди, знающие китайский: ", *ch)


