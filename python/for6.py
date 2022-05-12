array = []
for i in range(1, 10, 2):
    array.append(i*i)
print(array)

array = [i*i for i in range(1, 10, 2)]
print(array)

array = [i*i for i in range(1, 10, 2) if i*i > 30]
print(array)   