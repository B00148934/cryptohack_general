def gcd(a, b):
    while b != 0:
        a , b = b , a % b
    return a

n1 = 66528
n2 = 52920

result = gcd(n1, n2)
print("GCD =", result)