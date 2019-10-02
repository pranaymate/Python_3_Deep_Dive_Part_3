print('#' * 52 + '  ')

from collections import OrderedDict

print('#' * 52 + ' #### Reverse Iteration ')

d1 = OrderedDict(a=1, b=2, c=3, d=4)
d2 = dict(a=1, b=2, c=3, d=4)

print(d1)
print(d2)

for k in reversed(d1):
    print(k)

print('#' * 52 + ' For now, it can be done but it means making a list out of the keys,'
                 ' and then iterating through the reversed list:  ')

for k in reversed(list(d2.keys())):
    print(k)

print('#' * 52 + ' #### Popping Items  ')
print('#' * 52 + ' Getting the first key is not difficult -'
                 ' we simply retrieve the first key from the keys() view for example:  ')

first_key = next(iter(d2.keys()))
print(d2)
print(first_key)



print('#' * 52 + ' Fiding the last key is a bit more challenging, but fortunately,'
                 ' we can just use the `popitem` method on plain dictionaries that'
                 ' is guaranteed to pop the last insert item - again, this is a guarantee'
                 ' only in Python 3.7 and above: ')

d1 = OrderedDict(a=1, b=2, c=3, d=4)
d2 = dict(a=1, b=2, c=3, d=4)

print(d2)
print(d2.popitem())
print(d2)

print('#' * 52 + '  So we could combine these into a custom function as follows: ')

def popitem(d, last=True):
    if last:
        return d.popitem()
    else:
        first_key = next(iter(d.keys()))
        return first_key, d.pop(first_key)

d2 = dict(a=1, b=2, c=3, d=4)
print(d2)
print(popitem(d2))
print(d2)

d2 = dict(a=1, b=2, c=3, d=4)
print(d2)
print(popitem(d2, last=False))
print(d2)

print('#' * 52 + ' #### Move to End  ')

d2 = dict(a=1, b=2, c=3, d=4)
print(d2)
key = 'b'
d2[key] = d2.pop(key)
print(d2)

print('#' * 52 + '  ')

d = dict(a=1, b=2, c=3, d=4, e=5, f=6)
key = 'c'

print(d.keys())

# first move desired key to end
d[key] = d.pop(key)
print(d.keys())

keys = list(d.keys())[:-1]
for key in keys:
    d[key] = d.pop(key)
    print(d.keys())

print(d)

print('#' * 52 + ' We can combine both into a single function:  ')


def move_to_end(d, key, *, last=True):
    d[key] = d.pop(key)

    if not last:
        for key in list(d.keys())[:-1]:
            d[key] = d.pop(key)

d = dict(a=1, b=2, c=3, d=4, e=5, f=6)
move_to_end(d, 'c')
print(d)

move_to_end(d, 'c', last=False)
print(d)

print('#' * 52 + ' #### Equality Comparison  ')

d1 = {'a': 10, 'b': 20, 'c': 30}
d2 = {'b': 20, 'c': 30, 'a': 10}

print(d1 == d2)
print(d1.keys() == d2.keys())
print(list(d1.keys()) == list(d2.keys()))
print(d1 == d2 and list(d1.keys()) == list(d2.keys()))

def dict_equal_sensitive(d1, d2):
    if d1 == d2:
        for k1, k2 in zip(d1.keys(), d2.keys()):
            if k1 != k2:
                return False
        return True
    else:
        return False

print(dict_equal_sensitive(d1, d2))
print(dict_equal_sensitive(d1, d1))

print('#' * 52 + ' If you want a pure functional programming approach that does not use a loop,'
                 ' we can do it this way too, using `all` and `map`:  ')

def dict_equal_sensitive(d1, d2):
    if d1 == d2:
        return all(map(lambda el: el[0] == el[1],
                       zip(d1.keys(), d2.keys())
                      )
                  )
    else:
        return False

print(dict_equal_sensitive(d1, d2))

print('#' * 52 + ' Lets look at a few timings to see the performance difference between plain `dicts` and `OrderedDicts ')

from timeit import timeit

def create_dict(n=100):
    d = dict()
    for i in range(n):
        d[i] = i
    return d

def create_ordered_dict(n=100):
    d = OrderedDict()
    for i in range(n):
        d[i] = i
    return d

print(timeit('create_dict(10_000)', globals=globals(), number=1_000))
print(timeit('create_ordered_dict(10_000)', globals=globals(), number=1_000))


print('#' * 52 + ' As you can see, creating an OrderedDict has slightly more overhead. ')
print('#' * 52 + ' Lets see if recovering a key from an `OrderedDict` is slower than a plain `dict`: ')

d1 = create_dict(10_000)
d2 = create_ordered_dict(10_000)

print(timeit('d1[9_999]', globals=globals(), number=100_000))

n = 1_000_000
d1 = create_dict(n)
print(timeit('d1.popitem()', globals=globals(), number=n))

n = 1_000_000
d2 = create_ordered_dict(n)
print(timeit('d2.popitem(last=True)', globals=globals(), number=n))

n = 100_000
d1 = create_dict(n)
print(timeit('popitem(d1, last=False)', globals=globals(), number=n))

n = 100_000
d2 = create_ordered_dict(n)
print(timeit('d2.popitem(last=False)', globals=globals(), number=n))

