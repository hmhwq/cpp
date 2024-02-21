def is_prime(n):             # 判断一个数是否为素数
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def M(p):
    return 2**p - 1

def find(n):
    i = 0
    p = 2
    while True:
        m = M(p)
        if is_prime(m):
            i += 1
            if i == n:
                return m
        else:
            p += 1
            