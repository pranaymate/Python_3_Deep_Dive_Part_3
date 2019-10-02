print('#' * 52 + '  ')
from collections import defaultdict

print('#' * 52 + '  Standard dictionaries in Python will raise an exception if we try to access a non-existent key: ')
d = {}
# print(d['a']) #  KeyError: 'a'


print('#' * 52 + ' Now, we can certainly use the `.get` method:  ')

result = d.get('a')
print(type(result))

print('#' * 52 + '  And we can even specify a default value for the key if it is not present: ')

print(d.get('a', 0))

print('#' * 52 + ' Lets say we want to keep track of the number of occurrences of individual characters in a string.  ')

counts = {}
sentence = "able was I ere I saw elba"

for c in sentence:
    if c in counts:
        counts[c] += 1
    else:
        counts[c] = 1

print(counts)

print('#' * 52 + '  So this works, but we have that `if` statement - it would be nice to simplify our code somewhat: ')

counts = {}
for c in sentence:
    counts[c] = counts.get(c, 0) + 1

print(counts)

print('#' * 52 + ' Instead, we could use a `defaultdict`. In a `defaultdict` we specify what the default value is for'
                 ' a missing key - more precisely, we specify a default factory method that is called: ')

counts = defaultdict(lambda : 0)
for c in sentence:
    counts[c] += 1
print(counts)

print('#' * 52 + ' As you can see that simplified our code quite a bit, but the result is not quite a dictionary'
                 ' - it is a `defaultdict`. ')
print('#' * 52 + ' However, it inherits from `dict` so all the dictionary methods we have grown to know and love are'
                 ' still available because ` defaultdict` **is** a `dict`:  ')

print(isinstance(counts, defaultdict))
print(isinstance(counts, dict))

print('#' * 52 + ' And `counts` behaves like a regular dictionary too:  ')

print(counts.items())
print(counts['a'])


print('#' * 52 + '  The main difference is when we request a non-existent key: ')

print(counts['python'])

print('#' * 52 + ' We get the default value back - not only that, but it actually created that key as well:  ')

print(counts)

print('#' * 52 + ' And of course we can manipulate our dictionary just like a standard dictionary:  ')

counts['hello'] = 'world'
print(counts)

del counts['hello']
print(counts)

print('#' * 52 + ' Very often you will see what looks like a **type** specified as the default factory'
                 ' - but keep in mind that it is in fact the corresponding functions (constructors) that are actually'
                 ' being specified.  ')

print(int())
print(bool())
print(str())
print(list())

d = defaultdict(int)
print(d['a'])

d = defaultdict(bool)
print(d['a'])

d = defaultdict(str)
print(d['a'])

d = defaultdict(list)
print(d['a'])

print('#' * 52 + '  Note that this no different than writing: ')

d = defaultdict(lambda: list())
print(d['a'])

print('#' * 52 + ' Suppose we have a dictionary structure that has people s names as keys, '
                 'and a dictionary for the value that contains the persons eye color.  ')

persons = {
    'john': {'age': 20, 'eye_color': 'blue'},
    'jack': {'age': 25, 'eye_color': 'brown'},
    'jill': {'age': 22, 'eye_color': 'blue'},
    'eric': {'age': 35},
    'michael': {'age': 27}
}

eye_colors = {}
for person, details in persons.items():
    if 'eye_color' in details:
        color = details['eye_color']
    else:
        color = 'unknown'
    if color in eye_colors:
        eye_colors[color].append(person)
    else:
        eye_colors[color] = [person]

print(eye_colors)

print('#' * 52 + ' Now lets simplify this by leveraging the `.get` method: ')

eye_colors = {}
for person, details in persons.items():
    color = details.get('eye_color', 'Unknown')
    person_list = eye_colors.get(color, [])
    person_list.append(person)
    eye_colors[color] = person_list

print(eye_colors)

print('#' * 52 + '  And finally lets use a `defaultdict`: ')

eye_colors = defaultdict(list)
for person, details in persons.items():
    color = details.get('eye_color', 'Unknown')
    eye_colors[color].append(person)

print(eye_colors)

print('#' * 52 + ' When we create a `defaultdict` we have to specify the factory method as the first argument,'
                 ' but thereafter we can specify key/value pairs just like we would with the `dict` constructor'
                 ' (they are basically just passed along to the underlying `dict`): ')

d = defaultdict(bool, k1=True, k2=False, k3='python')
print(d)

print('#' * 52 + '  So, using this, if we had used a `defaultdict` for the Person values, '
                 '  we could simplify our previous example a bit more: ')

persons = {
    'john': defaultdict(lambda: 'unknown',
                        age=20, eye_color='blue'),
    'jack': defaultdict(lambda: 'unknown',
                        age=20, eye_color='brown'),
    'jill': defaultdict(lambda: 'unknown',
                        age=22, eye_color='blue'),
    'eric': defaultdict(lambda: 'unknown', age=35),
    'michael': defaultdict(lambda: 'unknown', age=27)
}

eye_colors = defaultdict(list)
for person, details in persons.items():
    eye_colors[details['eye_color']].append(person)

print(eye_colors)

print('#' * 52 + '  ')

from functools import partial
eyedict = partial(defaultdict, lambda: 'unknown')

print('#' * 52 + ' Alternatively we could also just define it this way:  ')

eyedict = lambda *args, **kwargs: defaultdict(lambda: 'unknown', *args, **kwargs)

persons = {
    'john': eyedict(age=20, eye_color='blue'),
    'jack': eyedict(age=20, eye_color='brown'),
    'jill': eyedict(age=22, eye_color='blue'),
    'eric': eyedict(age=35),
    'michael': eyedict(age=27)
}

print(persons)

print('#' * 52 + ' And we can use our previous code just as before:  ')

eye_colors = defaultdict(list)
for person, details in persons.items():
    eye_colors[details['eye_color']].append(person)

print(eye_colors)

print('#' * 52 + ' In this example we want to keep track of how many times certain functions are being called,'
                 ' as well as when they were **first** called.  ')
print('#' * 52 + ' To do this I want to be able to decorate the functions I want to keep track of,'
                 ' and I want to be able to specify the dictionary that should be used so'
                 ' I can keep a reference to it so I can examine the results.')

from collections import defaultdict, namedtuple
from datetime import datetime
from functools import wraps


def function_stats():
    d = defaultdict(lambda: {"count": 0, "first_called": datetime.utcnow()})
    Stats = namedtuple('Stats', 'decorator data')

    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            d[fn.__name__]['count'] += 1
            return fn(*args, **kwargs)

        return wrapper

    return Stats(decorator, d)

stats = function_stats()
print(dict(stats.data))

@stats.decorator
def func_1():
    pass

@stats.decorator
def func_2(x, y):
    pass

print(dict(stats.data))
print(func_1())
print(dict(stats.data))
print(func_1())
print(dict(stats.data))
print(func_2(10, 20))
print(dict(stats.data))

