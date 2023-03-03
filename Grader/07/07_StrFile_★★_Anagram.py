s1 = input()
s2 = input()

s1 = sorted((s1.replace(" ", "")).lower())
s2 = sorted((s2.replace(" ", "")).lower())

anagram = "YES"
if len(s1) != len(s2):
    anagram = "NO"
else:
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            anagram = "NO"
            break

print(anagram)
