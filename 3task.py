with open("diary.txt", "r", encoding="utf-8") as file:
    content = file.read()

entries = content.split("----------------------------------------\n")
locations = set()
word_count = 0

for entry in entries:
    lines = entry.strip().split("\n")
    for line in lines:
        if line.startswith("Локація:"):
            loc = line.replace("Локація:", "").strip()
            locations.add(loc)
        elif line.startswith("Текст:"):
            text = line.replace("Текст:", "").strip()
            word_count += len(text.split())

print("Кількість записів:", len([e for e in entries if e.strip() != ""]))
print("Кількість унікальних локацій:", len(locations))
print("Загальна кількість слів у всіх нотатках:", word_count)
