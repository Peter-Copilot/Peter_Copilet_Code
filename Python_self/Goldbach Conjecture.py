def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def goldbach_conjecture_check(limit):
    for even_number in range(4, limit + 1, 2):
        goldbach = False
        for prime1 in range(2, even_number):
            if is_prime(prime1) and is_prime(even_number - prime1):
                goldbach = True
                break
        if not goldbach:
            print(f"哥德巴赫猜想在 {even_number} 处被证明是错误的。")
            return
    print(f"在给定的范围内（<= {limit}），哥德巴赫猜想验证正确。")

if __name__ == "__main__":
    limit = 100000000
    goldbach_conjecture_check(limit)
