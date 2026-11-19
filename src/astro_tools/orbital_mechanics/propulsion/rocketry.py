import math

def ideal_rocket_equation(Isp: float, g0: float, mass:float, delta_m: float | None = None, delta_v: float | None = None) -> tuple[float, float]:
    if (delta_v is None) == (delta_m is None):
        raise ValueError("Provide exactly one of delta_v or delta_m")
    
    if delta_m is None and delta_v is not None:
        delta_m = mass*(1- math.exp(delta_v / (Isp * g0)))
    elif delta_v is None and delta_m is not None:
        delta_v = Isp * g0 * math.log(1 - delta_m/mass)

    return delta_v, delta_m