n = int(input())
docinf = {}
docset = {}
for i in range(n):
    docname = input().strip()
    information = input().split()
    docinf[docname] = information
    k = set()
    for i in information:
        k.add(i)
    docset[docname] = k

while True:
    s = input().strip()
    if s != '-1':
        docpoint = {}
        for doc in docinf:
            wordcount = 0
            relate = 0
            for word in docinf[doc]:
                if s == word:
                    wordcount += 1
            relate = wordcount / len(docinf[doc]) / len(docset[doc])
            docpoint[doc] = relate
        maximus = max(list(docpoint.values()))
        if maximus == 0:
            print("NOT FOUND")
        else:
            for doc in docpoint:
                if docpoint[doc] == maximus:
                    print(doc)

    else:
        break