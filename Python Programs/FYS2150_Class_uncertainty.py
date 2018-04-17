import numpy as np

def zeros(x):
    if not isinstance(x, int):
        error = 'zeros function only accepts a length of type <int>'
    a = [uFloat(0,0)]*x
    return uArray(a)

def ones(x):
    if not isinstance(x, int):
        error = 'ones function only accepts a length of type <int>'
    a = [uFloat(1,1)]*x
    return uArray(a)

def arange(start, stop, step = 1, uncertainty = 0):
    if not isinstance(start, (int, float)):
        error = 'linspace function only accepts a start of type <int> or <float>'
    elif not isinstance(stop, (int, float)):
        error = 'linspace function only accepts a stop of type <int> or <float>'
    elif not isinstance(step, (int, float)):
        error = 'linspace function only accepts a step of type <int> or <float>'
    elif not isinstance(uncertainty, (int, float)):
        error = 'linspace function only accepts a uncertainty of type <int> or <float>'
    a_vals = np.arange(start, stop, step)
    a_uncertainty = uncertainty*np.ones_like(a_vals)
    a = []
    for i,j in zip(a_vals, a_uncertainty):
        a.append(uFloat(i,j))
    return uArray(a)

def linspace(start, stop, length, uncertainty = 0, retstep = False):
    if not isinstance(start, (int, float)):
        error = 'linspace function only accepts a start of type <int> or <float>'
    elif not isinstance(stop, (int, float)):
        error = 'linspace function only accepts a stop of type <int> or <float>'
    elif not isinstance(length, (int, float)):
        error = 'linspace function only accepts a length of type <int> or <float>'
    elif not isinstance(uncertainty, (int, float)):
        error = 'linspace function only accepts a uncertainty of type <int> or <float>'
    a_vals, step = np.linspace(start, stop, length, retstep = True)
    a_uncertainty = uncertainty*np.ones_like(a_vals)
    a = []
    for i,j in zip(a_vals, a_uncertainty):
        a.append(uFloat(i,j))
    if retstep is False:
        return uArray(a)
    elif retstep is True:
        return uArray(a), step
    else:
        error = 'Argument retstep must be of type <bool>'
        raise SyntaxError(error)

class uFloat(object):

    '''
        A mathematical object analagous to floats, which allow for the
        implementation of uncertainty and takes this into account when
        performing mathematical operations.

        Supports standard, reverse, and inplace mathematical operations such as:
            Addition, Subtraction, Multiplication, Division, Floor Division,
            Modulus, Exponentiation

        Also supports the following mathematical functions:
            abs(), __neg__, ln(), log(), sqrt() and exp()

        The following logical operators can be used between two uFloats:
            ==, !=, >, >=, <, <=

        In addition to math/logic functions, uFloat supports the following:
            int(), float(), __str__, __repr__, __format__
    '''

    def __init__(self, value, uncertainty = None):
        try:
            self.value = float(value)
        except:
            assert False, 'Cannot create uFloat object from type <{}>'\
            .format(type(value))

        if uncertainty is None:
            self.uncertainty = 0.
        else:
            try:
                self.uncertainty = abs(float(uncertainty))
            except:
                assert False, 'Cannot create uFloat object from type <{}>'\
                .format(type(uncertainty))

        if abs(self.value) < 1e-14 or abs(self.uncertainty/self.value) > 1:
            self.relative_uncertainty = self.uncertainty/(1 + abs(self.value))
        else:
            self.relative_uncertainty = self.uncertainty/abs(self.value)

    def _get_type(self, x):
        if not isinstance(x, uFloat):
            try:
                x = uFloat(x)
            except:
                error = 'Cannot perform operation between types <uFloat> and <{}>'.\
                format(type(x))
                raise TypeError(error)
        return x

    '''MATHEMATICAL METHODS'''

    def __abs__(self):
        return uFloat(abs(self.value), self.uncertainty)

    def __neg__(self):
        return uFloat(-self.value, self.uncertainty)

    def __add__(self, x):
        x = self._get_type(x)
        value = self.value + x.value
        uncertainty = np.sqrt(self.uncertainty**2 + x.uncertainty**2)
        return uFloat(value, uncertainty)

    def __radd__(self, x):
        return self.__add__(x)

    def __sub__(self, x):
        x = self._get_type(x)
        value = self.value - x.value
        uncertainty = np.sqrt(self.uncertainty**2 + x.uncertainty**2)
        return uFloat(value, uncertainty)

    def __rsub__(self, x):
        return -self.__sub__(x)

    '''INPLACE OPERATORS'''

    def __iadd__(self, x):
        if not isinstance(x, (float, int, long, uFloat)):
            error = 'Cannot add an object of type<uFloat>'
            error += ' to object of type<{}>'.format(type(x))
            raise TypeError(error)
        else:
            return self.__add__(x)

    def __isub__(self, x):
        if not isinstance(x, (float, int, long, uFloat)):
            error = 'Cannot subtract an object of type<uFloat>'
            error += ' from object of type<{}>'.format(type(x))
            raise TypeError(error)
        else:
            return self.__sub__(x)

    def __imul__(self, x):
        if not isinstance(x, (float, int, long, uFloat)):
            error = 'Cannot multiply an object of type<uFloat>'
            error += ' with object of type<{}>'.format(type(x))
            raise TypeError(error)
        else:
            return self.__mul__(x)

    def __itruediv__(self, x):
        if not isinstance(x, (float, int, long, uFloat)):
            error = 'Cannot multiply an object of type<uFloat>'
            error += ' with object of type<{}>'.format(type(x))
            raise TypeError(error)
        else:
            return self.__truediv__(x)

    def __ifloordiv__(self, x):
        if not isinstance(x, (float, int, long, uFloat)):
            error = 'Cannot multiply an object of type<uFloat>'
            error += ' with object of type<{}>'.format(type(x))
            raise TypeError(error)
        else:
            return self.__floordiv__(x)

    def __imod__(self, x):
        if not isinstance(x, (float, int, long, uFloat)):
            error = 'Cannot multiply an object of type<uFloat>'
            error += ' with object of type<{}>'.format(type(x))
            raise TypeError(error)
        else:
            return self.__mod__(x)

    def __ipow__(self, x):
        if not isinstance(x, (float, int, long, uFloat)):
            error = 'Cannot multiply an object of type<uFloat>'
            error += ' with object of type<{}>'.format(type(x))
            raise TypeError(error)
        else:
            return self.__pow__(x)

    '''MATHEMATICAL METHODS WIP'''

    def __mul__(self, x):
        x = self._get_type(x)
        value = self.value*x.value
        uncertainty = value*np.sqrt((self.relative_uncertainty)**2 + \
        (x.relative_uncertainty)**2)
        return uFloat(value, uncertainty)

    def __rmul__(self, x):
        return self.__mul__(x)

    def __truediv__(self, x):
        x = self._get_type(x)
        if x.value == 0:
            raise ZeroDivisionError('Cannot divide by zero ({}/{})')\
            .format(self.value, x.value)
        value = self.value/x.value
        uncertainty = value*np.sqrt((self.relative_uncertainty)**2 + \
        (x.relative_uncertainty)**2)
        return uFloat(value, uncertainty)

    def __rtruediv__(self, x):
        x = self._get_type(x)
        if self.value == 0:
            raise ZeroDivisionError('Cannot divide by zero ({}/{})')\
            .format(x.value, self.value)
        value = x.value/self.value
        uncertainty = value*np.sqrt((self.relative_uncertainty)**2 + \
        (x.relative_uncertainty)**2)
        return uFloat(value, uncertainty)

    def __floordiv__(self, x):
        x = self._get_type(x)
        if x.value == 0:
            raise ZeroDivisionError('Cannot divide by zero ({}/{})')\
            .format(self.value, x.value)
        value = self.value//x.value
        uncertainty = value*np.sqrt((self.relative_uncertainty)**2 + \
        (x.relative_uncertainty)**2)
        return uFloat(value, uncertainty)

    def __rfloordiv__(self, x):
        x = self._get_type(x)
        if self.value == 0:
            raise ZeroDivisionError('Cannot divide by zero ({}/{})')\
            .format(x.value, self.value)
        value = x.value//self.value
        uncertainty = value*np.sqrt((self.relative_uncertainty)**2 + \
        (x.relative_uncertainty)**2)
        return uFloat(value, uncertainty)

    def __mod__(self, x):
        x = self._get_type(x)
        if x.value == 0:
            raise ZeroDivisionError('Cannot divide by zero ({}/{})')\
            .format(self.value, x.value)
        value = self.value % x.value
        uncertainty = value*np.sqrt((self.relative_uncertainty)**2 + \
        (x.relative_uncertainty)**2)
        return uFloat(value, uncertainty)

    def __rmod__(self, x):
        x = self._get_type(x)
        if self.value == 0:
            raise ZeroDivisionError('Cannot divide by zero ({}/{})')\
            .format(x.value, self.value)
        value = x.value % self.value
        uncertainty = value*np.sqrt((self.relative_uncertainty)**2 + \
        (x.relative_uncertainty)**2)
        return uFloat(value, uncertainty)

    def __pow__(self, x):
        try:
            x = float(x)
        except:
            error = 'Cannot perform exponentiation between types <uFloat> and <{}>'.\
            format(type(x))
            raise TypeError(error)
        value = self.value**x
        uncertainty = value*x*self.relative_uncertainty
        return uFloat(value, uncertainty)

    def __rpow__(self, x):
        try:
            x = uFloat(x, 0)
        except:
            error = 'Cannot perform exponentiation between types <{}> and <uFloat>'.\
            format(type(x))
            raise TypeError(error)
        return x.__pow__(self)

    def ln(self):
        value = np.log(self.value)
        uncertainty = self.relative_uncertainty
        return uFloat(value, uncertainty)

    def log(self, x = 10):
        value = np.log(self.value, x)
        uncertainty = self.relative_uncertainty/np.log(x)
        return uFloat(value, uncertainty)

    def exp(self):
        value = np.exp(self.value)
        uncertainty = self.uncertainty
        return uFloat(value, uncertainty)

    def sqrt(self):
        return self.__pow__(0.5)

    '''LOGIC'''

    def __eq__(self, x):
        if not isinstance(x, uFloat):
            error = 'Cannot equate an object of type <uFloat> to an object of type <{}>'.format(type(x))
            raise TypeError(error)
        if (self.value == x.value) and (self.uncertainty == x.uncertainty):
            return True
        else:
            return False

    def __ne__(self, x):
        if not isinstance(x, uFloat):
            error = 'Cannot equate an object of type <uFloat> to an object of type <{}>'.format(type(x))
            raise TypeError(error)
        if (self.value != x.value) or (self.uncertainty != x.uncertainty):
            return True
        else:
            return False

    def __lt__(self, x):
        if not isinstance(x, uFloat):
            error = 'Cannot equate an object of type <uFloat> to an object of type <{}>'.format(type(x))
            raise TypeError(error)
        if self.value < x.value:
            return True
        else:
            return False

    def __gt__(self, x):
        if not isinstance(x, uFloat):
            error = 'Cannot equate an object of type <uFloat> to an object of type <{}>'.format(type(x))
            raise TypeError(error)
        if self.value > x.value:
            return True
        else:
            return False

    def __le__(self, x):
        if not isinstance(x, uFloat):
            error = 'Cannot equate an object of type <uFloat> to an object of type <{}>'.format(type(x))
            raise TypeError(error)
        if self.value <= x.value:
            return True
        else:
            return False

    def __ge__(self, x):
        if not isinstance(x, uFloat):
            error = 'Cannot equate an object of type <uFloat> to an object of type <{}>'.format(type(x))
            raise TypeError(error)
        if self.value >= x.value:
            return True
        else:
            return False

    '''MISC METHODS'''

    def __str__(self):
        return '{} ± {}'.format(self.value, self.uncertainty)

    def __repr__(self):
        return '{} ± {}'.format(self.value, self.uncertainty)

    def __float__(self):
        return float(self.value)

    def __int__(self):
        return int(self.value)

    def __format__(self, s):
        error = '{{{}}} is an invalid uFloat format, use a number of 2-array'
        if s == '':
            return self.__str__()
        if (s[-1] not in ['g','f','d']) or not isinstance(s, str):
            raise SyntaxError(error)
        c1 = float(s[:-1])
        c2 = s[-1]
        try:
            if c2 == 'g':
                string = '{:{d1}g} ± {:{d1}g}'.format(self.value,
                self.uncertainty, d1 = c1)
            elif c2 == 'f':
                string = '{:{d1}f} ± {:{d1}f}'.format(self.value,
                self.uncertainty, d1 = c1)
            elif c2 == 'd':
                string = '{:{d1}d} ± {:{d1}d}'.format(self.value,
                self.uncertainty, d1 = c1)
        except:
            raise SyntaxError(error)
        return string

class uArray(object):

    '''
        A mathematical object analagous to ndarrays, which allow for the
        implementation of uncertainty and takes this into account when
        performing mathematical operations.

        Supports standard, reverse, and inplace mathematical operations such as:
            Addition, Subtraction, Multiplication, Division, Floor Division,
            Modulus, Exponentiation

        Also supports the following mathematical functions:
            abs(), __neg__, ln(), log(), sqrt() and exp()

        The following logical operators can be used between two uArrays:
            ==, !=

        In addition to math/logic functions, uArray supports the following:
            __str__, __repr__, len(), __contains__, __getitem__, __setitem__,
            __delitem__, pop(), append()

        It is also possible to iterate through a uArray object
    '''

    def __init__(self, a):
        if not isinstance(a, (list, tuple)):
            raise TypeError('Invalid attempt to create uArray with type <{}>'.format(type(a)))
        self.a = a
        self.size = len(a)
        self.values = np.zeros(self.size)
        self.uncertainties = np.zeros(self.size)
        self.iterindex = 0

        for n,i in enumerate(a):
            self.values[n] = i.value
            self.uncertainties[n] = i.uncertainty

    '''MATHEMATICAL METHODS'''

    def __abs__(self):
        new_a = []
        for i in self.a:
            new_a.append(abs(i))
        return uArray(new_a)

    def __neg__(self):
        new_a = []
        for i in self.a:
            new_a.append(-i)
        return uArray(new_a)

    def __add__(self, x):
        new_a = []
        if isinstance(x, (list, tuple, np.ndarray, uArray)):
            for i,j in zip(self.a, x):
                new_a.append(i + j)
        elif isinstance(x, (int, float, uFloat)):
            for i in self.a:
                new_a.append(i + x)
        return uArray(new_a)

    def __radd__(self, x):
        new_a = self.__add__(x)
        return uArray(new_a)

    def __sub__(self, x):
        new_a = []
        if isinstance(x, (list, tuple, np.ndarray, uArray)):
            for i,j in zip(self.a, x):
                new_a.append(i - j)
        elif isinstance(x, (int, float, uFloat)):
            for i in self.a:
                new_a.append(i - x)
        return uArray(new_a)

    def __rsub__(self, x):
        new_a = self.__neg__(self.__sub__(x))
        return uArray(new_a)

    '''MATHEMATICAL METHODS WIP'''

    def __mul__(self, x):
        new_a = []
        if isinstance(x, (list, tuple, np.ndarray, uArray)):
            for i,j in zip(self.a, x):
                new_a.append(i * j)
        elif isinstance(x, (int, float, uFloat)):
            for i in self.a:
                new_a.append(i * x)
        return uArray(new_a)

    def __rmul__(self, x):
        new_a = []
        return self.__mul__(x)

    def __truediv__(self, x):
        new_a = []
        if isinstance(x, (list, tuple, np.ndarray, uArray)):
            for i,j in zip(self.a, x):
                new_a.append(i / j)
        elif isinstance(x, (int, float, uFloat)):
            for i in self.a:
                new_a.append(i / x)
        return uArray(new_a)

    def __rtruediv__(self, x):
        new_a = []
        if isinstance(x, (list, tuple, np.ndarray, uArray)):
            for i,j in zip(self.a, x):
                new_a.append(j / i)
        elif isinstance(x, (int, float, uFloat)):
            for i in self.a:
                new_a.append(x / i)
        return uArray(new_a)

    def __floordiv__(self, x):
        new_a = []
        if isinstance(x, (list, tuple, np.ndarray, uArray)):
            for i,j in zip(self.a, x):
                new_a.append(i // j)
        elif isinstance(x, (int, float, uFloat)):
            for i in self.a:
                new_a.append(i // x)
        return uArray(new_a)

    def __rfloordiv__(self, x):
        new_a = []
        if isinstance(x, (list, tuple, np.ndarray, uArray)):
            for i,j in zip(self.a, x):
                new_a.append(j // i)
        elif isinstance(x, (int, float, uFloat)):
            for i in self.a:
                new_a.append(x // i)
        return uArray(new_a)

    def __mod__(self, x):
        new_a = []
        if isinstance(x, (list, tuple, np.ndarray, uArray)):
            for i,j in zip(self.a, x):
                new_a.append(i % j)
        elif isinstance(x, (int, float, uFloat)):
            for i in self.a:
                new_a.append(i % x)
        return uArray(new_a)

    def __rmod__(self, x):
        new_a = []
        if isinstance(x, (list, tuple, np.ndarray, uArray)):
            for i,j in zip(self.a, x):
                new_a.append(j % i)
        elif isinstance(x, (int, float, uFloat)):
            for i in self.a:
                new_a.append(x % i)
        return uArray(new_a)

    def __pow__(self, x):
        new_a = []
        if isinstance(x, (list, tuple, np.ndarray, uArray)):
            for i,j in zip(self.a, x):
                new_a.append(i ** j)
        elif isinstance(x, (int, float, uFloat)):
            for i in self.a:
                new_a.append(i ** x)
        return uArray(new_a)

    def ln(self):
        new_a = []
        for i in self.a:
            new_a.append(i.ln())
        return uArray(new_a)

    def log(self, x = 10):
        new_a = []
        for i in self.a:
            new_a.append(i.log(x))
        return uArray(new_a)

    def exp(self):
        new_a = []
        for i in self.a:
            new_a.append(i.exp())
        return uArray(new_a)

    def sqrt(self):
        new_a = []
        for i in self.a:
            new_a.append(i.sqrt())
        return uArray(new_a)

    '''INPLACE OPERATORS'''

    def __iadd__(self, x):
        return self.__add__(x)

    def __isub__(self, x):
        return self.__sub__(x)

    def __imul__(self, x):
        return self.__mul__(x)

    def __itruediv__(self, x):
        return self.__truediv__(x)

    def __ifloordiv__(self, x):
        return self.__floordiv__(x)

    def __imod__(self, x):
        return self.__mod__(x)

    '''LOGIC'''

    def __eq__(self, x):
        if not isinstance(x, uArray):
            error = 'Cannot compare object of type <uArray> to object of type <{}>'.\
            format(type(x))
            raise TypeError(error)
        if self.__len__() != len(x):
            return False
        for i,j in zip(self.a, x.a):
            if i != j:
                return False
        return True

    def __ne__(self, x):
        return not self.__eq__(x)

    '''MISC METHODS'''

    def __str__(self):
        string = 'uArray('
        for i in range(self.size):
            string += '{} ± {}'.format(self.values[i], self.uncertainties[i])
            if i < self.size - 1:
                string += ', '
        return string + ')'

    def __repr__(self):
        return self.__str__()

    def _slice(self, x):
        start = x.start
        stop = x.stop
        step = x.step
        if start is None:
            start = 0
        elif start < 0:
            start = self.size + start
        if stop is None:
            stop = self.size - 1
        elif stop < 0:
            stop = self.size + stop
        if step is None:
            step = 1
        return start, stop, step

    '''ARRAY FUNCTIONS'''

    def __len__(self):
        return self.size

    def __contains__(self, x):
        for i in self.a:
            if i.__eq__(x):
                return True
        return False

    def __getitem__(self, x):
        if isinstance(x, slice):
            start, stop, step = self._slice(x)
            new_a = []
            for n in range(self.size):
                if (n >= start) and (n < stop):
                    new_a.append(self.a[n])
            return uArray(new_a)
        elif isinstance(x, int):
            if x < 0:
                x = self.size + x
            return self.a[x]
        else:
            error = 'Attempting to set values in uArray with invalid slice'
            raise ValueError(error)

    def __delitem__(self, x):
        new_a = []
        if isinstance(x, slice):
            start, stop, step = self._slice(x)
            for n,i in enumerate(self.a):
                if ((n < start) or (n > stop)) and ((n+1) % step != 1):
                    new_a.append(i)
        elif isinstance(x, int):
            if x < 0:
                x = self.size + x
            for n,i in enumerate(self.a):
                if n != x:
                    new_a.append(i)
        else:
            raise TypeError('Command <del> only works with an <int> or <slice>')
        self.__init__(new_a)

    def pop(self, x):
        if not isinstance(x, int):
            raise TypeError('Method pop() only accepts indices of type <int>')
        pop_val = self.__getitem__(x)
        self.__delitem__(x)
        return pop_val

    def __setitem__(self, x, y):
        new_a = []
        if isinstance(x, slice):
            start, stop, step = self._slice(x)
            N = stop - start + 1
        if not isinstance(y, (uFloat, uArray)):
            error = 'uArray only accepts elements of type <uArray> or <uFloat>'
            raise TypeError(error)
        elif isinstance(x, int) and isinstance(y, uFloat):
            if x < 0:
                x = self.size + x
            for n,i in enumerate(self.a):
                if n != x:
                    new_a.append(i)
                else:
                    new_a.append(y)
        elif isinstance(x, slice) and isinstance(y, uArray) and len(y) == N:
            new_a = []
            counter = 0
            for n,i in enumerate(self.a):
                if (n >= start) and (n <= stop):
                    new_a.append(y[counter])
                    counter += 1
                else:
                    new_a.append(i)
        else:
            error = 'Attempting to set values in uArray with invalid slice'
            raise ValueError(error)
        self.__init__(new_a)

    def __iter__(self):
        for i in self.a:
            yield i

    def append(self, x):
        if not isinstance(x, uFloat):
            error = 'Cannot append object of type <{}> to uArray, only <uFloat>'\
            .format(type(x))
            TypeError(error)
        new_a = self.a + [x]
        self.__init__(new_a)

if __name__ == '__main__':
    pass
