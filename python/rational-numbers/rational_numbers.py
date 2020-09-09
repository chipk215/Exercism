from __future__ import division
from __future__ import annotations
from math import gcd
from typing import Union


class Rational:
    def __init__(self, numer, denom):
        if denom == 0:
            raise Exception(f"Rational number {numer}/{denom} must have non-zero denominator")

        if denom < 0 <= numer:
            denom = abs(denom)
            numer *= -1

        if denom < 0 and numer < 0:
            denom = abs(denom)
            numer = abs(numer)

        self.numer = numer
        self.denom = denom
        self.reduce()

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other):
        sum_num = self.numer * other.denom + other.numer * self.denom
        sum_denom = self.denom * other.denom
        return Rational(sum_num, sum_denom)

    def __sub__(self, other):
        other.numer *= -1
        return self.__add__(other)

    def __mul__(self, other):
        prod_num = self.numer * other.numer
        prod_denom = self.denom * other.denom
        return Rational(prod_num, prod_denom)

    def __truediv__(self, other):
        quot_num = self.numer * other.denom
        quot_denom = other.numer * self.denom
        return Rational(quot_num, quot_denom)

    def __abs__(self):
        self.numer = abs(self.numer)
        self.denom = abs(self.denom)
        return self

    # https://stackoverflow.com/a/33533514/2304816
    def __pow__(self, power: Union[int, float, Rational]) -> Union[Rational, float]:
        """
        I don't like this function that returns two different types.
        :param power:
        :return:
        """
        if isinstance(power, int):
            return Rational(self.numer ** power, self.denom ** power)
        else:
            return self.numer ** power / self.denom ** power

    def __rpow__(self, base):
        temp = base ** self.numer
        return temp ** (1/self.denom)

    def reduce(self):
        gcd_value = gcd(self.numer, self.denom)
        self.numer //= gcd_value
        self.denom //= gcd_value
