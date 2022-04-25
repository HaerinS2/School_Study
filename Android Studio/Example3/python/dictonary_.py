# 딕셔너리 생성
d = {}
urls = {"google":"google.com", 18:"unesco.org"}
print(urls)
print(type(urls))

# 딕셔너리 요소 추가
urls["x"] = 2560
print(urls)

# 딕셔너리 요소 수정
urls["x"] = 1920
print(urls)

# 딕셔너리 요소 제거
del urls["x"]
print(urls)
urls.pop(18)
print(urls)
urls.clear()
print(urls)

# 딕셔너리 요소 검색
urls = {"google":"google.com", 18:"unesco.org"} 
print(urls["google"]) # 키 'google'의 값을 가져옴
print(urls.get("google")) # 키 'google'의 값을 가져옴
print("google" in urls) # 키 'google.com'이 있는지 확인한다
print("google.com" in urls) # 키 'google.com'이 있는지 확인한다
print("google.com" in urls.values())

# 기타 딕셔너리 관련 함수
print(len(urls))
print(urls.keys())
print(urls.values())
print(urls.items())