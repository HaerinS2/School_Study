x = int(input())
cnt = 0
for i in range (2, x):
    if(x%i==0):
        cnt+=1
if cnt==2:
    print("소수입니다.")
else:
    print("소수가 아닙니다.")