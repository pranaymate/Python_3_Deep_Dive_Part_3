print('#' * 52 + ' Remember the difference between equality (`=`) and identity (`is`):  ')

t1 = (1, 2, 3)
t2 = (1, 2, 3)

print(t1 is t2)
print(t1 == t2)

d = {t1: 100}
print(d[t1])
print(d[t2])

print('#' * 52 + ' As you can see, even though `t1` and `t2` are different **objects**, we can still retrieve'
                 ' the element from the dictionary using either one - because they compare **equal** to each other,'
                 ' and, in fact, **have the same hash** as well: ')

print(hash(t1), hash(t2))

print('#' * 52 + '   by default, different instances of a custom class instances will never compare equal,'
                 ' since by default it compares the memory address. ')


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'Person(name={self.name}, age={self.age})'

p1 = Person('John', 78)
p2 = Person('John', 78)

print(id(p1), id(p2))
print(p1 == p2)
print(hash(p1), hash(p2))

print('#' * 52 + ' Because of this default hash calculation, '
                 'we can actually use custom objects as keys in dictionaries: ')

p1 = Person('John', 78)
p2 = Person('Eric', 75)
persons = {p1: 'John object', p2: 'Eric object'}

for k in persons.keys():
    print(k)

print(persons[p1])

print('#' * 52 + '  ')
p = Person('John', 78)
print(p, id(p))
print(p1, id(p1))

print('#' * 52 + ' As you can see they are not the **same** object, they do not compare equal,'
                 ' and their hash is not the same:  ')

print(p == p1, hash(p), hash(p1))
print(persons.get(p, 'not found'))

print('#' * 52 + ' To do this we would start by implementing an `__eq__` method in our class: ')


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'Person(name={self.name}, age={self.age})'

    def __eq__(self, other):
        if isinstance(other, Person):
            return self.name == other.name and self.age == other.age
        else:
            return False

p1 = Person('John', 78)
p2 = Person('John', 78)

print(p1 == p2)

print('#' * 52 + '  ')


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'Person(name={self.name}, age={self.age})'

print(hash(Person('John', 78)))

print('#' * 52 + '  ')


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'Person(name={self.name}, age={self.age})'

    def __eq__(self, other):
        if isinstance(other, Person):
            return self.name == other.name and self.age == other.age
        else:
            return False

# print(hash(Person('John', 78))) # TypeError: unhashable type: 'Person'

hash_func = Person.__hash__
print(hash_func)

print('#' * 52 + ' Notice how the __hash__ attribute is `None` - it is not a function that returns `None`. ')
print('#' * 52 + ' In fact, we could have done this explicitly ourselves as well: ')


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'Person(name={self.name}, age={self.age})'

    def __eq__(self, other):
        if isinstance(other, Person):
            return self.name == other.name and self.age == other.age
        else:
            return False

    __hash__ = None

# print(hash(Person('John', 78))) #  TypeError: unhashable type: 'Person'

print('#' * 52 + ' In this case though, we do want Person instances to be hashable so we can recover Person keys in'
                 ' our dictionary based on whether the objects compare equal or not. ')
print('#' * 52 + ' In this case we simply want to create a hash based on `name` and `age`. Since both of these'
                 ' values are themselves hashable it turns out to be pretty easy to do:  ')


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'Person(name={self.name}, age={self.age})'

    def __eq__(self, other):
        if isinstance(other, Person):
            return self.name == other.name and self.age == other.age
        else:
            return False

    def __hash__(self):
        print('__hash__ called...')
        return hash((self.name, self.age))

p1 = Person('John', 78)
p2 = Person('John', 78)
print(id(p1) is id(p2))
print(p1 == p2)
print(hash(p1) == hash(p2))

print('#' * 52 + ' As you can see, `Person` objects are now hashable, and equal objects have equal hashes. Of course,'
                 ' if the objects are not equal they usually will have different hashes (though that is not mandatory'
                 ' - we will come back to that in a bit). ')

p3 = Person('Eric', 75)
print(p1 == p3)
print(hash(p1) == hash(p3))

print('#' * 52 + ' Lets just remove that print statement quick:  ')


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'Person(name={self.name}, age={self.age})'

    def __eq__(self, other):
        if isinstance(other, Person):
            return self.name == other.name and self.age == other.age
        else:
            return False

    def __hash__(self):
        return hash((self.name, self.age))

p1 = Person('John', 78)
p2 = Person('John', 78)
p3 = Person('Eric', 75)

persons = {p1: 'first John object'}
print(persons[p1])
print(persons[p2])
# print(persons[p3]) # KeyError: Person(name=Eric, age=75)

print('#' * 52 + ' Now lets try to add `p2` to the dictionary: ')

persons[p2] = 'other (equal) John object'
print(persons)

print('#' * 52 + ' As you can see, we actually just overwrote the value of that key -'
                 ' since those two keys are in fact equal (`==`). ')

persons = {p1: 'p1', p2: 'p2'}
print(persons)

print('#' * 52 + ' As you can see the key was considered the same, and hence the last value assignment was effective. ')

persons = {p1: 'p1', p3: 'p3'}
print(persons)

print('#' * 52 + ' When we call the `hash()` function, although it in turn calls'
                 ' the `__hash__` method, it does something more.  ')
print('#' * 52 + ' It will truncate the integer returned by `__hash__` to'
                 ' a certain width which is implementation dependent. ')
print('#' * 52 + ' In my case, I can see that hashes will be truncated to 64-bits:  ')

import sys
print(sys.hash_info.width)

print('#' * 52 + ' Lets just see how that affects the results of our `__hash__` method:  ')

class Test:
    def __hash__(self):
        return 1_000_000_000_000_000_000

print(hash(Test()))

class Test:
    def __hash__(self):
        return 10_000_000_000_000_000_000

print(hash(Test()))
mod = sys.hash_info.modulus
print(mod)
print(10_000_000_000_000_000_000 % mod)

print('#' * 52 + '  ')


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'Person(name={self.name}, age={self.age})'

    def __eq__(self, other):
        if isinstance(other, Person):
            return self.name == other.name and self.age == other.age
        else:
            return False

    def __hash__(self):
        return 100

p1 = Person('John', 78)
p2 = Person('Eric', 75)

print(hash(p1), hash(p2))
print(p1 == p2)
persons = {p1: 'p1', p2: 'p2'}
print(persons)
print(persons[p1])
print(persons[p2])
print(persons[Person('John', 78)])

print('#' * 52 + ' As you can see that still works just fine. '
                 ' But lets see how performance is affected by this.'
                 ' To test this we are going to create a slightly simpler class: ')


class Number:
    def __init__(self, x):
        self.x = x

    def __eq__(self, other):
        if isinstance(other, Number):
            return self.x == other.x
        else:
            return False

    def __hash__(self):
        return hash(self.x)


class SameHash:
    def __init__(self, x):
        self.x = x

    def __eq__(self, other):
        if isinstance(other, SameHash):
            return self.x == other.x
        else:
            return False

    def __hash__(self):
        return 100

numbers = {Number(i): 'some value' for i in range(1_000)}
same_hashes = {SameHash(i): 'some value' for i in range(1_000)}

print(numbers[Number(500)])
print(same_hashes[SameHash(500)])


print('#' * 52 + ' And now lets time how long it takes to retrieve an element from each of those dictionaries:  ')
from timeit import timeit
print(timeit('numbers[Number(500)]', globals=globals(), number=10_000))
print(timeit('same_hashes[SameHash(500)]', globals=globals(), number=10_000))

print('#' * 52 + ' Example  ')


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'({self.x}, {self.y})'

pt = Point(1, 2)
print(pt)


print('#' * 52 + ' In this case, we actually would like to be able to put these points as keys in a dictionary.'
                 ' We certainly can as it is: ')

points = {Point(0,0): 'pt 1', Point(1,1): 'pt 2'}
# points[Point(0,0)] #  KeyError: (0, 0)

print('#' * 52 + '  ')


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'({self.x}, {self.y})'

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        else:
            return False

    def __hash__(self):
        return hash((self.x, self.y))

points = {Point(0, 0): 'origin', Point(1,1): 'pt at (1,1)'}
print(points[Point(0,0)])

print('#' * 52 + '  ')


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'({self.x}, {self.y})'

    def __eq__(self, other):
        if isinstance(other, tuple) and len(other) == 2:
            other = Point(*other)
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        else:
            return False

    def __hash__(self):
        return hash((self.x, self.y))

points = {Point(0,0): 'origin', Point(1,1): 'pt at (1,1)'}
print(points[Point(0,0)])
print(points[(0,0)])

print('#' * 52 + ' In fact:  ')

print((0,0) == Point(0,0))

print('#' * 52 + ' You will notice that our `Point` class is technically mutable. '
                 'So we could do something like this:  ')

pt1 = Point(0,0)
pt2 = Point(1,1)
points = {pt1: 'origin', pt2: 'pt at (1,1)'}
print(points[pt1], points[Point(0,0)], points[(0,0)])

print('#' * 52 + ' But what happens if we mutate `pt1`?  ')
pt1.x = 10
print(pt1)
# print(points[pt1]) # KeyError: (10, 0)

print('#' * 52 + ' So we cant recover our item using `pt1`,'
                 ' that is because the hash of `pt1` has changed,'
                 ' so Python start looking in the wrong place in the dictionary.  ')

for k, v in points.items():
    print(k, v)

print('#' * 52 + '  ')


class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def __repr__(self):
        return f'({self.x}, {self.y})'

    def __eq__(self, other):
        if isinstance(other, tuple) and len(other) == 2:
            other = Point(*other)
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        else:
            return False

    def __hash__(self):
        return hash((self.x, self.y))

pt = Point(0,0)
print(pt.x)

# pt.x = 10 #  AttributeError: can't set attribute


