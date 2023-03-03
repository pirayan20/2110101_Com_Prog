import urllib
import urllib.request as urq

dd_url = 'https://www.dek-d.com/home/writer/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'}
dd_request = urq.Request(dd_url, None, headers)
dd_html = str(urq.urlopen(dd_request).read().decode('utf-8'))

m = 'number"'
c = 0
n = 0
n = dd_html.find(m)

for i in range(len(dd_html)):
    if dd_html[i:i+len(m)] == m:
        c += 1

for i in range(c):
    s = ""
    a = dd_html.find('class="title"', n)
    a += 21
    while dd_html[a] != '"':
        s += dd_html[a]
        a += 1
    n = 0 + len(s) + a
    print(s)
