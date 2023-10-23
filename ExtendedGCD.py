def egcd(a, b):
    if a%b == 0:
        return [0,1]

    [u,v] = egcd(b,a%b)
    q = (a - a % b) / b
    return [v,u-v*q]

n1 = 26513
n2 = 32321
print(egcd(n1, n2))