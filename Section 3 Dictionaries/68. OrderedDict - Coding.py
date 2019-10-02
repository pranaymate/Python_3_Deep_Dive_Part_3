print('#' * 52 + '  ')
from collections import OrderedDict

d = OrderedDict()
d['z'] = 'hello'
d['y'] = 'world'
d['a'] = 'python'
print(d)

print('#' * 52 + ' And if we iterate through the keys of the `OrderedDict` we will retain that key order as well: ')

for key in d:
    print(key)

print('#' * 52 + '  The `OrderedDict` also supports reverse iteration using `reversed()`: ')

for key in reversed(d):
    print(key)

print('#' * 52 + '  ')

d = OrderedDict()
d['first'] = 10
d['second'] = 20
d['third'] = 30
d['last'] = 40

print(d)
print(d.popitem())
print(d)

print('#' * 52 + ' As you can see the last item was popped off (and returned as a key/value tuple). ')
print('#' * 52 + ' To pop the first item we can do this:  ')

print(d.popitem(last=False))
print(d)

print('#' * 52 + ' The `move_to_end` method simply moves the specified key to the end (by default),'
                 ' or to the beginning (if `last=False` is specified) of the dictionary:  ')

d = OrderedDict()
d['first'] = 10
d['second'] = 20
d['third'] = 30
d['last'] = 40

d.move_to_end('second')
print(d)

d.move_to_end('third', last=False)
print(d)

print('#' * 52 + ' Be careful if you specify a non-existent key, you will get an exception:  ')

# d.move_to_end('x')  KeyError: 'x'

print('#' * 52 + '  Equality Comparisons ')

d1 = {'a': 10, 'b': 20}
d2 = {'b': 20, 'a': 10}

print(d1 == d2)

print('#' * 52 + ' But this is not the case with `OrderedDicts` - since ordering matters here,'
                 ' two `OrderedDicts` will compare equal if both their key/values pairs are equal **and**'
                 ' if the keys are in the same order: ')

d1 = OrderedDict()
d1['a'] = 10
d1['b'] = 20

d2 = OrderedDict()
d2['a'] = 10
d2['b'] = 20

d3 = OrderedDict()
d3['b'] = 20
d3['a'] = 10


print(d1)
print(d2)
print(d3)

print(d1 == d2)
print(d1 == d3)

print('#' * 52 + ' Now, an `OrderedDict` is a subclass of a standard `dict`:  ')

print(isinstance(d1, OrderedDict))
print(isinstance(d1, dict))

print('#' * 52 + ' So, can we compare an `OrderedDict` with a plain `dict`?  ')
print('#' * 52 + ' The answer is yes, and in this case order does **not** matter:  ')

d1 = OrderedDict()
d1['a'] = 10
d1['b'] = 20

d2 = {'b': 20, 'a': 10}

print(d1)
print(d2)

print(d1 == d2)
print(d2 == d1)

print('#' * 52 + ' Using an OrderedDict as a Stack or Queue  ')

from timeit import timeit
from collections import deque

def create_ordereddict(n=100):
    d = OrderedDict()
    for i in range(n):
        d[str(i)] = i
    return d

def create_deque(n=100):
    return deque(range(n))

def pop_all_ordered_dict(n=1000, last=True):
    d = create_ordereddict(n)
    while True:
        try:
            d.popitem(last=last)
        except KeyError:
            # done popping
            break

def pop_all_deque(n=1000, last=True):
    dq = create_deque(n)
    if last:
        pop = dq.pop
    else:
        pop = dq.popleft

    while True:
        try:
            pop()
        except IndexError:
            break


print('#' * 52 + '  Now lets go ahead and time these operations, both the creations and the pops: ')

print(timeit('create_ordereddict(10_000)',
       globals=globals(),
       number=1_000))

print(timeit('create_deque(10_000)',
       globals=globals(),
       number=1_000))

print('#' * 52 + ' Now lets time popping elements - keep in mind that we are also timing the recreation'
                 ' of the data structures every time as well - so our timings are going to be biased because of that. ')
print('#' * 52 + ' A very rough way of rectifying that will be to subtract how much time we measured above'
                 ' for creating the structures by themselves: ')

n = 10_000
number = 1_000

results = dict()

results['dict_create'] = timeit('create_ordereddict(n)',
                                globals=globals(),
                                number=number)

results['deque_create'] = timeit('create_deque(n)',
                                 globals=globals(),
                                 number=number)

results['dict_create_pop_last'] = timeit(
    'pop_all_ordered_dict(n, last=True)',
    globals=globals(), number=number)

results['dict_create_pop_first'] = timeit(
    'pop_all_ordered_dict(n, last=False)',
    globals=globals(), number=number)

results['deque_create_pop_last'] = timeit(
    'pop_all_deque(n, last=True)',
    globals=globals(), number=number
)

results['deque_create_pop_first'] = timeit(
    'pop_all_deque(n, last=False)',
    globals=globals(), number=number
)

results['dict_pop_last'] = (
    results['dict_create_pop_last'] - results['dict_create'])

results['dict_pop_first'] = (
    results['dict_create_pop_first'] - results['dict_create'])

results['deque_pop_last'] = (
    results['deque_create_pop_last'] - results['deque_create'])

results['deque_pop_first'] = (
    results['deque_create_pop_first'] - results['deque_create'])

for key, result in results.items():
    print(f'{key}: {result}')



print('#' * 52 + '  ')
print('#' * 52 + '  ')
print('#' * 52 + '  ')
print('#' * 52 + '  ')
print('#' * 52 + '  ')

print('#' * 52 + '  ')
print('#' * 52 + '  ')
print('#' * 52 + '  ')
print('#' * 52 + '  ')
print('#' * 52 + '  ')
print('#' * 52 + '  ')
print('#' * 52 + '  ')
print('#' * 52 + '  ')
print('#' * 52 + '  ')
print('#' * 52 + '  ')
print('#' * 52 + '  ')

print('#' * 52 + '  ')
print('#' * 52 + '  ')
print('#' * 52 + '  ')
print('#' * 52 + '  ')
print('#' * 52 + '  ')
print('#' * 52 + '  ')
print('#' * 52 + '  ')
print('#' * 52 + '  ')
print('#' * 52 + '  ')
print('#' * 52 + '  ')
print('#' * 52 + '  ')

print('#' * 52 + '  ')
print('#' * 52 + '  ')
print('#' * 52 + '  ')
print('#' * 52 + '  ')
print('#' * 52 + '  ')
print('#' * 52 + '  ')
print('#' * 52 + '  ')
print('#' * 52 + '  ')
print('#' * 52 + '  ')
print('#' * 52 + '  ')
print('#' * 52 + '  ')