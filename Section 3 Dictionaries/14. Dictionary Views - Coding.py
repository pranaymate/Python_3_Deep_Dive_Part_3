print('#' * 52 + ' ### Views: keys, values and items  ')

s1 = {1, 2, 3}
s2 = {2, 3, 4}

print('#' * 52 + ' Unions:  ')

print(s1 | s2)

print('#' * 52 + ' Intersections: ')

print(s1 & s2)

print('#' * 52 + '  Differences: ')

print(s1 - s2)
s2 - s1

print('#' * 52 + '  ')

d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'c': 30, 'd': 4, 'e': 5}

for key in d1:
    print(key)

for key in d1.keys():
    print(key)

print('#' * 52 + ' We can iterate over just the values of the dictionary: ')

for value in d1.values():
    print(value)

print('#' * 52 + ' and over the items, as tuples, of the dictionary:  ')

for item in d1.items():
    print(item)

print('#' * 52 + ' We can also unpack the tuples directly while iterating: ')

for k, v in d1.items():
    print(k, v)

print('#' * 52 + ' These views are iterables, not just iterators:  ')

keys = d1.keys()
print(list(keys))
print(list(keys))

print('#' * 52 + ' The order in which keys, value and items are returned during iteration match - as long'
                 ' as the dictionary has not changed in-between. ')

print(list(d1.items()) == list(zip(d1.keys(), d1.values())))
print(keys)
d1['z'] = 10
print(keys)
del d1['z']
print(keys)

print('#' * 52 + ' Now, the interesting thing is that some of these views also exhibit set behaviors. ')

print(d1)
print(d2)

print('#' * 52 + ' We can find all the keys that are in both `d1` and `d2`: ')

print(type(d1.keys()), d1.keys())
print(type(d2.keys()), d2.keys())
union = d1.keys() | d2.keys()
print(type(union), union)

print('#' * 52 + ' We can also find the keys that are in both `d1` and `d2`:  ')

print(d1.keys() & d2.keys())

print('#' * 52 + ' We can also find the keys that are only in `d1` but not in `d2`: ')

print(d1.keys() - d2.keys())

print('#' * 52 + ' The same works with items as well: ')

print(d1.items() | d2.items())

print('#' * 52 + '  ')
d3 = {'a': [1, 2], 'b': [3, 4]}
d4 = {'b': [30, 40], 'c': [5, 6]}
print(d3.values())
print(d3)
print(d4)

print('#' * 52 + ' But thats not always the case. Lets go back to our first example: ')

print(d1)
print(d2)
print(d1.items() | d2.items())

print('#' * 52 + '  ')
d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'b': 2, 'c': 30, 'd': 4}
k1 = d1.keys()
k2 = d2.keys()
print(k1 & k2)

print('#' * 52 + ' So we have now identified the common keys, all thats left to do is build a dictionary from those'
                 ' keys and the corresponding values.  ')
print('#' * 52 + ' We can use a simple loop to do this: ')

new_dict = {}
for key in d1.keys() & d2.keys():
    new_dict[key] = (d1[key], d2[key])
print(new_dict)

print('#' * 52 + ' But, a dictionary comprehension would be a better approach here: ')

new_dict = {key: (d1[key], d2[key]) for key in d1.keys() & d2.keys()}
print(new_dict)

print('#' * 52 + '  ')
d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'b': 2, 'c': 30, 'd': 4}
new_dict = {key: d2[key] for key in d1.keys() & d2.keys()}
print(new_dict)

print('#' * 52 + '  ')
d1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
d2 = {'a': 10, 'b': 20, 'c': 30, 'e': 5}
print({'d': 4, 'e': 5})

print('#' * 52 + ' Start with the union of the keys - this identifies all unique keys in both dictionaries:  ')

union = d1.keys() | d2.keys()
print(union)

print('#' * 52 + ' Next, we look at the intersection of the keys-this identifies all keys common to both dictionaries:')

intersection = d1.keys() & d2.keys()
print(intersection)

print('#' * 52 + ' Finally, we can remove the keys in the intersection from the kesy in the union:  ')

keys = union - intersection
print(keys)

value = d1.get('e')
print(value)

value = d2.get('e')
print(value)

print('#' * 52 + ' So, we can combine these two expressions with an or to get the non-`None`'
                 ' value (one of them always will be `None`): ')

print(d1.get('d') or d2.get('d'))
print(d1.get('e') or d2.get('e'))

print('#' * 52 + ' So now we need to use this to gather up the values for our keys and create a result dictionary: ')
print('#' * 52 + ' We could do it using a standard loop: ')

d1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
d2 = {'a': 10, 'b': 20, 'c': 30, 'e': 5}
union = d1.keys() | d2.keys()
intersection = d1.keys() & d2.keys()
keys = union - intersection

result = {}
for key in keys:
    result[key] = d1.get(key) or d2.get(key)
print(result)

print('#' * 52 + ' Or, better yet, we could use a dictionary comprehension:  ')
result = {key: d1.get(key) or d2.get(key) for key in keys}
print(result)

print('#' * 52 + ' Just for completeness, and again, we will cover this in detail later, we can use the symmetric'
                 ' difference operator for sets (`^`) which does in one operation the same thing we did with the union,'
                 ' intersection, and difference operators, making this even more concise: ')

d1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
d2 = {'a': 10, 'b': 20, 'c': 30, 'e': 5}
result = {key: d1.get(key) or d2.get(key)
         for key in d1.keys() ^ d2.keys()}
print(result)

