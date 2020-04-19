
n = 5


def fact_iter(n):
    x = 1
    for i in range(n, 0, -1):
        # x = x * i
        x *= i
    return x


def fact_recur(n):
    if n <= 1:
        return 1
    else:
        return n * fact_recur(n-1)
    

print(fact_recur(n))
