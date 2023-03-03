dna = input().strip()
dna = dna.upper()
base = "ATCG"
size = True
command = input()

for i in range(len(dna)):
    if dna[i] not in base:
        print("Invalid DNA")
        size = False
        break

newdna = ''
if size == True:
    if command == "R":
        for i in range(len(dna)):
            if dna[i] == "A":
                newdna += "T"
            elif dna[i] == "C":
                newdna += "G"
            elif dna[i] == "T":
                newdna += "A"
            else:
                newdna += "C"
        print(newdna[::-1])

    elif command == "F":
        a, b, c, d = 0, 0, 0, 0
        for i in range(len(dna)):
            if dna[i] == "A":
                a += 1
            elif dna[i] == "T":
                b += 1
            elif dna[i] == "G":
                c += 1
            else:
                d += 1

        dna = "A"*a + "T"*b + "G"*c + "C"*d

        answer = ""
        i = 0

        while i <= len(dna)-1:
            count = 1
            alpha = dna[i]
            k = i
            while k < len(dna)-1:
                if dna[k] == dna[k+1]:
                    count += 1
                    k += 1
                else:
                    break
            answer = answer+alpha+"="+str(count)+", "
            i = k+1

        print(answer[:-2])

    elif command == "D":
        count = 0
        pair = input().strip()
        for i in range(len(dna)-1):
            if dna[i:i+2] == pair:
                count += 1
        print(count)
