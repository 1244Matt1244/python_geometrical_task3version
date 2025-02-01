# src/geometry_toolkit/core/shape.py
from abc import ABC, abstractmethod
from typing import Tuple
from dataclasses import dataclass
from .units import UnitConverter

@dataclass
class Dimension:
    value: float
    unit: str = "m"

class Shape(ABC):
    def __init__(self, unit_converter: UnitConverter):
        self.unit_converter = unit_converter

    @abstractmethod
    def area(self) -> Tuple[float, str]:
        pass

    @abstractmethod
    def volume(self) -> Tuple[float, str]:
        pass
