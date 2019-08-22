import pickle

ser = pickle.dumps('Python Pickled Peppers')

print(ser)

print('#' * 52 + ' We can deserialize the data this way:  ')

deser = pickle.loads(ser)
print(deser)

print('#' * 52 + ' We can do the same thing with numerics ')
ser = pickle.dumps(3.14)
print(ser)
deser = pickle.loads(ser)
print(deser)

print('#' * 52 + ' We can do the same with lists and tuples:  ')
d = [10, 20, ('a', 'b', 30)]
ser = pickle.dumps(d)
print(ser)
deser = pickle.loads(ser)
print(deser)

print('#' * 52 + '  Note that the original and the deserialized objects are equal, but not identical:')
print(d is deser, d == deser)

print('#' * 52 + '  This works the same way with sets too:')
s = {'a', 'b', 'x', 10}
print(s)

ser = pickle.dumps(s)
print(ser)

deser = pickle.loads(ser)
print(deser)

print('#' * 52 + '  And finally, we can pickle dictionaries as well:')
d = {'b': 1, 'a': 2, 'c': {'x': 10, 'y': 20}}
print(d)

ser = pickle.dumps(d)
print(ser)

deser = pickle.loads(ser)
print(deser)
print(d == deser)

print('#' * 52 + '  What happens if we pickle a dictionary that has two of its values set to another dictionary?')
d1 = {'a': 10, 'b': 20}
d2 = {'x': 100, 'y': d1, 'z': d1}
print(d2)
ser = pickle.dumps(d2)
d3 = pickle.loads(ser)
print(d3)

print('#' * 52 + '  That seems to work... Is that sub-dictionary still the same as the original one?')
print(d3['y'] == d2['y'])
print(d3['y'] is d2['y'])

print('#' * 52 + '  But consider the original dictionary d2: both the x and y keys referenced the same dictionary d1:')
print(d2['y'] is d2['z'])

print('#' * 52 + '  How did this work with our deserialized dictionary?')
print(d3['y'] == d3['z'])

print('#' * 52 + '  As you can see the relative shared object is maintained.')
print('#' * 52 + '  ')

print('#' * 52 + '  What this means though is that you have to be very careful how you use serialization and deserialization.')
d1 = {'a': 1, 'b': 2}
d2 = {'x': 10, 'y': d1}
print(d1)
print(d2)
d1['c'] = 3
print(d1)
print(d2)

print('#' * 52 + '  Now suppose we pickle our dictionaries to restore those values the next time around, '
                 '  but use the same code, expecting the same result:')

d1 = {'a': 1, 'b': 2}
d2 = {'x': 10, 'y': d1}
d1_ser = pickle.dumps(d1)
d2_ser = pickle.dumps(d2)

# simulate exiting the program, or maybe just restarting the notebook
del d1
del d2

# load the data back up
d1 = pickle.loads(d1_ser)
d2 = pickle.loads(d2_ser)

# and continue processing as before
print(d1)
print(d2)
d1['c'] = 3
print(d1)
print(d2)

print('#' * 52 + '  So just remember that as soon as you pickle a dictionary, '
                 '  whatever object references it had to another object is essentially lost - '
                 '  just as if you had done a deep copy first. '
                 '  It is a subtle point, but one that can easily lead to bugs if we are not careful.')
print('#' * 52 + '  ')
print('#' * 52 + '  However, the pickle module is relatively intelligent and will not re-pickle an object it has'
                 '  already pickled - which means that relative references are preserved.')


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    def __repr__(self):
        return f'Person(name={self.name}, age={self.age})'


john = Person('John Cleese', 79)
eric = Person('Eric Idle', 75)
michael = Person('Michael Palin', 75)

parrot_sketch = {
    "title": "Parrot Sketch",
    "actors": [john, michael]
}

ministry_sketch = {
    "title": "Ministry of Silly Walks",
    "actors": [john, michael]
}

joke_sketch = {
    "title": "Funniest Joke in the World",
    "actors": [eric, michael]
}

fan_favorites = {
    "user_1": [parrot_sketch, joke_sketch],
    "user_2": [parrot_sketch, ministry_sketch]
}


from pprint import pprint
pprint(fan_favorites)

print('#' * 52 + '  As you can see we have some shared references, for example:')
print(fan_favorites['user_1'][0] is fan_favorites['user_2'][0])

print('#' * 52 + '  Lets store the id of the parrot_sketch for later reference:')
parrot_id_original = id(parrot_sketch)

print('#' * 52 + '  Now lets pickle and unpickle this object:')
ser = pickle.dumps(fan_favorites)
new_fan_favorites = pickle.loads(ser)
print(fan_favorites == new_fan_favorites)

print('#' * 52 + '  And lets look at the id of the parrot_sketch object in our new dictionary'
                 '  compared to the original one:')
print(id(fan_favorites['user_1'][0]), id(new_fan_favorites['user_1'][0]))

print('#' * 52 + '  As expected the ids differ - but the objects are equal:')
print(fan_favorites['user_1'][0] == new_fan_favorites['user_1'][0])

print('#' * 52 + '  But now lets look at the parrot sketch that is in both user_1 and user_2 - '
                 '  remember that originally the objects were identical (is):')
print(fan_favorites['user_1'][0] is fan_favorites['user_2'][0])

print('#' * 52 + '  and with our new object:')
print(new_fan_favorites['user_1'][0] is new_fan_favorites['user_2'][0])

print('#' * 52 + '  As you can see the relative relationship between objects that were pickled is preserved.')