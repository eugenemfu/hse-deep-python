import copy

class Matrix:
    def __init__(self, values):
        self.h = len(values)
        self.w = len(values[0])
        for row in values:
            assert len(row) == self.w
        self.values = values

    def _check_shape(self, other):
        assert isinstance(other, self.__class__)
        assert self.h == other.h
        assert self.w == other.w

    def __add__(self, other):
        self._check_shape(other)
        res = copy.deepcopy(self)
        for i in range(self.h):
            for j in range(self.w):
                res.values[i][j] += other.values[i][j]
        return res

    def __mul__(self, other):
        self._check_shape(other)
        res = copy.deepcopy(self)
        for i in range(self.h):
            for j in range(self.w):
                res.values[i][j] *= other.values[i][j]
        return res

    def __matmul__(self, other):
        assert isinstance(other, self.__class__)
        assert self.w == other.h
        res = self.__class__([[0 for _ in range(other.w)] for _ in range(self.h)])
        for i in range(self.h):
            for j in range(other.w):
                res.values[i][j] = sum(self.values[i][k] * other.values[k][j] for k in range(self.w))
        return res

    def __str__(self):
        return "\n".join(["\t".join([str(item) for item in row]) for row in self.values])

    def save(self, path):
        with open(path, 'w') as f:
            f.write(str(self))


class HashMixin:
    def __hash__(self):
        """
        Sum of the elements.
        """
        return int(sum(sum(row) for row in self.values))


class HashMatrix(Matrix, HashMixin):
    pass


def cached_matmul(a, b, cache):
    hashes = hash(a), hash(b)
    if hashes not in cache:
        cache[hashes] = a @ b
    return cache[hashes]