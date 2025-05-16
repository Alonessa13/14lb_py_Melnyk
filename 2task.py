search = input("Введіть дату або ключове слово для пошуку: ").lower()

with open("diary.txt", "r", encoding="utf-8") as file:
    entries = file.read().split("----------------------------------------\n")

    found = False
    for entry in entries:
        if search in entry.lower():
            print(entry)
            print("-" * 40)
            found = True

    if not found:
        print("Записів не знайдено.")
