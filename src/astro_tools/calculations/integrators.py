import numpy as np
import math

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
B = np.array([
    [0,         0,          0,          0,          0],
    [1/4,       0,          0,          0,          0],
    [3/32,      9/32,       0,          0,          0],
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


def rkf45(y0: np.ndarray,  tspan: tuple[float, float], f: Callable[[float, np.ndarray], np.ndarray], rtol: float = 10e-8, atol: float | np.ndarray = 1e-6):
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

    atol = np.asarray(atol)

    if np.any(atol <= 0):
        raise ValueError("atol must be positive")

    if rtol < 0:
        raise ValueError("rtol must be non-negative")

    if atol.ndim > 1 or (atol.ndim == 1 and atol.shape != y0.shape):
        raise ValueError("atol must be scalar or match y0 shape")

    beta = 0.9  # 0.8 or 0.9 are common and depends on the program
    p = 4       # lower number of the two orders, in this case its a RKF4(5) so p=4

    # setting up initial conditions
    t0 = tspan[0]
    tf = tspan[1]
    t  = t0
    y = y0
    h = (tf - t0)/100
    # initialize outputs
    tout = [t]
    yout = [y.copy()]

    hMax_factor = 64.0
    hMin_factor = 1.0 / hMax_factor


    while(t < tf):
        k_1 = h * f(t + a[0]*h, y)
        k_2 = h * f(t + a[1]*h, y + B[1, 0]*k_1)
        k_3 = h * f(t + a[2]*h, y + B[2, 0]*k_1 + B[2, 1]*k_2)
        k_4 = h * f(t + a[3]*h, y + B[3, 0]*k_1 + B[3, 1]*k_2 + B[3, 2]*k_3)
        k_5 = h * f(t + a[4]*h, y + B[4, 0]*k_1 + B[4, 1]*k_2 + B[4, 2]*k_3 + B[4, 3]*k_4)
        k_6 = h * f(t + a[5]*h, y + B[5, 0]*k_1 + B[5, 1]*k_2 + B[5, 2]*k_3 + B[5, 3]*k_4 + B[5, 4]*k_5)

        y_new = y + c5[0]*k_1 + c5[1]*k_2 + c5[2]*k_3 + c5[3]*k_4 + c5[4]*k_5 + c5[5]*k_6
        error = (c5[0] - c4[0])*k_1 + (c5[1] - c4[1])*k_2 + (c5[2] - c4[2])*k_3 + (c5[3] - c4[3])*k_4 + (c5[4] - c4[4])*k_5 + (c5[5] - c4[5])*k_6

        scale = atol + rtol*np.maximum(np.abs(y), np.abs(y_new))
        norm_errors = np.abs(error) / scale

        truncation_error = np.max(norm_errors)

        # protect agains the 0 case
        if truncation_error > 0:
            factor = beta * (rtol/truncation_error)**(1 / (p+1))
        else:
            factor = hMax_factor

        factor = min(hMax_factor, max(hMin_factor, factor))
        h_new = h * factor

        # do we accept or reject the new state
        if truncation_error <= rtol:
            
            
            t += h
            y = y_new

            tout.append(t)
            yout.append(y.copy())

        h = h_new

    return np.array(tout), np.array(yout)