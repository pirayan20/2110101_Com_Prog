import urllib
import urllib.request as urq
import os

dir_path = os.path.dirname(os.path.realpath("__file__"))


url = 'https://comprogchula.github.io/'
html = str(urq.urlopen(url).read().decode('utf-8'))

# ---- TO DO 2 : Code Here ----

# -------------------------------เพิ่ม folder--------------------------------------
# -------------------------!mkdir -p faculty_image-------------------------------

k = "post-media"
m = len(k)
c = 0
n = 0

for i in range(len(html)):
    if html[i:i+m] == k:
        c += 1

g = ''
b = '/content/faculty_image/'

for i in range(c):
    x = html.find('data-src="', n)
    x += 10
    g = ''
    while html[x] != '"':
        g += html[x]
        x += 1
        n = 0 + x + len(g)
        g = str(g)

    d = urq.urlopen(str(g))
    l = open(b + g[37::], 'wb')
    l.write(d.read())
    l.close()

'''
d = urq.urlopen("https://comprogchula.github.io/image/chula-faculty-allied-health-sciences-hero-desktop-1024x640.jpg")
l = open('/content/faculty_image/chula-faculty-allied-health-sciences-hero-desktop-1024x640.jpg', 'wb')
l.write(d.read())
l.close()
'''
