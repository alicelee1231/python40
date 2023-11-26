# e2f = {"dog" : "chien", 
#     "cat" : "chat",
#     "walrus" : "morse"
#     }
# print(e2f.items())
# print(e2f["walrus"])

# f2e = {}
# for en, fr in e2f.items() :
#     f2e[fr]=en
# print(f2e["chien"])
# f2e["chien"] = "pi"
# print(f2e)
# c = list(e2f.items())
# print(c[0][0])

# print([k for k, v in e2f.items() if v == "chien"])
# print(e2f.keys())

# life = {
#     "animals" : {
#         "cats" : [
#             "Henri", "Grumpy", "Lucy"
#             ],
#         'octopi' : {},
#     "emus" : {}
#         },
#     "plants" :{},
#     "others" : {}
# }
# print(list(life.keys()))
# print(list(life["animals"]["cats"]))

# squares = { i : i*i for i in range(10)}
# print(squares)

# com = {d for d in range(10) if d % 2 == 1}
# print(type(com))

#제너레이터 수식은 list comprehension과 비슷하지만 대괄호[] 대신 ()를 사용
for thing in ('Got %s' %number for number in range(10)) :
    print(thing)


# key =    {"optimist", "pessimist", "troll"   }
# values = {"The glass is half full","The glass is half empty", "How did you get a glass?"}

# print(dict(zip(key,values)))

# titles = ["Creature of Habit", "Crewel Fate"]
# plots = ["A run turns into a mon ster", "A hunted yarn shop"]
# movies = dict(zip(titles,plots))
# print(movies)