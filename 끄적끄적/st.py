# while True :
#     stuff = input("String to capitalization [type q to quit]: ")
#     if stuff == "q":
#         break
#     print(stuff.capitalize())


while True :
    value = input("Integer, please [q to quit]:")
    if value == "q" : 
        break
    number = int(value)
    if number % 2 == 0:
        continue
    print(number,"squard is", number*number)