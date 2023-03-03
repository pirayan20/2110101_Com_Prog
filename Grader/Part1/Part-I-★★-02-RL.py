def str2RLE(message):
    answer = ""
    i = 0

    while i <= len(message)-1:
        count = 1
        alpha = message[i]
        k = i
        while k < len(message)-1:
            if message[k] == message[k+1]:
                count += 1
                k += 1
            else:
                break
        answer = answer+alpha+" "+str(count)+" "
        i = k+1
    return answer


def RLE2str(message):
    message = message[0::].split(" ")
    i = 0
    s = ""
    while i <= len(message)-2:
        s += message[i]*int(message[i+1])
        i += 2
    return s


k = input()
if k == "str2RLE":
    m = input()
    print(str2RLE(m))
elif k == "RLE2str":
    m = input()
    print(RLE2str(m))
else:
    print("Error")
