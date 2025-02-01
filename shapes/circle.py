# shapes/circle.py
from typing import Tuple
from dataclasses import dataclass

@dataclass
class Circle:
    radius: float
    unit: str = "m"

    def area(self) -> Tuple[float, str]:
        """Calculate the area of the circle with proper unit handling."""
        return 3.14159 * self.radius ** 2, f"{self.unit}²"
