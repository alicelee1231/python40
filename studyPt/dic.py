import copy

# a = {}
# lol = [["a","b"],['c','d'],['e','f']]
# print(dict(lol))
# print(lol)

# first = {'a':'agony', 'b':"bliss"}
# second = {"c" :"cat", "d":"daddy"}
# thrid = {"d":"dd",}
# print({**first,**second,**thrid})

# del first["a"]
# print(first)
# second.pop("d")
# print(second,"pop")
# second.clear()
# print(second,"clear")


# pythonw = {"chang" :"gram" , "mac" :"machere","mcdonal":"hamburger"}
# print("chandg" in pythonw)

# #할당
# save_first = first
# print(save_first)
# first["a"] = "changed"
# print(first)

#얕은 복사는 원래의 값만 변경되고 복사한 값은 변경되지 않는다. 단, 딕셔너리 값이 불변이면 동작(str), 가변이면 동작안함 -> deepcopy()사용해야함 
# sam = {"demon" :"trace", "ton" : "up"}
# samso = sam.copy()
# sam["demon"] = "angel"
# print(sam)
# print(samso)

# samsoni =  copy.deepcopy(sam)
# print(samsoni)
# sam["demon"] = "mumu"
# print(sam)
# print(samsoni)

# for etc,btc in sam.items():
#     print("etc",etc, "btc",btc)


word = "letters"
letter_count = {letter : word.count(letter) for letter in word}
print(letter_count)
