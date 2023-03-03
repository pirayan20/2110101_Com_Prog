import urllib
import urllib.request as urq
import os

dir_path = os.path.dirname(os.path.realpath("__file__"))


url = 'https://comprogchula.github.io/'
html = str(urq.urlopen(url).read().decode('utf-8'))

# ---- TO DO 1 : Code Here ----

txt = "Faculty of"
k = "post-entry"
n = 0
c = 0

for i in range(len(html)):
    if html[i] == "ค":
        if html[i+1] == "ณ":
            c += 1
        else:
            pass
    else:
        pass

for i in range(c):
    s = ""
    x = html.find(k, n)
    y = html.find(txt, x)
    while html[y] != "<":
        s += html[y]
        y += 1
    n = 0 + y
    print(s)

print("Number of Faculties :", c)
