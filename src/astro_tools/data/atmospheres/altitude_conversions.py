
def kerbin_to_earth_geopotential(altitude: float) -> float:

    h = (7_963_750 * altitude) / (6_371_000 + 1.25*altitude)
    return h