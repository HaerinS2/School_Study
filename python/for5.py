table = [["월","화","수"], [100, 200, 300]]
for row in table:
    for col in row:
        print(col)
    print()

a = [(1, 2), (3, 4), (5, 6)]
for row in a:
    for a in row:
        print(a)
    print()

mun='Happy Programming'
for i, m in enumerate(mun):
    print(i, '-', m)