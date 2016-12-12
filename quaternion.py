import math

class Quaternion(object):
    def __init__(self, real = 0, i = 0, j = 0, k = 0):
        if type(real) == type(self):
            self.real = real.real
            self.i = real.i
            self.j = real.j
            self.k = real.k
        else:
            self.real = real
            self.i = 0
            self.j = 0
            self.k = 0

        if type(i) == type(self):
            self.real -= i.i
            self.i += i.real
            self.j += i.k
            self.k -= i.j
        elif type(real) != type(self):
            self.i = i

        if type(j) == type(self):
            self.real -= j.j
            self.i -= j.k
            self.j += j.real
            self.k += j.i
        elif type(real) != type(self):
            self.j = j

        if type(k) == type(self):
            self.real -= k.k
            self.i += k.j
            self.j -= k.i
            self.k += k.real
        elif type(real) != type(self):
            self.k = k

    def conjugate(self):
        return Quaternion(self.real, -self.i, -self.j, -self.k)

    def scalar_prod(self, other):
        result = (self.conjugate() * other + self * other.conjugate()) / 2
        if result.real != 0: return result.real
        elif result.i != 0: return  result.i
        elif result.j != 0: return result.j
        else: return result.k

    def vector_prod(self, other):
        return (self * other + other * self) / 2

    def __abs__(self):
        return math.sqrt(self.real * self.real +
                         self.i * self.i +
                         self.j * self.j +
                         self.k * self.k)

    def __truediv__(self, other):
        return Quaternion(self.real / other, self.i / other, self.j / other, self.k / other)

    def __neg__(self):
        return Quaternion(-self.real, -self.i, -self.j, -self.k)

    def __add__(self, other):
        other = Quaternion(other)
        return Quaternion(self.real + other.real,
                          self.i + other.i,
                          self.j + other.j,
                          self.k + other.k)

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        return self + (-other)

    def __rsub__(self, other):
        return other + (-self)

    def __mul__(self, other):
        other = Quaternion(other)
        return Quaternion(self.real * other.real - self.i * other.i - self.j * other.j - self.k * other.k,
                          self.real * other.i + self.i * other.real + self.j * other.k - self.k * other.j,
                          self.real * other.j + self.j * other.real + self.k * other.i - self.i * other.k,
                          self.real * other.k + self.k * other.real + self.i * other.j - self.j * other.i)

    def __rmul__(self, other):
        other = Quaternion(other)
        return other * self

    def __eq__(self, other):
        other = Quaternion(other)
        return (self.real == other.real and
                self.i == other.i and
                self.j == other.j and
                self.k == other.k)

    def __ne__(self, other):
        return not (self == other)

    def __str__(self):
        return "%g%+gi%+gj%+gk" % (self.real, self.i, self.j, self.k)