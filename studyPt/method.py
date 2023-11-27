# def agree():
#     return True

# if agree():
#     print("true")
# else :
#     print("false")


# def echo(anything):
#     print(anything + " " + anything)

# echo("blahblah")

# def commentary(color):
#     if color == "red":
#         print("It's a tomato")
#     elif color == "blue":
#         print("that color impressed the feeling")
#     else :
#         print("I don't know what to say")

# commentary("red")

# def whatis(thing) :
#     if thing is None :
#         print(thing,"it is none")
#     elif thing :
#         print(thing,"it is true")
#     else :
#         print(thing,"it is false")

# whatis(True)
# whatis(0)

# def menu(wine, entree, dessert) :
#     print("wine :", wine, "entree :", entree, "dessert :", dessert)   

# menu("chardonnay", "chicken","cake")


# def buggy(arg, result = []) :
#     result.append(arg)
#     print(result)

# buggy("a")
# buggy("b")


# def nonbuggy(arg, result = None):
#     if result is None:
#         result = []
#     result.append(arg)
#     print(result)

# new_list = ["new"]
# nonbuggy("a",new_list)
# nonbuggy("b")

# def print_data(data,*, start = 0, end =100):
#     for value in (data[start : end]):
#         print(value)

# data = ["a","b","c","d","e","f"]
# print_data(data)

# print_data(data, start = 4)
# print_data(data, end = 4)

#인수가 가변 객체인 경우 해당 매개변수를 통해 함수 내부에서 값을 변경할 수 있다.
# outside = ["one","two","three"]
# def mangle(arg):
#     arg[1] = "no it is four"

# print(outside)
# mangle(outside)
# print(outside)

# def add_args(arg1, arg2):
#     print(arg1 + arg2)

# print(add_args(1,2))

# def add_args_with(func,arg1,arg2):
#     func(arg1, arg2)

# print(add_args_with(add_args,1,2))

# def sum_args(*args):
#     return sum(args)

# def run_with_po(func,*args):
#     return func(*args)

# print(run_with_po(sum_args,1,2,3,4))

def edit_story(words,func):
    for word in words:
        print(func(word))

staris = {"thus","meow","thud","hiss"}
# def enliven(word):
#     return word.capitalize() + "!"

edit_story(staris,lambda word:word.capitalize()+"!")