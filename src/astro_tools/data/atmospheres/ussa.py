import math

from dataclasses import dataclass
from collections.abc import Callable

# Constants, but because of the time some of these are different from what we normally use now but the model still banks on them
R_EARTH = 6_356_766             # meter
REF_G = 9.80665                 # meter / second

R_UNIVERSAL = 8.31432                       # J / mole * K 
M_MOLAR_MASS = 0.0289644                    # kg / mole
R_SPECIFIC_GAS = R_UNIVERSAL / M_MOLAR_MASS # J / Kg * K

@dataclass(frozen=True)
class AtmosphericLayer:
    base_altitude: float                # geopotential height above MSL [m]
    lapse_rate: float                   # temperature lapse rate [K/m]
    base_molecular_temperature: float   # Standard Temp [K]
    base_pressure: float                # Static Pressure [Pa]

class USSA1976:
    layers = (
        AtmosphericLayer(0, -0.0065, 288.15, 101_325),
        AtmosphericLayer(11_000, 0.0, 216.65, 22_632.1),
        AtmosphericLayer(20_000, 0.001, 216.65, 5_474.89),
        AtmosphericLayer(32_000, 0.0028, 228.65, 868.019),
        AtmosphericLayer(47_000, 0.0, 270.65, 110.906),
        AtmosphericLayer(51_000, -0.0028, 270.65, 66.9389),
        AtmosphericLayer(71_000, -0.002, 214.65, 3.95642),
        AtmosphericLayer(84_852, 0.0, 186.964, 0.0)         # Note that the model stops at 84,852 meters up, so either contiune to use previous layer rates or 0
        )

    def __init__(self, altitude_converter: Callable[[float], float] | None = None):
        self._altitude_converter = (altitude_converter if altitude_converter is not None else self._geometric_to_geopotential)

    def _get_layer(self, altitude: float) -> tuple[AtmosphericLayer, float]:
        """
            Get layer of the U.S. Standard Atmospheric Model 1976.
        
            Parameters
            ----------
            altitude : float
                Geopotential Height [m].
        
            Returns
            -------
            tuple (AtmosphereicLayer, layerNumber)
                The USSA layer that the provided altitude is within, and the index of that layer.
        """
        layerNum = 0
        selectedLayer = self.layers[layerNum]

        for idx, layer in enumerate(self.layers):
            if altitude >= layer.base_altitude:
                selectedLayer = layer
                layerNum = idx
            else:
                break

        return selectedLayer, layerNum

    def _geometric_to_geopotential(self, altitude: float) -> float:
        """
            Converts from typical geometric altitude to geopotential altitude.
        
            Parameters
            ----------
            altitude : float
                Geometric Height (Z) [m].
        
            Returns
            -------
            h : float
                The Geopotential altitude defined for the USSA1976 [m].
        """
        return R_EARTH * altitude / (R_EARTH + altitude)

    def molecular_scale_temperature(self, altitude: float) -> float:
        h = self._altitude_converter(altitude)
        layer, layerNum = self._get_layer(h)

        if layerNum < len(self.layers) - 1:
            # model is covered
            temp = (h - layer.base_altitude) * layer.lapse_rate + layer.base_molecular_temperature
        else:
            # need to extrapolate up
            temp = self.layers[-1].base_molecular_temperature

        return temp


    def temperature(self, altitude: float) -> float:
        h = self._altitude_converter(altitude)
        layer, layerNum = self._get_layer(h)
        t = layer.base_molecular_temperature + layer.lapse_rate * (h - layer.base_altitude)
        return t

    def pressure(self, altitude: float) -> float:
        h = self._altitude_converter(altitude)
        layer, layerNum = self._get_layer(h)
        t = self.molecular_scale_temperature(altitude)

        
        if layer.lapse_rate == 0.0:
            # Isothermal layer
            pressure = layer.base_pressure * math.exp((-REF_G * (h - layer.base_altitude)) / (R_SPECIFIC_GAS * t))
        else:
            # Non-Isothermal layer
            expn = -REF_G / (R_SPECIFIC_GAS * layer.lapse_rate)
            pressure = layer.base_pressure * (t / layer.base_molecular_temperature) ** expn

        return pressure

    def density(self, altitude: float) -> float:
        pres = self.pressure(altitude)
        temp = self.molecular_scale_temperature(altitude)

        density =  pres / (R_SPECIFIC_GAS * temp)
        return density

