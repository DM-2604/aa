mydict = {"name":"vasu","age":22}

print(mydict.values())
print(mydict.keys())
print(mydict.items())
mydict.setdefault("sal",30000)
mydict.update({"year":2025})
mydict['sal'] = 90000
# mydict['year'] = "2026"




for x in mydict:
    if mydict['sal']<50000:
          mydict.update({'sal':88000})
          print(x,mydict[x])
print(mydict)


child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}


myfamily["child2"]["name"] = "baburao"

for i in myfamily:
    print(i,myfamily[i])
# {'the': 3, 'quick': 1, 'brown': 1, 'fox': 2, 'jumps': 1, 'over': 1, 'lazy': 1, 'dog': 1}
"""
v = "the quick brown fox jumps over the lazy dog the fox"
dictt = dict()
for i in v.split():
    dictt[i] = v.count(i)
print(dictt)
"""

"""
ii ={'a': 1, 'b': 2, 'c': 3}
# Output: {1: 'a', 2: 'b', 3: 'c'}
iii = {}
for i in ii:
    iii[ii[i]] = i
print(ii)
print(iii)

ii = "programminggg"
# {'character': 'g', 'frequency': 2}
dictt = {}
l = []
for i in ii:
     dictt[i] = ii.count(i)
print(dictt)

print(max(dictt),dictt[max(dictt)])


print(max(dictt.keys(),key=dictt.get))
print(max(dictt.values()))

"""
""""""
"""
dict1 = {'a': 10, 'b': 20, 'c': 30,'e':44}
dict2 = {'b': 15, 'c': 25, 'd': 40,'e':69}
output = {}


def dictt(dict1, dict2, dict3):
    for i in dict1:
        if i in dict2:
            print(i, dict2[i] + dict1[i])
            dict3[i] = dict2[i] + dict1[i]
        elif i not in dict3:
            dict3[i] = dict1[i]


    for i in dict2:
       if i in dict1:
          print(i, dict2[i] + dict1[i])
          dict3[i] = dict2[i] + dict1[i]
       elif i not in dict3:
          dict3[i] = dict2[i]

dictt(dict1,dict2,output)

print(output)
"""

"""

data = {
    'classA': {'name': 'Alice', 'age': 24},
    'classB': {'name': 'Bob', 'age': 27},
    'classC': {'name': 'Charlie', 'age': 22},
}

for i in data:
    print(data[i]["name"])"""



