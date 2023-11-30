# def dive():
#     return dive()

# import time
# import asyncio

# async def find_users_async(n):
#     for i in range(1, n + 1):
#         print(f'{n}명 중 {i}번 째 사용자 조회 중 ...')
#         await asyncio.sleep(1)
#     print(f'> 총 {n} 명 사용자 비동기 조회 완료!')

# async def process_async():
#     start = time.time()
#     await asyncio.wait([
#         find_users_async(3),
#         find_users_async(2),
#         find_users_async(1),
#     ])
#     end = time.time()
#     print(f'>>> 비동기 처리 총 소요 시간: {end - start}')

# if __name__ == '__main__':
#     asyncio.run(process_async())

# short_list = [1,2,3]
# position = 5
# try :
#     short_list[position]
# except:
#     print("Need a position between 0 and", len(short_list)-1, 'but got', position)

# short_list = [1,2,3]
# while True :
#     value = input("Position [ q to quit] ?")
#     if value == "q":
#         break
#     try :
#         position = int(value)
#         print(short_list[position])
#     except IndentationError as err :
#         print("Bad index :", position)
#     except Exception as other :
#         print("Something else broke:", other)

#1번 문제
# def good():
#     a = ['Harry', 'Ron', 'Hermione']
#     print(a)

# good()

#2번문제 generator

def get_odds():
    for number in range(1,10,2):
        yield number

count = 1
for number in get_odds():
    if count == 3 :
        print("the third odd number is ", number)
        break
    count +=1


#3번 문제 decorator
def test(fun):
    def new_fun(): #wrapper 함수
        print("start")
        fun()
        print("end")
    return new_fun


@test
def fun1():
    print("test")
fun1()


def decorator1(func):
    def wrapper():
        print('decorator1')
        func()
    return wrapper
 
def decorator2(func):
    def wrapper():
        print('decorator2')
        func()
    return wrapper
 
# 데코레이터를 여러 개 지정
@decorator1
@decorator2
def hello():
    print('hello')
 
hello()

#4번 예외처리 문제
class OopsException(Exception):
    pass
try : 
    raise OopsException
except OopsException :
    print("Caught an oops")


