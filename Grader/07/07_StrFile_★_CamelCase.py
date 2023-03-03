import string
s = input().strip()
for i in string.punctuation:
    s = s.replace(i, " ")

s = s.split(" ")

i = 0
n = len(s)
while i < n:
    if s[i] == "":
        s.remove(s[i])
        i -= 1
        n -= 1
    i += 1

result = ''
for i in range(len(s)):
    if i == 0:
        result += s[i].lower()
    elif s[i][0] in string.ascii_letters:
        result += s[i].capitalize()
    else:
        result += s[i]

print(result)
