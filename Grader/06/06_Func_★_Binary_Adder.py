# x = input()
# x = x[0::].split(" ")


# def binary2decimal(e):
#     decimal = 0
#     k = len(e)-1
#     for i in range(len(e)):
#         decimal += int(e[i])*(2**k)
#         k -= 1
#     return decimal


# for i in range(len(x)):
#     x[i] = binary2decimal(x[i])

# y = sum(x)
# y = bin(y)

# print(y[2::])

x = input().split()
print(bin(int(x[0],2)+int(x[1],2))[2:])
