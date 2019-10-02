print('#' * 52 + '  ')

d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d3 = {'e': 5, 'f': 6}

d = {**d1, **d2, **d3}

print(d)

print('#' * 52 + ' or ')

d = {}
d.update(d1)
d.update(d2)
d.update(d3)
print(d)

print('#' * 52 + ' But in a way this is wasteful because we had to copy the data into a new dictionary. ')
print('#' * 52 + ' Instead we can use `ChainMap`:  ')

from collections import ChainMap

d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d3 = {'e': 5, 'f': 6}
d = ChainMap(d1, d2, d3)

print(d)
print(isinstance(d, dict))
print(d['a'])
print(d['c'])
for k, v in d.items():
    print(k, v)

print('#' * 52 + '  Now what happens if we have key collisions? ')

d1 = {'a': 1, 'b': 2}
d2 = {'b': 20, 'c': 3}
d3 = {'c': 30, 'd': 4}

d = ChainMap(d1, d2, d3)

print(d['b'])
print(d['c'])

for k, v in d.items():
    print(k, v)

print('#' * 52 + ' Now lets look at how ChainMap objects handle inserts, deletes and updates: ')

d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d3 = {'e': 5, 'f': 6}
d = ChainMap(d1, d2, d3)

d['z'] = 100
print(d)

print('#' * 52 + ' As you can see the element z: 100` was added to the chain map. '
                 ' But what about the underlying dictionaries that make up the map?  ')

print(d1)
print(d2)
print(d3)

print('#' * 52 + ' Lets try to update `c`, which is in the second dictionary: ')

d['c'] = 300
print(d)

print('#' * 52 + ' As you can see the **first** dictionary in the chain was "updated" - since the key did not exist,'
                 ' the key with the "updated" value was added to the underlying dictionary: ')

print(d1)
print(d2)
print(d3)

print('#' * 52 + ' What about deleting an item?  ')

d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d3 = {'e': 5, 'f': 6}
d = ChainMap(d1, d2, d3)

del d['a']

print(list(d.items()))

print(d1)
print(d2)
print(d3)

print('#' * 52 + ' Something important to note here when deleting keys,'
                 ' is that deleting a key does not guarantee the key no longer exists in the chain!'
                 ' It could exist in one of the parents, and only the child is affected:  ')

d1 = {'a': 1, 'b': 2}
d2 = {'a': 100}
d = ChainMap(d1, d2)

print(d['a'])
del d['a']
print(d['a'])

print('#' * 52 + ' Since we can only mutate the **first** dict in the chain,'
                 ' trying to delete an item that is present in the chain, '
                 ' but not in the child will cause an exception: ')

# del d['c']  # KeyError: 'c'

print('#' * 52 + ' A `ChainMap` is built as a view on top of a sequence of mappings,'
                 ' and those maps are incorporated **by reference**.  ')
print('#' * 52 + ' This means that if an underlying map is mutated,'
                 ' then the `ChainMap` instance will **see** the change: ')

d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d3 = {'e': 5, 'f': 6}
d = ChainMap(d1, d2, d3)

print(list(d.items()))
d3['g'] = 7
print(list(d.items()))

print('#' * 52 + ' We can even chain ChainMaps. ')
print('#' * 52 + ' For example, we can use this approach to "append" a new dictionary to a chain map,'
                 ' in essence create a **new** chain map containing the maps from one chain map and'
                 ' adding one or more maps to the list: ')

d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d = ChainMap(d1, d2)

d3 = {'d':400, 'e': 5 }
d = ChainMap(d, d3)

print(d)

print('#' * 52 + ' Of course, we could place `d3` in front: ')

d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d = ChainMap(d1, d2)

d3 = {'d':400, 'e': 5 }
d = ChainMap(d3, d)
print(d)

print('#' * 52 + ' Instead of adding an element to the beginning of the chain list using the technique above,'
                 ' we can also use the `new_child` method, which returns a new chain map with the new element'
                 ' added to the beginning of the list: ')

d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d = ChainMap(d1, d2)

d3 = {'d':400, 'e': 5 }
d = d.new_child(d3)
print(d)

print('#' * 52 + ' There is also a property that can be used'
                 ' to return every map in the chain **except** the first map:  ')

d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d3 = {'e': 5, 'f': 6}
d = ChainMap(d1, d2, d3)
print(d)

d = d.parents
print(d)

print('#' * 52 + ' The chain map is list of maps is accessible via the `maps` property:  ')

d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d = ChainMap(d1, d2)

print(type(d.maps), d.maps)

print('#' * 52 + ' As you can see this is a list, and so we can actually manipulate it as we would any list:  ')

d3 = {'e': 5, 'f': 6}
d.maps.append(d3)
print(d.maps)

print('#' * 52 + ' We could equally well remove a map from the list entirely, insert one wherever we want, etc:  ')

d.maps.insert(0, {'a': 100})
print(d.maps)
print(list(d.items()))

print('#' * 52 + ' As you can see `a` now has a value of `100` in the chain map.  ')
print('#' * 52 + ' We can also delete a map from the chain entirely: ')

del d.maps[1]
print(d.maps)

print('#' * 52 + ' ##### Example  ')

config = {
    'host': 'prod.deepdive.com',
    'port': 5432,
    'database': 'deepdive',
    'user_id': '$pg_user',
    'user_pwd': '$pg_pwd'
}

local_config = ChainMap({}, config)
print(list(local_config.items()))

print('#' * 52 + ' And we can make changes to `local_config`: ')

local_config['user_id'] = 'test'
local_config['user_pwd'] = 'test'

print(list(local_config.items()))

print('#' * 52 + ' But notice that our original dictionary is unaffected: ')

print(list(config.items()))

print('#' * 52 + ' That is because the changes we made were reflected in the **first**'
                 ' dictionary in the chain - that empty dictionary: ')

print(local_config.maps)

