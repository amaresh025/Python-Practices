s = "   python is powerful   "
remove_spaces = s.strip()

print(remove_spaces.upper())

raw = "apple, banana , mango ,orange,  grapes "
result = raw.split(",")
cleaned = []


for fruit in result:
    c = fruit.strip()
    if c not in cleaned:
        cleaned.append(c)

print(cleaned)