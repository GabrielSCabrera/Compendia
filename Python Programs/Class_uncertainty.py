import numpy as np
import sys, re

class uFloat(object):

    '''
        A mathematical object analagous to floats, which allow for the
        implementation of uncertainty and takes this into account when
        performing mathematical operations
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
                assert False, 'Cannot perform operation between types \
                <uFloat> and <{}>'.format(type(x))
        return x

    '''MATHEMATICAL METHODS'''

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
        return self.__sub__(x)

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

    def __pow__(self, x):
        try:
            x = float(x)
        except:
            assert False, 'Cannot perform operation between types \
            <uFloat> and <{}>'.format(type(x))
        value = self.value**x
        uncertainty = value*x*self.relative_uncertainty
        return uFloat(value, uncertainty)

    def ln(self):
        value = np.log(self.value)
        uncertainty = self.relative_uncertainty
        return uFloat(value, uncertainty)

    def exp(self):
        value = np.exp(self.value)
        uncertainty = self.uncertainty
        return uFloat(value, uncertainty)

    def sqrt(self):
        return self.__pow__(0.5)

    '''MISC METHODS'''

    def __str__(self):
        return '{} ± {}'.format(self.value, self.uncertainty)

    def __repr__(self):
        return '{} ± {}'.format(self.value, self.uncertainty)

    def __float__(self):
        return float(self.value)

    def __int__(self):
        return int(self.value)

if __name__ == '__main__':
    pass
