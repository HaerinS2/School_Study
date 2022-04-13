game={"LOL","Overwatch","Tetris",1942,2048}
print(game)
a=set("Funny") # set(문자열): 문자열의 문자가 하나씩 요소로 들어간다.
print(a)
print(type(a))
a=set([2048, "Tetris", "Cube"]) # set(리스트): 리스트의 각 요소가 하나씩 셋의 요소로 들어간다.
print(a)
a=set((2560,1440)) # set(튜플): 튜플의 각 요소가 하나씩 셋의 요소로 들어간다.
print(a)
a=set({"google":"google.com",18:"unesco.org"}) # set(딕셔너리): 딕셔너리의 키가 하나씩 셋의 요소로 들어간다
print(a)
a=set(range(3)) # set(range()): range() 함수의 요소가 하나씩 리스트의 요소로 들어간다.
print(a)
game.add("FIFA")
print(game)
game.update(("NBA","MLB"))
print(game)
game.remove("LOL")
print(game)

s3={3, 6, 9, 12}
s4 = {4, 8, 12, 16}
s3 & s4
s3.intersection(s4)
