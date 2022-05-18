our_pots={'김규진':1, '김도원':2, '김찬웅':3, '김채은':4, '김태현':5}
print(our_pots)
print()

for i in our_pots:
    print(i)
print()

for i in our_pots:
    print('{}의 집에는 {}개의 냄비가 있다.'.format(i, our_pots[i]))
print()

for i in our_pots:
    if our_pots:
        if our_pots[i]>3:
            print(i)
print()

for i in our_pots:
    if our_pots:
        if our_pots[i]>3:
            print(i)
        break
print()

for i in range(2, 10):
    for j in range(1, 10):
        print("{} x {} = {}".format(i, j, j*i))
print()

dan=2
while dan<10:
    for i in range(1, 10):
        print("{} x {} = {}".format(dan, i, dan*i))
    dan+=1
print()

for i in range(1, 101):
    if i%2!=0:
        print(i)
print()

for i in range(100, 201):
    if i%3==0:
        print(i)
print()
