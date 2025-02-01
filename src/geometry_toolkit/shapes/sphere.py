# src/geometry_toolkit/shapes/sphere.py
from ..core.shape import Shape, Dimension
from ..exceptions import InvalidDimensionError

class Sphere(Shape):
    def __init__(self, radius: Dimension, unit_converter):
        super().__init__(unit_converter)
        if radius.value <= 0:
            raise InvalidDimensionError("Radius must be positive")
        self.radius = radius

    def area(self) -> Tuple[float, str]:
        # Surface area
        converted_radius = self.unit_converter.convert(
            self.radius.value, self.radius.unit, "m"
        )
        area = 4 * 3.14159 * converted_radius ** 2
        return area, "m²"

    def volume(self) -> Tuple[float, str]:
        converted_radius = self.unit_converter.convert(
            self.radius.value, self.radius.unit, "m"
        )
        volume = (4/3) * 3.14159 * converted_radius ** 3
        return volume, "m³"
