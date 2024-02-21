def is_prime(n):
    """判断一个数是否为素数"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def mersenne_number(p):
    """计算默尼森数"""
    return 2 ** p - 1

def find_mersenne_number(n):
    """找第n个默尼森数"""
    count = 0
    p = 2
    while True:
        if is_prime(p):
            m = mersenne_number(p)
            if is_prime(m):
                count += 1
                if count == n:
                    return m
            if count == 10 * n:
                return None
        p += 1

n = int(input("请输入要查找的默尼森数的序号："))
m = find_mersenne_number(n)
if m:
    print("第%d个默尼森数是：%d" % (n, m))
else:
    print("找不到第%d个默尼森数" % n)