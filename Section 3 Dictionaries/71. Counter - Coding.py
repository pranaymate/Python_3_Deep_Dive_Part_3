print('#' * 52 + '  ')
from collections import defaultdict, Counter

sentence = 'the quick brown fox jumps over the lazy dog'
counter = defaultdict(int)

for c in sentence:
    counter[c] += 1

print('#' * 52 + ' We can do the same thing using a `Counter` - unlike the `defaultdict`'
                 ' we dont specify a default factory - its always zero (its a counter after all):  ')

counter = Counter()
for c in sentence:
    counter[c] += 1

print(counter)

print('#' * 52 + ' #### Constructor ')
print('#' * 52 + ' It is so common to create a frequency distribution of elements in an iterable,'
                 ' that this is supported automatically: ')

c1 = Counter('able was I ere I saw elba')
print(c1)

print('#' * 52 + ' Of course this works for iterables in general, not just strings: ')

import random

random.seed(0)
my_list = [random.randint(0, 10) for _ in range(1_000)]
c2 = Counter(my_list)
print(c)

print('#' * 52 + ' We can also initialize a `Counter` object by passing in keyword arguments, or even a dictionary:  ')

c2 = Counter(a=1, b=10)
print(c2)

c3 = Counter({'a': 1, 'b': 10})
print(c3)

print('#' * 52 + ' #### Finding the n most Common Elements  ')

import re

sentence = '''
his module implements pseudo-random number generators for various distributions.
For integers, there is uniform selection from a range. For sequences, there is uniform selection of a random element,
a function to generate a random permutation of a list in-place, and a function for random sampling without replacement.
On the real line, there are functions to compute uniform, normal (Gaussian), lognormal, negative exponential, gamma,
and beta distributions. For generating distributions of angles, the von Mises distribution is available.
Almost all module functions depend on the basic function random(), which generates a random float uniformly in
the semi-open range [0.0, 1.0). Python uses the Mersenne Twister as the core generator. It produces 53-bit precision
floats and has a period of 2**19937-1. The underlying implementation in C is both fast and threadsafe. 
The Mersenne Twister is one of the most extensively tested random number generators in existence. 
However, being completely deterministic, it is not suitable for all purposes, and is completely unsuitable 
for cryptographic purposes.'''

words = re.split('\W', sentence)
print(words)

print('#' * 52 + ' But what are the frequencies of each word, and what are the 5 most frequent words? ')

word_count = Counter(words)
print(word_count)
print(word_count.most_common(5))

print('#' * 52 + ' #### Using Repeated Iteration  ')

c1 = Counter('abba')
print(c1)

for c in c1:
    print(c)

print('#' * 52 + ' However, we can have an iteration'
                 ' that repeats the counter keys as many times as the indicated frequency:  ')

for c in c1.elements():
    print(c)

print('#' * 52 + '  ')

l = []
for i in range(1, 11):
    for _ in range(i):
        l.append(i)
print(l)

print('#' * 52 + ' But we could use a `Counter` object as well:  ')

c1 = Counter()
for i in range(1, 11):
    c1[i] = i

print(c1)
print(c1.elements())

print('#' * 52 + ' And we can iterate through that `chain` quite easily:  ')

for i in c1.elements():
    print(i, end=', ')

print('#' * 52 + '  Just for fun, how could we reproduce this functionality using a plain dictionary? ')


class RepeatIterable:
    def __init__(self, **kwargs):
        self.d = kwargs

    def __setitem__(self, key, value):
        self.d[key] = value

    def __getitem__(self, key):
        self.d[key] = self.d.get(key, 0)
        return self.d[key]

r = RepeatIterable(x=10, y=20)
print(r.d)
r['a'] = 100
print(r['a'])
print(r['b'])
print(r.d)

print('#' * 52 + ' Now we have to implement that `elements` iterator: ')


class RepeatIterable:
    def __init__(self, **kwargs):
        self.d = kwargs

    def __setitem__(self, key, value):
        self.d[key] = value

    def __getitem__(self, key):
        self.d[key] = self.d.get(key, 0)
        return self.d[key]

    def elements(self):
        for k, frequency in self.d.items():
            for i in range(frequency):
                yield k

r = RepeatIterable(a=2, b=3, c=1)

for e in r.elements():
    print(e, end=', ')

print('#' * 52 + ' Lastly lets see how we can update a `Counter` object using another `Counter` object.  ')
print('#' * 52 + ' When both objects have the same key, we have a choice - do we add the count of one'
                 ' to the count of the other, or do we subtract them? ')
print('#' * 52 + ' We can do either, by using the `update` (additive) or `subtract` methods.  ')

c1 = Counter(a=1, b=2, c=3)
c2 = Counter(b=1, c=2, d=3)

c1.update(c2)
print(c1)

print('#' * 52 + ' On the other hand we can subtract instead of add counters: ')

c1 = Counter(a=1, b=2, c=3)
c2 = Counter(b=1, c=2, d=3)

c1.subtract(c2)
print(c1)

print('#' * 52 + ' Just as the constructor for a `Counter` can take different arguments, so too can the `update` and'
                 ' `subtract` methods.  ')

c1 = Counter('aabbccddee')
print(c1)
c1.update('abcdef')
print(c1)

print('#' * 52 + ' #### Mathematical Operations  ')

c1 = Counter('aabbcc')
c2 = Counter('abc')
c1 + c2

print(c1 - c2)

c1 = Counter(a=5, b=1)
c2 = Counter(a=1, b=10)

print(c1 & c2)

print(c1 | c2)

print('#' * 52 + ' The **unary** `+` can also be used to remove any non-positive count from the Counter: ')

c1 = Counter(a=10, b=-10)
print(+c1)

print('#' * 52 + ' The **unary** `-` changes the sign of each counter, and removes any non-positive result:  ')

print(-c1)

print('#' * 52 + ' ##### Example ')

import random
random.seed(0)

widgets = ['battery', 'charger', 'cable', 'case', 'keyboard', 'mouse']

orders = [(random.choice(widgets), random.randint(1, 5)) for _ in range(100)]
refunds = [(random.choice(widgets), random.randint(1, 3)) for _ in range(20)]

print(orders)
print(refunds)

print('#' * 52 + ' Lets first load these up into counter objects.  ')
print('#' * 52 + ' To do this we are going to iterate through the various lists and update our counters: ')

sold_counter = Counter()
refund_counter = Counter()

for order in orders:
    sold_counter[order[0]] += order[1]

for refund in refunds:
    refund_counter[refund[0]] += refund[1]

print(sold_counter)
print(refund_counter)

net_counter = sold_counter - refund_counter

print(net_counter)
print(net_counter.most_common(3))

print('#' * 52 + ' We could actually do this a little differently, not using loops to populate our initial counters. ')
print('#' * 52 + ' Recall the `repeat()` function in `itertools`: ')

from itertools import repeat
print(list(repeat('battery', 5)))
print(orders[0])
print(list(repeat(*orders[0])))

print('#' * 52 + ' So we could use the `repeat()` method to essentially repeat each widget for each item of `orders`. ')
print('#' * 52 + ' We need to chain this up for each element of `orders` - this will give us a single iterable'
                 ' that we can then use in the constructor for a `Counter` object. ')
print('#' * 52 + ' We can do this using a generator expression for example: ')

from itertools import chain

print(list(chain.from_iterable(repeat(*order) for order in orders)))

order_counter = Counter(chain.from_iterable(repeat(*order) for order in orders))
print(order_counter)

print('#' * 52 + ' What if we dont want to use a `Counter` object. We can still do it (relatively easily) as follows: ')

net_sales = {}
for order in orders:
    key = order[0]
    cnt = order[1]
    net_sales[key] = net_sales.get(key, 0) + cnt

for refund in refunds:
    key = refund[0]
    cnt = refund[1]
    net_sales[key] = net_sales.get(key, 0) - cnt

# eliminate non-positive values (to mimic what - does for Counters)
net_sales = {k: v for k, v in net_sales.items() if v > 0}

# we now have to sort the dictionary
# this means sorting the keys based on the values
sorted_net_sales = sorted(net_sales.items(), key=lambda t: t[1], reverse=True)

# Top three
print(sorted_net_sales[:3])

