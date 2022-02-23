import numpy as np
from numpy.lib.mixins import NDArrayOperatorsMixin


class Values:
    def __init__(self, values):
        self._values = np.asarray(values)

    @property
    def values(self):
        return self._values

    @values.setter
    def values(self, values):
        self._values = values


class String:
    def __str__(self):
        return "\n".join(["\t".join([str(item) for item in row]) for row in self.values])


class Save:
    def save(self, path):
        with open(path, 'w') as f:
            f.write(str(self))


class Func:
    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
        assert method == '__call__'
        inputs_ = []
        for item in inputs:
            assert isinstance(item, self.__class__)
            inputs_.append(item.values)
        return self.__class__(ufunc(*inputs_, **kwargs))


class MixArray(NDArrayOperatorsMixin, Values, String, Save, Func):
    pass