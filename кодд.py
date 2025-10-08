print("Добро пожаловать в конвертер величин")
print("Я могу преобразовать различные единицы измерения")

while True:
    print("Выберите тип конвертации")
    print("1. Метры в километры")
    print("2. Километры в метры")
    print("3. Градусы Цельсия в Фаренгейты")
    print("4. Сантимертры в дециметры")
    print("5. Килограммы в фунты")

    print("0. Выход")


    value = float(input("Введите число для конвертации: "))

    choice = str(input("Введите номер операции: ")).strip()  



    match choice: 
        case "1":
            result = value / 1000  # перевод из метров в километры
            print(f"{value}м = {result}км")
    match choice:
         case "2":
             result = value * 1000
             print(f"{value}км = {result} м")
    match choice:
         case "3":
              result = (value * 9/5) + 32
              print(f"{value} C = {result} F")
    match choice:
         case "4":
             result = value / 10
             print(f"{value} см = {result} дм")
    match choice:
         case "5":
             result = value * 2.20462
             print(f"{value} кг = {result} фунтов")

    match choice:
        case "0":
            print("До свидания!")
            break