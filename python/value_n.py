def hello(n, *value):
    for i in range(n):
        for s in value:
            print(s)

hello(3, "안녕하세요", "정보통신과", "파이팅!")