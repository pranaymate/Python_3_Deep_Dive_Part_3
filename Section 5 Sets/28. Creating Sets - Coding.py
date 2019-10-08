print('#' * 52 + '  Just like dictionaries, there is a variety of ways to create sets.')

s = {'a', 100, (1,2)}
print(type(s))

print('#' * 52 + '  To create an empty set we cannot use {} since that would create an empty dictionary:')
d = {}
print(type(d))

print('#' * 52 + '  Instead, we have to use the set() function:')
s = set()
print(type(s))

print('#' * 52 + '  This brings up the second way we can create sets. We can use the set() function '
                 '  and pass it an iterable:')
s = set([1, 2, 3])
print(s)

print('#' * 52 + '  or even:')
s = set(range(10))
print(s)

# Of course we are restricted to an iterable of hashable elements only.
#
# So this would not work:

# s = set([[1,2], [3,4]]) # ERROR # unhashable type: 'list'

print('#' * 52 + '  What might surprise you is this:')
d = {'a': 1, 'b': 2}
s = set(d)

# See? No exception!
#
# But consider what happens when we iterate a dictionary:

for e in d:
    print(e)

print('#' * 52 + '  We just get the keys back! All dictionary keys are hashable, '
                 '  and therefore we can always create a set from a dictionary, but it will just contain the keys:')
print(s)

print('#' * 52 + '  Next we can use a set comprehension to create a set. It looks and works almost the same as '
                 '  a dictionary comprehension - but a set, unlike a dictionary, has no associated values. '
                 '  Here is an example:')
s = {c for c in 'python'}
print(s)

print('#' * 52 + '  Of course, we do not really need to use a comprehension here. '
                 '  Since strings are iterables of characters (which are hashable), '
                 '  we can create a set from the characters in a string as follows:')
s = set('python')
print(s)

print('#' * 52 + '  Just like we have iterable unpacking and dictionary unpacking, we also have set unpacking:')
s1 = {'a', 'b', 'c'}
s2 = {10, 20, 30}
print('#' * 52 + '  To combine both elements of these sets, we cannot do this:')
# s = {s1, s2} # ERROR unhashable type: 'set'

# This would be a set of sets - and sets are not hashable anyway (we could use a frozenset, but more about those later).
#
# What we want is to unpack the elements of the sets into something else.
#
# We could create a set containing all these elements:

s = {*s1, *s2}
print(s)

print('#' * 52 + '  What is interesting about the unpacking though, '
                 '  is that we are not restricted to just creating another set:')
l = [*s1, *s2]
print(l)

print('#' * 52 + '  or even to pass as arguments to a function - with a big caveat!')
def my_func(a, b, c):
    print(a, b, c)

args = {20, 10, 30}
print('#' * 52 + '  We cannot just pass the set directly to my_func because it expects three arguments,'
                 '  but we can unpack the set before we pass it:')
my_func(*args)

print('#' * 52 + ' Notice the order of the arguments! As we know, order of elements in a set is considered random'
                 ' (it is not of course, but for all practical purposes it might as well be).'
                 ' In some cases however, it might not matter. Consider this function:')

def averager(*args):
    total = 0
    for arg in args:
        total += arg
    return total / len(args)

print(averager(10, 20, 30))

print('#' * 52 + ' Distinct Elements ')
print('#' * 52 + '  We know that set elements must be distinct - '
                 ' so how do all these methods we have seen for creating sets behave when we have repeated elements?')
print('#' * 52 + '  Let is take a look at each, one at a time:')

s = {'a', 'b', 'c', 'a', 'b', 'c'}
print(s)

print('#' * 52 + '  As you can see, Python just discards any repeated element.')
s = set('baabaa')
print(s)

print('#' * 52 + '  And the same with a comprehension:')
s = {c for c in 'moomoo'}
print(s)

print('#' * 52 + '  Now unpacking is a little different. If we unpack into a set, then sure, '
                 '  elements will remain distinct:')
s1 = {10, 20, 30}
s2 = {20, 30, 40}
s = {*s1, *s2}
print(s)

print('#' * 52 + '  But if we unpack into a tuple for example:')
t = (*s1, *s2)
print(t)

# Application
print('#' * 52 + '  Application')
print('#' * 52 + '  So, one really interesting application of sets and the fact that their elements are unique, '
                 '  is finding unique elements from collections whose elements might not be.')
print('#' * 52 + '  Consider this problem. We have a string, '
                 '  and we want to assign a score to the string based on how many distinct characters of the alphabet '
                 '  it uses.')
print('#' * 52 + '  (I am considering an alphabet here to be "a" - "z"). So the total length of that alphabet is 26, '
                 '  and we can score a string this way:')

s = 'abcdefghijklmnopqrstuvwxyz'
distinct = set(s)
score = len(s) / 26
print(score)

print('#' * 52 + '  Lets write a function to do this, (and remove any characters that are not part of our "alphabet"):')
def scorer(s):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    s = s.lower()
    distinct = set(s)
    # we want to only count characters that are in our alphabet
    effective = distinct & alphabet
    return len(effective) / len(alphabet)

print(scorer(s))
print(scorer('baa baa'))
print(2 / 26)
print(scorer('baa baa baa!!! 123'))
print(scorer('the quick brown fox jumps over the lazy dog'))


