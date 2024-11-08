"""We have two lists with equal or different size.

 # ex. l1=[1,3,5,7]  l2=[1,4,5]
 # task:
 # create list that will store such values
 list_target = [(1,1), (3,4), (5,5), (7,0)]
 # zero (0) is our default value that we set if no such
 element by index was found in certain list.
 # code should work and vise versa # ex. l1=[1,4,5] l2=[1,3,5,7]
input data should produce
list_target = [(1,1), (4,3), (5,5), (0,7)]
# your solution should include comprehension constructions
# # Advices:
# set of (list1 indexes union list2 indexes) could be
helpful to get larger indexes scope ( or use if-else)
# dict as you remember has default value if
key was not found d1.get(key, 0) l1 = [2, 4, 6, 8, 10] l2 = [1, 2, 3]
"""

l1 = [2, 4, 6, 8, 10]

l2 = [1, 2, 3]

"""lists to dictionaries."""

dictionary1 = {i: l1[i] for i in range(len(l1))}

dictionary2 = {i: l2[i] for i in range(len(l2))}

""" Union of the indices."""

union_all = set(dictionary1.keys()).union(dictionary2.keys())

"""list comprehension for target list """

total = [(dictionary1.get(i, 0),
          dictionary2.get(i, 0)) for i in sorted(union_all)]

print(total)
