empty_set = set()
even = {0,2,4,6,8}
odd = {1,3,5,7,9}

even.add(12)
print(even)
even.remove(12)
print(even)


drinks = {
    "martine" : {'vodks',"vermount"},
    "soju" :{"alchole","lum"},
    "baijiu" : {"vodks","alchole"},
    "whitewine" : {"grape","vodks"}
}

# for name, contents in drinks.items():
#     if "vodks" in contents:
#         print(name)



for name, contents in drinks.items():
    if "vodks" in contents and not ('vermount' in contents or "grape" in contents ):
        print(name)

a = {1,2}
b = {2,3}
# print(a.intersection(b))
# print(a|b)
# print(a-b)
print(a.symmetric_difference(b))