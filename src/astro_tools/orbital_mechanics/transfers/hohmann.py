import math

from dataclasses import dataclass
from ..two_body import orbital_period

@dataclass(frozen=True)
class HohmannTransfer:
    semi_major_axis: float
    eccentricity: float

    departure_velocity: float
    arrival_velocity: float

    delta_v1: float
    delta_v2: float
    total_delta_v: float

    transfer_time: float
  

"Classical Hohmann transfer from circular to circular"
def hohmann_transfer(mu: float, r1: float, r2: float) -> HohmannTransfer:
    a = (r1 +  r2)/2
    e = abs(r2-r1) / (r1 + r2)

    "Honestly a better way i think is using velocities directly "
    h1 = math.sqrt(mu*r1)
    h2 = math.sqrt(2*mu)*math.sqrt(r1*r2/(r1 + r2))
    h3 = math.sqrt(mu*r2)

    "Init orbit"
    v1 = h1/r1
    "Transfer orbit"
    v2 = h2/r1
    v3 = h2/r2
    "final orbit"
    v4 = h3/r2

    delta_v1 = abs(v2 - v1)
    delta_v2 = abs(v4 - v3)

    total_delta_v = delta_v1 + delta_v2

    return HohmannTransfer(
        semi_major_axis=a,
        eccentricity=e,
        departure_velocity=v2,
        arrival_velocity=v3,
        delta_v1=delta_v1,
        delta_v2=delta_v2,
        total_delta_v=total_delta_v,
        transfer_time=orbital_period(mu, a)/2
    )

def hohmann_transfer_semi_major_axis(r1: float, r2: float) -> float:
    return (r1 + r2)/2  

def hohmann_transfer_time(mu: float, radius_1: float, radius_2: float) -> float:

    semi_major_axis = hohmann_transfer_semi_major_axis(radius_1, radius_2)

    return orbital_period(mu, semi_major_axis) / 2

