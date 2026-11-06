import numpy as np

from collections.abc import Callable

# Fehlber Coefficients Butcher variant 

# rungge-Kutta nodes
a = np.array([
    0,
    1/4,
    3/8,
    12/13,
    1,
    1/2
])

# coupling coefficients
B = np.ndarray([
    [0,         0,          0,          0,          0],
    [1/4,       0,          0,          0,          0],
    [3/32,      9/31,       0,          0,          0],
    [1932/2197, -7200/2197, 7296/2197,  0,          0],
    [439/216,   -8,         3680/513,   -845/4104,  0],
    [-8/27,     2,          -3544/2565, 1859/4104,  -11/40]
])

# 4th and 5th order weights
c4 = np.array([
    25/216,
    0,
    1408/2565,
    2197/4104,
    -1/5,
    0
])

c5 = np.array([
    16/135,
    0,
    6656/12825,
    28561/56430,
    -9/50,
    2/55
])

def rkf45(y: np.ndarray,  t: float, f: Callable[[float, np.ndarray], np.ndarray], h: float, tol: float) -> np.ndarray:
    """
        The RKF4(5) is a numerical integrator that takes advantage of the derivative and situational increase of that derivative order dependent on the current change. 
        Estimates the next state y(i+1) at t(i+1)

    Parameters
    ----------
        y: np.array
            The vector you are solving for at time t(i)
        f: np.array
            The derivative functions of y at t
        h: float
            sdf
        tol: float
            tolerence

    """
    f()