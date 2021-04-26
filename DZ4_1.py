from sys import argv
name_file, production, bet, prize = argv

sal = (int(production) * int(bet) + int(prize))

print(f"Имя файла {name_file}")
print(f"Ваша зарплата {sal}")

