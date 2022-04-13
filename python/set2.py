s3={3, 6, 9, 12}
s4 = {4, 8, 12, 16}
print(s3 & s4)
s3.intersection(s4)

print(s3|s4)
s3.union(s4)

print(s3 - s4)
s3.difference(s4)

print(s3 ^ s4)
s3.symmetric_difference(s4)