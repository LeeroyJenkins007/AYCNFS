import math

from astro_tools.data.celestial_body import CelestialBody


def orbital_velocity(body: CelestialBody, radius: float, a: float | None = None) -> float:
    """
    Calculate the orbital velocity of an orbit.

    Parameters
    ----------
    body.mu : float
        Gravitational parameter [m^3/s^2].
    radius : float
        Distance from body center [m].

    Returns
    -------
    float
        Orbital velocity [m/s].
    """
    if a is None:
        # circular orbit
        return math.sqrt(body.mu / radius)

    # Elliptical orbit (vis-viva equation)
    return math.sqrt((2*body.mu / radius) - (body.mu / a))


def escape_velocity(body: CelestialBody, radius: float) -> float:
     """
    Calculate escape velocity from a spherical body.

    Parameters
    ----------
    body.mu : float
        Gravitational parameter [m^3/s^2].
    radius : float
        Distance from body center [m].

    Returns
    -------
    float
        Escape velocity [m/s].
    """
     return math.sqrt(2 * body.mu / radius)


def orbital_period(body: CelestialBody, a: float) -> float:
    """
    Calculates the orbital period from any closed orbit.

    Parameters
    ----------
    body.mu : float
        Gravitational parameter [m^3/s^2].
    a : float
        Semi-Major axis of ellipse [m].
    
    Returns
    -------
    float
        Period for one complete orbit [s].
    """
    return 2 * math.pi * math.sqrt(
        a**3 / body.mu
    )