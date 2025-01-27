# fruits  = ["mango","Banana","apple",2025]
#
# print(fruits)
#
#
# fruits.insert(1,"kiwi")
#
# print(fruits)
#
# year = fruits.pop(-1)
#
# print(year)
#
# print(fruits)
#
# #sorting the list
#
# fruits.sort()
#
# print(fruits)
#
#
# # #if we want to sort the list according to our need or condition o we can do it
# lst = [11,54,6,3,24,22,16]
# def myfunc(n):
#     return abs(n-17)
# lst.sort(key=myfunc)
# print(lst)
# #
#
# # changing item in list
#
# # this will do the overriding
# lst[3] = 17
# print(lst)
# #
# #
# fruits[1:] = "vasu","rucchu","varusi"
#
# # fruits[2:] ="v"
# # #
# # #
# print(fruits)
# # #
# #
# # # when we use insert this will also add the item in list on our expected space or index but it dosnt
# # #override things
# # lst.insert(3,176)
# print(lst)
# #
# mylst = ["jamun","kiwi","mango","orange","banana"]
# #
# print(mylst)
# #
# mylst[1 ] =["apple","b"],"h"
# print(mylst[1][-2])
# print(mylst)
# #
# Example = [1, 2, 3, 4, 5, 6]
# # Expected
# # Output: ([2, 4, 6], [1, 3, 5])
# lst = []
# lstt = []
# for i in Example:
#     if i % 2 == 0:
#         lst.append(i)
#     else:
#         lstt.append(i)
# output = (lst, lstt)
# # print(output)
#
# # 2
# output = []
# Example2 = [[1, 2], [3, 4], [5]]
# # Expected Output: [1, 2, 3, 4, 5]
# for i in Example2:
#     for j in i:
#         output.append(j)
# # print(output)
#
# # 3
#
# Examplee = [1, 2, 1, 3, 4, 5, 1, 2]
# # Expected Output: [1, 2, 3, 4, 5]
#
# for i in Examplee:
#     if i not in output:
#         output.append(i)
# # print(output)
#
# # 4
#
# Exampleee = [1, 2, 3, 2, 1,89]
# # # Expected Output: True
# l1 = []
# l2 = []
# for i in Exampleee:
#     l1.append(i)
# print(l1)
# for j in Exampleee[::-1]:
#     l2.append(j)
# print(l2)
# # # if l1 == l2:   print("True")
#
# # 5
# Exampleeee = [2,3,4,5,6,7,8,9,10]
# # Expected Output : odd even
# l11= [i for i  in Exampleeee if i%2==0]
# l22 = [i for i in Exampleeee if i%2!=0]
# final = l11+ l22
# # print(final)
#
# # #6
# # 19. Split List into Chunks of N Size
# #
# #     Split a list into chunks of N elements.
# _16 = var = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# #     Expected Output: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# #     Methods: range(), list slicing.
#
# # print(len(_16))
#
# a= _16[:3]
# b = _16[3:6]
# c = _16[6:]
# nl = [a,b,c]
# # print(nl)
#
#
# #17
#
# _17keys = ['a', 'b', 'c']
# _17values = [1, 2, 3]
# # Expected Output: {'a': 1, 'b': 2, 'c': 3}
# dictt = {}
# for key ,value in zip(_17keys,_17values):
#     dictt[key] = value
# # print(dictt)
#
#
# #18
l = [1,2,3,2,4]
n= 2
ouu = []
# # Expected Output: [1, 3]
# # Methods: enumerate(), append().
#
for i in range(len(l)):
    if l[i] == n:
        ouu.append(i)
print(ouu)
#
# #19
#
# # 11. Convert List to a Set of Tuples
# #
# #     Convert a list of lists into a set of tuples.
# E = [[1, 2], [3, 4], [5, 6]]
#
# # Output: {(1, 2), (3, 4), (5, 6)}
# # Methods: tuple(), set().
# st = set()
# for i in range (len(E)):
#     st.add(tuple(E[i]))
# # print(st)
#
# #20
lll2 = []
lll = [1, 2, 3, 4]
# Expected Output: [1, 3, 6, 10]
# Methods: accumulate(), for loop.

for i in range(1,len(lll)+1):
    lll2.append(sum(lll[:i]))
print(lll2)
#
#
#
# # . Find the Most Frequent Element
# #
# #     Given a list, find the most frequent element. If there are ties, return any of them.
# E= [1, 2, 3, 1, 2, 1]
# lw = []
# for i in set(E):
#     lw.append(E.count(i))
# # print("most frequently occurs : ",max(lw))
#
#
# #20
# # Given two lists, return a list containing only the elements that are in both lists (intersection).
# E21,E22= [1, 2, 3, 4], [3, 4, 5, 6]
#
# # Expected Output: [3, 4]
# nll = []
# for i in E21:
#     for j in E22:
#         if i == j:
#            nll.append(i)
# # print(nll)
#
#
# # Given a list of numbers, find the longest contiguous sublist that is strictly increasing.
# sp =  [1, 2, 1, 3, 4, 5, 1, 2]
# # Expected Output: [1, 2, 3, 4, 5]
# sq = list(set(sp))
# # print(sq)
#
#
# y =  [1, 2, 3, 4, 5]
# r =2
# # Expected Output: [3, 4, 5, 1, 2]
#
#
# v = y[2:]+y[:2]
# print(v)
#
#
# lst = [2,3,4,5,6,7,8]
#
# v1 = list(map(lambda x : x//2,lst))
# v11= list(filter(lambda x : x%2==0,lst))
#
# print(v1)
#
#
#
# #list comprehension
#
# fr = ["mango","banana","apple","kiwi"]
#
# nfr = [x if x!= "banana" else "Pineapple" for x in fr]
# print(nfr)
#
#
# nfrr = [x if "a" in x else "a nahi hai" for x in fr]
# print(nfrr)
#
# nfrrr = [x.upper() for x in fr]
# print(nfrrr)
#
# s = [1,2,3,4,5,6,7,8]
# nfrrrr = [x**2 if x%2==0 else x for x in s]
#
# print(nfrrrr)
#
