# Додаємо нову нотатку у файл
date = input("Введіть дату (у форматі YYYY-MM-DD): ")
location = input("Введіть локацію: ")
text = input("Введіть текст нотатки: ")

with open("diary.txt", "a", encoding="utf-8") as file:
    file.write(f"Дата: {date}\n")
    file.write(f"Локація: {location}\n")
    file.write(f"Текст: {text}\n")
    file.write("-" * 40 + "\n")

print("Нотатку збережено у файл.")
