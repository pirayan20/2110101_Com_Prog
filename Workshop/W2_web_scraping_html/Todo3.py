import urllib
import urllib.request as urq
url = 'https://comprogchula.github.io/'
html = str(urq.urlopen(url).read().decode('utf-8'))

start = 0
n = 0
a = 0

while True:
    start = html.find('><a href="https://comprogchula.github.io/faculty', start+1)
    stop = html.find('.html', start+1)
    name = html[start+41:stop]
    if start == -1:
        break
    else:
        url1 = html[start+10:stop+5]
        html1 = str(urq.urlopen(url1).read().decode('utf-8'))
        print(name)
        while True:
            if url1 != 'https://comprogchula.github.io/faculty-of-communication-arts-chulalongkorn-university.html':
                a = html1.find('<div id="wpcf-field-custom-content-contact-2"', a+1)
                a1 = html1.find('22', a + 1)
                a2 = html1.find('<', a1)
            else:
                a = html1.find('<p><strong>Tel:</strong>', a + 1)
                a1 = html1.find('22', a+1)
                a2 = html1.find('<', a1)
            if a == -1:
                break
            else:
                z = html1[a1:a2]
                z = z.replace('+66', '0')
                print('     '+'0'+' ' + z)
                n += 1


print('Number of faculty:', n)
