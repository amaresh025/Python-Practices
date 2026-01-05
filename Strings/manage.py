s = "hello world from python"
result = s.title()
print(result)


s3 = " a, b , c ,d  , e "
r = s3.split(",")

cleaned = []
for i in r:
    c = i.strip()
    if c not in cleaned:
        cleaned.append(c)

print(cleaned)



s2 = "  hi   i   am   adam  "
n = s2.strip()
n2 = n.split()
n3 = " ".join(n2)
print(n3)


s4 = "python_is_easy_and_powerful"
stp = s4.split("_")
result = " ".join(stp)
org = result.title()
print(org)