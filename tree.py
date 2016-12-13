def tree(n):
    for a in range(n):
        print((n - 1 - a) * ' ' + '*' + a * 2 * '*')
    print((' ' * (n - 1) + '*\n') * n)

tree(10000)