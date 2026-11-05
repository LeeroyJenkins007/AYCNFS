import math

def hohmann_transfer_time(mu: float, radius_1: float, radius_2: float) -> float:

    semi_major_axis = (radius_1 + radius_2) / 2

    return math.pi * math.sqrt(
        semi_major_axis**3 / mu
    )