start1 = ["fee","fie","foe"]
result = [i.title() for i in start1]
start1_cap = " ".join([i.capitalize() + "!" for i in start1 ])
print(start1_cap )


things = ["a","b","c"]
things[1]= things[1].capitalize()
print(things)

del things[-1]
print(things)