# word = "thud"
# offset = 0

# while offset < len(word):
#     print(word[offset])
#     offset += 1

# for i in word :
#     if i == "d":
#         break
#     print(i)

# for i in range(0,3):
#     print(i)
#     print(list(range(0,3)))

# for i in range(3,-1,-1):
#         print(i)

print(list(range(3,-1,-1)))

guess_me = 7
number = 1
while True:
    if guess_me > number :
        print("too low")
    elif guess_me == number:
        print("found it")
        break
    elif number > guess_me :
        print("oope")
        break
    number+=1 
    print(number)