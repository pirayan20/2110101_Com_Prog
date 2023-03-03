def RLE(message):
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


a = input()
print(RLE(a))
