def star(c, *n):
    for i in range(0, len(n)):
        print(c*n[i])
star("♡", 3)
star("♡", 1, 2, 3)