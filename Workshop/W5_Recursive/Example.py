
def a(n):  # Recursive method
    if n <= 0:
        return 0
    else:
        return a(n-1) + n


def flatten_list(x):
    if len(x) == 0:
        return x
    h = x[0:1]
    if type(x[0]) is list:
        h = flatten_list(x[0])
    return h + flatten_list(x[1:])


exec(input().strip())
