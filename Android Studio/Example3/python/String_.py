h = " Happy programming!"
print(len(h)) # h 문자열의 길이
print(h.count("p")) # h 문자열에 p가 얼마나 있을까용?
print(h.upper() ) # 소문자를 대문자로
print(h.lower()) # 대문자를 소문자로
print(h.strip()) # 양 옆 띄어쓰기 없어져라 얍!
print(h.replace("Happy", "Funny")) # Happy를 Funny로~
print(h.find("ap")) # 왼쪽부터 ap가 어디에 있나용?
print(h.rfind("a")) # 오른쪽부터 a가 어디에 있나용?
print(h.find("Happy")) # Happy가 어디에 있나용?
print(h.find("fun")) # fun이 어디에 있나용?
print("a" in h) # h 안에 a가 있나용? 맞으면 True 틀리면 False
print("b" in h) # h 안에 b가 있나용? 맞으면 True 틀리면 False
x = "01::23::ab::^^"
y = x.split("::") # ::을 기준으로 문자열 쪼개서 리스트로 만들기~
print(y)
print(", ".join(y)) # ,을 기준으로 문자열 합치기~











