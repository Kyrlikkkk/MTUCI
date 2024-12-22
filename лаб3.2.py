a = input("Введите текст: ")
with open("user_input.txt", "w") as file:
    file.write(a)

b = input("Введите текст для добавления: ")
with open("user_input.txt", "a") as file:
    file.write("\n" + b)


