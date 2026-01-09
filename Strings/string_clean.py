raw = "  Adam, Bob,  Casey ,Eva  "
w = raw.strip()

result = w.split(",")
clean = []
for name in result:
    if name not in clean:
        c = name.strip()
        clean.append(c)

print(clean)
