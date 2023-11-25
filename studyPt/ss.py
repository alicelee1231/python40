# year_list = [1980,1981,1982,1983,1984, 1985]
things = ["mozzarella","cinderella","salmonella"]
# print(things[1].capitalize())
# print(things)

i_upper = []
for i in things :
    if i == "mozzarella" :
        i_upper.append(i.upper())
    elif i == "cinderella": 
        i_upper.append(i)
    elif i == "salmonella":
        del things[2]
print(i_upper)

suprise = ["Groucho","Chico","Harpo"]

a= suprise[-1].lower()
print(a)
b= a[::-1]
print(b.capitalize())
# b=suprise.reverse()
# print(suprise)

cc = [ i for i in range(1,11) if i % 2 == 0]
print(cc)

