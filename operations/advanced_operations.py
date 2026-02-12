import math


# ---------- ROOT & POWER ----------

def square_root(x):
    if x < 0:
        raise ValueError("Cannot calculate square root of negative number")
    return math.sqrt(x)


def cube_root(x):
    return math.copysign(abs(x) ** (1/3), x)


def power(base, exponent):
    return math.pow(base, exponent)


# ---------- LOG FUNCTIONS ----------

def log_base10(x):
    if x <= 0:
        raise ValueError("Log undefined for zero or negative numbers")
    return math.log10(x)


def natural_log(x):
    if x <= 0:
        raise ValueError("Natural log undefined for zero or negative numbers")
    return math.log(x)


# ---------- TRIG (DEGREES) ----------

def sine(degrees):
    return math.sin(math.radians(degrees))


def cosine(degrees):
    return math.cos(math.radians(degrees))


def tangent(degrees):
    return math.tan(math.radians(degrees))


# ---------- INVERSE TRIG ----------

def arcsin(x):
    return math.degrees(math.asin(x))


def arccos(x):
    return math.degrees(math.acos(x))


def arctan(x):
    return math.degrees(math.atan(x))


# ---------- HYPERBOLIC ----------

def sinh(x):
    return math.sinh(x)


def cosh(x):
    return math.cosh(x)


def tanh(x):
    return math.tanh(x)


# ---------- FACTORIAL ----------

def factorial(n):
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers")
    return math.factorial(n)


# ---------- EXPONENTIAL ----------

def exponential(x):
    return math.exp(x)


# ---------- CONSTANTS ----------

def pi():
    return math.pi


def e():
    return math.e


# ---------- CONVERSIONS ----------

def to_radians(degrees):
    return math.radians(degrees)


def to_degrees(radians):
    return math.degrees(radians)
