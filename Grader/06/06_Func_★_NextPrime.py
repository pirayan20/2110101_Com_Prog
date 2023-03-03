def is_prime(n):
 # ทดสอบว่า n เป็นจำนวนเฉพาะหรือไม่
    if n <= 1:
        return False
    for k in range(2, int(n**0.5)+1):
        if n % k == 0:
            return False
    return True


def next_prime(n):
    if is_prime(n) == True:
        n += 1
        while is_prime(n) == False:
            n += 1
        return n
    else:
        while is_prime(n) == False:
            n += 1
        return n


def next_twin_prime(n):
    if is_prime(n) == False:
        while True:
            if is_prime(n) == True:
                if is_prime(n+2) == True:
                    return n, n+2
                else:
                    n += 1
            else:
                n += 1

    else:
        n += 1
        while True:
            if is_prime(n) == True:
                if is_prime(n+2) == True:
                    return n, n+2
                else:
                    n += 1
            else:
                n += 1


exec(input().strip())
