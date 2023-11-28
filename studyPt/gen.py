'''list의 경우 list의 모든 값이 메모리에 적재됨 ,
그러나 generator의 경우 next()에 할당된 것만 차례대로 적재됨
그래서 메모리를 더 효율적으로 다룰 수 있음
데이터를 저장하지 않음
''' 

#generator comprehension
genobj = (pair for pair in zip(['a','b'],['1','2']))
print(genobj)

for things in genobj:
    print(things)

#decorator 작성
#*args, **kwarg는 모든 변수를 받을 수 있는것

def square_it(func):
    def new_function(*args, **kwargs):
        result = func(*args, **kwargs)
        return result + result
    return new_function

@square_it
def add_ints(a,b):
    return a + b

print(add_ints(3,1))
