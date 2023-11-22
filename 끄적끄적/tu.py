empty_tuple = ()

#튜플과 리스트는 거의 비슷하지만 가장 큰 차이점은 튜플은 값을 변경할 수 없음
#또한, 튜플에 첫번째 요소만 있을 때도 ","를 써줘야함 ex) a = (1,)
#str과 다른 것은 뒤에 ","를 붙여줘야함

a = "dd",
c = ("dd",) * 3
print(type(a))
print(type(c))
print(c)

print(id(c))
c =a + c
print(c)

#c에 새로운 값이 넣어진 것 같지만 다른 id를 가지고옴. 즉, 기존의 c에 다시는 접근할 수 없으면 새로운 c가 만들어진 것임
# = 튜플은 변경하지 못한다. 그저 새롭게 태어날뿐
# 기존의 튜플을 유지하고 싶으면 새로운 valiable을 사용해서 할당하면 됨
# 
#
q = [1,2,3]
print(type(q)) 
b = q
print(type(b))

a_list = [number for number in range(1,6) if number % 2 == 0]
print(a_list)

rows = range(1,4)
cols = range(1,3)
cells = [(row, col) for row in rows for col in cols]
for cell in cells:
    print(cell)