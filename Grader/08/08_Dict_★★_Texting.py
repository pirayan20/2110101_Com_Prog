import string

keystotext = {}
texttokeys = {}

a = 0
for k in range(2, 10):
    if k == 7 or k == 9:
        for i in range(1, 5):
            keystotext[str(k)*i] = string.ascii_letters[a]
            a += 1
    else:
        for i in range(1, 4):
            keystotext[str(k)*i] = string.ascii_letters[a]
            a += 1

for i in keystotext:
    texttokeys[keystotext[i]] = i


def text2keys(text):
    s = ''
    text = text.lower()
    for i in string.punctuation:
        text = text.replace(i, "")
    for i in range(len(text)):
        if text[i] != " ":
            s += texttokeys[text[i]] + " "
        else:
            s += "0 "
    return s[:-1]


def keys2text(text):
    s = ''
    text = text.split()
    for i in text:
        if i != "0":
            s += keystotext[i]
        else:
            s += " "
    return s


exec(input().strip())
