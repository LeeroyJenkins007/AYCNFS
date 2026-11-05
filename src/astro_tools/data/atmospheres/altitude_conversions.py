
def kerbin_to_earth_geopotential(altitude: float) -> float:

    h = (7963.75 * altitude) / (6371 + 1.25*altitude)
    return h