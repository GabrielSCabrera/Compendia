from FYS2150_Class_uncertainty import uFloat as uF
from FYS2150_Class_uncertainty import uArray as uA
import FYS2150_Class_uncertainty as cU
import numpy as np

def eq(x,y):
    for i,j in zip(x,y):
        if i != j:
            return False
    return True

'''TESTING uFloat OBJECTS'''

try:
    a = uF(1, 0.1)
    b = uF(2, 0.2)
except:
    raise Exception('__init__ failed for uFloat')

#LOGICAL COMPARATORS
assert a == a, '__eq__ failed (uFloat == uFloat)'
assert a != b, '__ne__ failed (uFloat != uFloat)'
assert a < b, '__lt__ failed (uFloat < uFloat)'
assert b > a, '__gt__ failed (uFloat > uFloat)'
assert a <= a, '__le__ failed (uFloat <= uFloat)'
assert a >= a, '__ge__ failed (uFloat >= uFloat)'

#ARITHMETIC
assert 3 == (a + b).value, '__add__ failed (uFloat + uFloat)'
assert 1 == (b - a).value, '__sub__ failed (uFloat - uFloat)'
assert 2 == (b * a).value, '__mul__ failed (uFloat * uFloat)'
assert 0.5 == (a/b).value, '__truediv__ failed (uFloat / uFloat)'
assert 0 == (a//b).value, '__floordiv__ failed (uFloat / uFloat)'
assert 4 == (b**b).value, '__pow__ failed (uFloat ** uFloat)'
assert np.sqrt(2) == b.sqrt().value, 'sqrt() failed (uFloat)'
assert np.log(2) == b.ln().value, 'ln() failed (uFloat)'
assert np.exp(2) == b.exp().value, 'exp() failed (uFloat)'
assert a == abs(uF(-1, 0.1)), '__abs__ failed (uFloat)'
assert uF(-2, 0.2) == -b, '__neg__ failed (uFloat)'

assert 3 == (a + 2).value, '__add__ failed (uFloat + int)'
assert 1 == (b - 1).value, '__sub__ failed (uFloat - int)'
assert 2 == (b * 1).value, '__mul__ failed (uFloat * int)'
assert 0.5 == (a/2).value, '__truediv__ failed (uFloat / int)'
assert 0 == (a//2).value, '__floordiv__ failed (uFloat / int)'
assert 4 == (b**2).value, '__pow__ failed (uFloat **  int)'

assert 3 == (1 + b).value, '__radd__ failed (int + uFloat)'
assert 1 == (2 - a).value, '__rsub__ failed (int - uFloat)'
assert 2 == (2 * a).value, '__rmul__ failed (int * uFloat)'
assert 0.5 == (1/b).value, '__rtruediv__ failed (int / uFloat)'
assert 0 == (1//b).value, '__rfloordiv__ failed (int / uFloat)'
assert 4 == (2**b).value, '__rpow__ failed (int ** uFloat)'

#TYPE CONVERSION

assert 2/3 == float(b/3), 'failed to convert uFloat to float'
assert 2 == int(b), 'failed to convert uFloat to int'

'''TESTING uArray OBJECTS'''

#GENERATING TEST ARRAYS

a = []
b = []
c = []
d = []
e = []
f = []
g = []
h = []
j = []
k = []
l = []
m = []

for i in range(1,11):
    a.append(uF(i, 0.1))
    b.append(uF(2*i, 0.1))
    c.append(uF(3*i, np.sqrt(0.1**2 + 0.1**2)))
    d.append(2*i**2)
    e.append(0.5)
    f.append((i)**(i))
    g.append(np.sqrt(i))
    h.append(np.log(i))
    j.append(np.exp(i))
    k.append(uF(-i, 0.1))
    l.append(i//(2*i))
    m.append((2*i)%i)

try:
    a = uA(a)
    b = uA(b)
    c = uA(c)
except:
    raise Exception('__init__ failed for uArray')

assert c == (a + b), '__add__ failed (uArray + uArray)'
assert eq(a.values, (b - a).values), '__sub__ failed (uArray - uArray)'
assert eq(d, (b * a).values), '__mul__ failed (uArray * uArray)'
assert eq(e, (a/b).values), '__truediv__ failed (uArray / uArray)'
assert eq(l, (a//b).values), '__floordiv__ failed (uArray / uArray)'
assert eq(f, (a**a).values), '__pow__ failed (uArray ** uArray)'
assert eq(g, a.sqrt().values), 'sqrt() failed (uArray)'
assert eq(h, a.ln().values), 'ln() failed (uArray)'
assert eq(j, a.exp().values), 'exp() failed (uArray)'
assert eq(l, (b%a).values), '__mod__ failed (uArray / uArray)'

assert eq(k, -a), '__neg__ failed (uArray)'
assert eq(abs(uA(k)), a), '__abs__ failed (uArray)'

c = []
d = []
e = []
f = []
g = []
h = []
j = []

for i in range(1,11):
    c.append(i+2)
    d.append(i-2)
    e.append(i*2)
    f.append(i/2)
    g.append(i**2)
    h.append(i//2)
    j.append(i%2)

assert eq((a + 2).values, c), '__add__ failed (uArray + int)'
assert eq((a - 2).values, d), '__sub__ failed (uArray - int)'
assert eq((a * 2).values, e), '__mul__ failed (uArray * int)'
assert eq((a / 2).values, f), '__truediv__ failed (uArray / int)'
assert eq((a // 2).values, h), '__floordiv__ failed (uArray / int)'
assert eq((a **2).values, g), '__pow__ failed (uArray ** int)'
assert eq((a%2).values, j), '__mod__ failed (uArray ** int)'

#ITERATION

for n,i in enumerate(a):
    assert uF(n+1, 0.1) == i, '__iter__ failed (uArray)'

a = []
for i in range(10):
    a.append(uF(i, 0.1))

a = uA(a)
assert cU.linspace(0, 9, 10, 0.1) == a, 'linspace() failed'
assert cU.arange(0, 10, 1, 0.1) == a, 'arange() failed'

a = [uF(0, 0)]*10
a = uA(a)
assert cU.zeros(10) == a, 'zeros() failed'

a = [uF(1, 1)]*10
a = uA(a)
assert cU.ones(10) == a, 'ones() failed'

a = [uF(1, 1)]*9 + [uF(0, 0)] + [uF(1, 1)]
a = uA(a)
b = cU.ones(11)
b[-2] = uF(0, 0)
assert a == b, '__setitem__ failed ([int] = uFloat())'

a = [uF(1, 1)]*9 + [uF(0, 0)]*3 + [uF(1, 1)]
a = uA(a)
b = cU.ones(13)
b[9:-2] = cU.zeros(3)
assert a == b, '__setitem__ failed ([slice] = uArray())'

a = [uF(1, 1)]*9 + [uF(0, 0)]
a = uA(a)
b = cU.ones(9)
b.append(uF(0, 0))
assert a == b, 'append() failed'

assert uF(0, 0) in a, '__contains__ failed'
assert uF(1, 0) not in a, 'not __contains__ failed'

del a[-1]
assert a == cU.ones(9), '__delitem__ failed ([int])'

del b[7:]
assert b == cU.ones(7), '__delitem__ failed ([slice])'

a.append(uF(0, 0))
x = a.pop(-1)
assert (x == uF(0, 0)) and (a == cU.ones(9)), 'pop() failed'

success_msg = '| uFloat and uArray – ALL TESTS PASSED |'
print('~'*len(success_msg))
print(success_msg)
print('~'*len(success_msg))
