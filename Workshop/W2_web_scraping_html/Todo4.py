import urllib
import urllib.request as urq
import os

dir_path = os.path.dirname(os.path.realpath("__file__"))

# -------------------------------------------------------------

url = 'https://www.cp.eng.chula.ac.th/en/about/faculty/'
html = str(urq.urlopen(url).read().decode('utf-8'))

n = 0
c = 0
v = 0
m = "mis.cp.eng"
d = 'href="/en/about/faculty/'
l = len(m)
ld = len(d)
x = html.find("Retired")
y = html.find("Deceased")

for i in range(0, x):
    if html[i:i+l] == m:
        c += 1

print("Current Faculty Members")
print(" ")

for i in range(c):
    s = ''
    a = html.find(m, n)
    b = html.find("<p>", a)
    b += 3
    while html[b] == " ":
        b += 1
    while html[b:b+4] != "    ":
        s += html[b]
        b += 1
    n = 500 + b
    print(s)

for j in range(x, y):
    if html[j:j+ld] == d:
        v += 1

print("")
print("Retired faculty members")

for i in range(v):
    s = ''
    a = html.find(d, x)
    b = html.find("<p>", a)
    b += 3
    while html[b] == " ":
        b += 1
    while html[b:b+4] != "    ":
        s += html[b]
        b += 1
    x = 500 + b
    print(s)
