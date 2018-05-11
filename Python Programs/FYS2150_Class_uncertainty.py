import matplotlib.pyplot as plt
from matplotlib import rc
import numpy as np
import warnings
rc('text', usetex = True)

def list_to_uArray(a, uncertainty = None):
    if not isinstance(a, (list, tuple, np.ndarray)):
        raise TypeError('Can only convert objects of type <list>, <tuple>, and <np.ndarray>')
    new_a = []
    if uncertainty is None:
        uncertainty = np.std(np.array(a))
    if isinstance(uncertainty, (list, tuple, np.ndarray)):
        print(len(uncertainty), len(a))
        if len(uncertainty) != len(a):
            raise ValueError('Uncertainty arrays must be of equal length to their value arrays')
        for i,j in zip(a, uncertainty):
            new_a.append(uFloat(i, j))
    else:
        for i in a:
            new_a.append(uFloat(i, uncertainty))
    return uArray(new_a)

def zeros(x):
    if not isinstance(x, int):
        error = 'zeros function only accepts a length of type <int>'
        raise TypeError(error)
    a = [uFloat(0,0)]*x
    return uArray(a)

def ones(x):
    if not isinstance(x, int):
        error = 'ones function only accepts a length of type <int>'
        raise TypeError(error)
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

def plot(x, y, title = None, xlabel = None, ylabel = None, savename = None,
xlim = None, ylim = None, legend = None, proportional = False, border = None,
style = None, ms = None, filetype = 'pdf', hold = False):

    def _plot(x, y, style, ms, alpha = None):
        if alpha is None:
            alpha = 1
        if style is not None and ms is not None:
            plt.plot(x, y, style, ms = ms, alpha = alpha)
        elif style is not None and ms is None:
            plt.plot(x, y, style, alpha = alpha)
        elif style is None and ms is not None:
            plt.plot(x, y, ms = ms, alpha = alpha)
        else:
            plt.plot(x, y, alpha = alpha)

    if style is None:
        style = 'b-'

    if isinstance(x, np.ndarray):
        x = list(x)
    if isinstance(y, np.ndarray):
        y = list(y)

    if isinstance(x, uArray):
        x = x.values

    if isinstance(y, uArray):
        is_uarray = True
        y = list([np.array(y.values),
        np.array(y.values) + np.array(y.uncertainties),
        np.array(y.values) - np.array(y.uncertainties)])
        axis = [min(x), max(x), min(y[2]), max(y[1])]
    else:
        is_uarray = False
        axis = [min(x), max(x), min(y), max(y)]

    diff_x = axis[1] - axis[0]
    diff_y = axis[3] - axis[2]

    if xlim is not None and ylim is not None and border is not None:
        raise ValueError('Cannot use argument <border> when xlim and ylim are both manually defined')

    if proportional is True:
        fig, ax= plt.subplots()
        ax.set(aspect=1)

    if is_uarray is True:
        c = style[0]
        if c == 'b':
            c = 'r'
        else:
            c = 'b'
        if style[1:] == '-':
            _plot(x, y[0], style = style, ms = None, alpha = 0.7)
            _plot(x, y[1], c + '-.', ms = None, alpha = 0.7)
            _plot(x, y[2], c + '-.', ms = None, alpha = 0.7)
            plt.fill_between(x, y[2], y[1], alpha = 0.25, color = c)
        else:
            _plot(x, y[0], style = style, ms = None, alpha = 0.7)
            _plot(x, y[1], c + '|', ms = None, alpha = 0.7)
            _plot(x, y[2], c + '|', ms = None, alpha = 0.7)
    else:
        _plot(x, y, style, ms)

    if title is not None:
        plt.title(title, fontsize = 26)

    plt.xticks(fontsize = 22)
    plt.yticks(fontsize = 22)
    plt.grid(b = True, alpha = 0.3, linestyle = 'dashed')

    if xlabel is not None:
        plt.xlabel(xlabel, fontsize = 22)

    if ylabel is not None:
        plt.ylabel(ylabel, fontsize = 22)

    if border is True:
        border = [0.1, 0.1]
    elif isinstance(border, (float, int)):
        border = [border, border]

    if xlim is not None:
        plt.xlim([axis[0], axis[1]])
    elif border is not None:
        plt.xlim([axis[0]-diff_x*border[0], axis[1]+diff_x*border[0]])
    else:
        plt.xlim([axis[0], axis[1]])

    if ylim is not None:
        plt.ylim([axis[2], axis[3]])
    elif border is not None:
        plt.ylim([axis[2]-diff_y*border[1], axis[3]+diff_y*border[1]])
    else:
        plt.ylim([axis[2], axis[3]])

    if legend is not None:
        plt.legend(legend, ms = 18)

    if hold is False:
        if savename is not None:
            fig = plt.gcf()
            fig.set_size_inches((11.6, 6.5), forward=False)
            plt.savefig('{}.{}'.format(savename, filetype))
        else:
            plt.show()
        plt.close()

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
            raise ZeroDivisionError('Cannot divide by zero ({}/{})'\
            .format(self.value, x.value))
        value = self.value/x.value
        uncertainty = value*np.sqrt((self.relative_uncertainty)**2 + \
        (x.relative_uncertainty)**2)
        return uFloat(value, uncertainty)

    def __rtruediv__(self, x):
        x = self._get_type(x)
        if self.value == 0:
            raise ZeroDivisionError('Cannot divide by zero ({}/{})'\
            .format(x.value, self.value))
        value = x.value/self.value
        uncertainty = value*np.sqrt((self.relative_uncertainty)**2 + \
        (x.relative_uncertainty)**2)
        return uFloat(value, uncertainty)

    def __floordiv__(self, x):
        x = self._get_type(x)
        if x.value == 0:
            raise ZeroDivisionError('Cannot divide by zero ({}/{})'\
            .format(self.value, x.value))
        value = self.value//x.value
        uncertainty = value*np.sqrt((self.relative_uncertainty)**2 + \
        (x.relative_uncertainty)**2)
        return uFloat(value, uncertainty)

    def __rfloordiv__(self, x):
        x = self._get_type(x)
        if self.value == 0:
            raise ZeroDivisionError('Cannot divide by zero ({}/{})'\
            .format(x.value, self.value))
        value = x.value//self.value
        uncertainty = value*np.sqrt((self.relative_uncertainty)**2 + \
        (x.relative_uncertainty)**2)
        return uFloat(value, uncertainty)

    def __mod__(self, x):
        x = self._get_type(x)
        if x.value == 0:
            raise ZeroDivisionError('Cannot divide by zero ({}/{})'\
            .format(self.value, x.value))
        value = self.value % x.value
        uncertainty = value*np.sqrt((self.relative_uncertainty)**2 + \
        (x.relative_uncertainty)**2)
        return uFloat(value, uncertainty)

    def __rmod__(self, x):
        x = self._get_type(x)
        if self.value == 0:
            raise ZeroDivisionError('Cannot divide by zero ({}/{})'\
            .format(x.value, self.value))
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

    '''INPLACE OPERATORS'''

    def __iadd__(self, x):
        if not isinstance(x, (float, int, uFloat)):
            error = 'Cannot add an object of type<uFloat>'
            error += ' to object of type<{}>'.format(type(x))
            raise TypeError(error)
        else:
            return self.__add__(x)

    def __isub__(self, x):
        if not isinstance(x, (float, int, uFloat)):
            error = 'Cannot subtract an object of type<uFloat>'
            error += ' from object of type<{}>'.format(type(x))
            raise TypeError(error)
        else:
            return self.__sub__(x)

    def __imul__(self, x):
        if not isinstance(x, (float, int, uFloat)):
            error = 'Cannot multiply an object of type<uFloat>'
            error += ' with object of type<{}>'.format(type(x))
            raise TypeError(error)
        else:
            return self.__mul__(x)

    def __itruediv__(self, x):
        if not isinstance(x, (float, int, uFloat)):
            error = 'Cannot multiply an object of type<uFloat>'
            error += ' with object of type<{}>'.format(type(x))
            raise TypeError(error)
        else:
            return self.__truediv__(x)

    def __ifloordiv__(self, x):
        if not isinstance(x, (float, int, uFloat)):
            error = 'Cannot multiply an object of type<uFloat>'
            error += ' with object of type<{}>'.format(type(x))
            raise TypeError(error)
        else:
            return self.__floordiv__(x)

    def __imod__(self, x):
        if not isinstance(x, (float, int, uFloat)):
            error = 'Cannot multiply an object of type<uFloat>'
            error += ' with object of type<{}>'.format(type(x))
            raise TypeError(error)
        else:
            return self.__mod__(x)

    def __ipow__(self, x):
        if not isinstance(x, (float, int, uFloat)):
            error = 'Cannot multiply an object of type<uFloat>'
            error += ' with object of type<{}>'.format(type(x))
            raise TypeError(error)
        else:
            return self.__pow__(x)

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
        exp_digit = -np.floor(np.log10(self.uncertainty))
        return '{} ± {}'.format(np.round(self.value, int(exp_digit)),
        np.round(self.uncertainty, int(exp_digit)))

    def __repr__(self):
        return self.__str__()

    def __float__(self):
        return float(self.value)

    def __int__(self):
        return int(self.value)

    def __format__(self, s):
        error = '{{{}}} is an invalid uFloat format, use a number of 2-array'
        if s == '':
            return self.__str__()
        elif (s[-1] not in ['g','f','d']) or not isinstance(s, str):
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

    def dot(self, x):
        new = uFloat(0, 0)
        if isinstance(x, (list, tuple, np.ndarray, uArray)):
            for i,j in zip(self.a, x):
                new += i * j
        else:
            raise TypeError('Cannot apply dot() operator to uArray and {}'.format(type(x)))
        return new

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

    def mean(self):
        new = 0
        for i in self.a:
            new += i
        return new/self.__len__()

    def min(self):
        index = -1
        min_value = None
        min_uncertainty = None
        multiple = 1
        for n,i in enumerate(self.a):
            if min_value is None or i.value < min_value:
                index = n
                min_value = i.value
                min_uncertainty = i.uncertainty
                multiple = 1
            elif min_value == i.value:
                multiple += 1
                if i.uncertainty < min_uncertainty:
                    index = n
                    min_value = i.value
                    min_uncertainty = i.uncertainty
        if multiple > 1:
            msg = "Array contains {} minima, returning minimum".format(multiple)
            msg += " with lowest uncertainty."
            warnings.warn(msg)
        return self.a[index]

    def max(self):
        index = -1
        max_value = None
        max_uncertainty = None
        multiple = 1
        for n,i in enumerate(self.a):
            if max_value is None or i.value > max_value:
                index = n
                max_value = i.value
                max_uncertainty = i.uncertainty
                multiple = 1
            elif max_value == i.value:
                multiple += 1
                if i.uncertainty < max_uncertainty:
                    index = n
                    max_value = i.value
                    max_uncertainty = i.uncertainty
        if multiple > 1:
            msg = "Array contains {} maxima, returning maximum".format(multiple)
            msg += " with lowest uncertainty."
            warnings.warn(msg)
        return self.a[index]

    def argmin(self):
        index = -1
        min_value = None
        min_uncertainty = None
        multiple = 1
        for n,i in enumerate(self.a):
            if min_value is None or i.value < min_value:
                index = n
                min_value = i.value
                min_uncertainty = i.uncertainty
                multiple = 1
            elif min_value == i.value:
                multiple += 1
                if i.uncertainty < min_uncertainty:
                    index = n
                    min_value = i.value
                    min_uncertainty = i.uncertainty
        if multiple > 1:
            msg = "Array contains {} minima, returning index".format(multiple)
            msg += " of minimum with lowest uncertainty."
            warnings.warn(msg)
        return index

    def argmax(self):
        index = -1
        max_value = None
        max_uncertainty = None
        multiple = 1
        for n,i in enumerate(self.a):
            if max_value is None or i.value > max_value:
                index = n
                max_value = i.value
                max_uncertainty = i.uncertainty
                multiple = 1
            elif max_value == i.value:
                multiple += 1
                if i.uncertainty < max_uncertainty:
                    index = n
                    max_value = i.value
                    max_uncertainty = i.uncertainty
        if multiple > 1:
            msg = "Array contains {} maxima, returning index".format(multiple)
            msg += " of maximum with lowest uncertainty."
            warnings.warn(msg)
        return index

    def sum(self):
        new = self.a[0]
        for i in self.a[1:]:
            new += i
        return new

    def prod(self):
        new = self.a[0]
        for i in self.a[1:]:
            new *= i
        return new

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

    def __missing__(self, x):
        if isinstance(x, ('int', 'slice')):
            raise ValueError('Index [{}] is out of bounds for uArray object'.format(x))
        else:
            raise ValueError('Must use <int> or <slice> when getting item from uArray')

if __name__ == '__main__':
    pass
