print('#' * 52 + '  Size')

s = {1, 2, 3}
print(len(s))

print('#' * 52 + '  Membership Testing')
s = {1, 2, 3}
print(1 in s)
print(10 in s)
print(1 not in s)
print(10 not in s)

# But let's go a little further and consider how membership testing works with sets.
# As I mentioned in earlier lectures, sets are hash tables, and membership testing is extremely efficient for sets,
# since it's simply a hash table lookup - as opposed to scanning a list for example,
# until we find the requested element (or not).
#
# Let's do some quick timings to verify this, as well as compare lookup speeds for sets and dictionaries as well
# (which are also, after all, hash tables).
print()
from timeit import timeit

n = 100_000
s = {i for i in range(n)}
l = [i for i in range(n)]
d = {i: None for i in range(n)}

number = 1_000_000
search = 9
t_list = timeit(f'{search} in l', globals=globals(), number=number)
t_set = timeit(f'{search} in s', globals=globals(), number=number)
t_dict = timeit(f'{search} in d', globals=globals(), number=number)
print('list:', t_list)
print('set:', t_set)
print('dict:', t_dict)

print('#' * 52 + '  The story changes even more if we test for example the last element of the list. '
                 '  I am definitely not to run the tests 1_000_000 times - not unless we want to make this video '
                 '  reaaaaaaly long!')

number = 3_000
search = 99_999
t_list = timeit(f'{search} in l', globals=globals(), number=number)
t_set = timeit(f'{search} in s', globals=globals(), number=number)
t_dict = timeit(f'{search} in d', globals=globals(), number=number)
print('list:', t_list)
print('set:', t_set)
print('dict:', t_dict)

print('#' * 52 + '  The situation for not in is the same:')

number = 3_000
search = -1
t_list = timeit(f'{search} not in l', globals=globals(), number=number)
t_set = timeit(f'{search} not in s', globals=globals(), number=number)
t_dict = timeit(f'{search} not in d', globals=globals(), number=number)
print('list:', t_list)
print('set:', t_set)
print('dict:', t_dict)

print('#' * 52 + '  But this efficiency does come at the cost of memory:')

print(d.__sizeof__())
print(s.__sizeof__())
print(l.__sizeof__())

print('#' * 52 + ' Even for empty objects: ')

s = set()
d = dict()
l = list()
print(d.__sizeof__())
print(s.__sizeof__())
print(l.__sizeof__())

print('#' * 52 + '  And adding just one element to each object:')
s.add(10)
d[10] =None
l.append(10)

print(d.__sizeof__())
print(s.__sizeof__())
print(l.__sizeof__())

print('#' * 52 + '  Adding Elements')
s = {30, 20, 10}
s.add(15)
print(s)

print('#' * 52 + '  Dont be fooled by the apparent ordering of the elements here. '
                 '  This is the same as with dictionaries - Jupyter tries to represent things nicely for us, '
                 '  but underneath the scenes:')

print(s)
s.add(-1)
print(s)

print('#' * 52 + ' And the order just changed again! :-)')
print('#' * 52 + ' What is interesting about the add() method, is that if we try to add an element that already exists,'
                 ' Python will simply ignore it:')

print(s)
s.add(15)
print(s)

print('#' * 52 + '  Now that we know how to add an element to a set, lets go back and see how the set, '
                 '  dictionary and list resize as we add more elements to them. '
                 '  We should expect the list to be more efficient from a memory standpoint:')


l = list()
s = set()
d = dict()

print('#', 'dict', 'set', 'list')
for i in range(50):
    print(i, d.__sizeof__(), s.__sizeof__(), l.__sizeof__())
    l.append(i)
    s.add(i)
    d[i] = None

print('#' * 52 + '  As you can see, the memory costs for a set or a dict are definitely higher than for a list. '
                 '  You can also see from this how it looks like CPython implements different resizing '
                 '  strategies for sets, dicts and lists. The strategy by the way has nothing to do with the size of '
                 '  the elements we put in those objects:')

l = list()
s = set()
d = dict()

print('#', 'dict', 'set', 'list')
for i in range(50):
    print(i, d.__sizeof__(), s.__sizeof__(), l.__sizeof__())
    l.append(i**1000)
    s.add(i*1000)
    d[i*1000] = None

print('#' * 52 + '  Removing Elements')
s = {1, 2, 3}
s.remove(1)
print(s)
# s.remove(10) # ERROR  # KeyError: 10

print('#' * 52 + '  As you can see, we get an exception.')
print('#' * 52 + '  If we dont want the exception we can do it this way:')
s.discard(10)
print(s)

print('#' * 52 + '  We can also remove (and return) an arbitrary element from the set:')
s = set('python')
print(s)
s.pop()

print('#' * 52 + '  Note that we do not know ahead of time what element will get popped.')
print('#' * 52 + '  Also, popping an empty set will result in a KeyError exception:')

s = set()
# s.pop() # ERROR KeyError: 'pop from an empty set'

# Something like that might be handy to handle all the elements of a set one at a time without caring
# for the order in which elements are removed from the set - not that you can, anyway - sets are not ordered!
# But this way you can get at the elements of a set without knowing the content of the set
# (since you need to know the element you are removing with remove and discard.)

print('#' * 52 + '  Finally, you can empty out a set by calling the clear method:')

s = {1, 2, 3}
s.clear()
print(s)

