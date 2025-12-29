s = "pythonisawesome"

result = {"vowels" : [], "consonants" : []}
vowel = {"a", "e", "i", "o", "u"}
for i in s:
    if i in vowel:
        result["vowels"].append(i)
    else:
        result["consonants"].append(i)

print(result)