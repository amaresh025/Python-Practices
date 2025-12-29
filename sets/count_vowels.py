vowels = {"a", "e", "i", "o", "u"}

def count_vowel(s):
    counts = 0
    for i in s:
        if i in vowels:
            counts += 1

    return counts


print(count_vowel("aeiouaeiou"))