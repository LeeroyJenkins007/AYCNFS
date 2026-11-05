from dataclasses import dataclass

EARTH_REF_RADIUS = 6_356_766    # meter
REF_G = 9.80665                 # meter / second

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

    def _get_layer(self, altitude: float) -> AtmosphericLayer:
        """
            Get layer of the U.S. Standard Atmospheric Model 1976.
        
            Parameters
            ----------
            altitude : float
                Geopotential Height [m].
        
            Returns
            -------
            AtmosphereicLayer
                The USSA layer that the provided altitude is within.
        """
        selectedLayer = self.layers[0]

        for layer in self.layers:
            if altitude >= layer.base_altitude:
                selectedLayer = layer
            else:
                break

        return selectedLayer

    def _geometric_to_geopotential(self, altitude: float) -> float:
        """
            Converts from typical geometric altitude to geopotential altitude.
        
            Parameters
            ----------
            altitude : float
                Geopotential Height [m].
        
            Returns
            -------
            AtmosphereicLayer
                The USSA layer that the provided altitude is within.
        """

    def molecular_scale_temperature(self, altitude: float) -> float:
        h = self._geometric_to_geopotential(altitude)

    def temperature(self, altitude: float) -> float:
        ...

    def pressure(self, altitude: float) -> float:
        ...

    def density(self, altitude: float) -> float:
        ...