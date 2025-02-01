# src/geometry_toolkit/engines/base_engine.py
from abc import ABC, abstractmethod
from ..core.shape import Shape

class CalculationEngine(ABC):
    @abstractmethod
    def calculate(self, shape: Shape) -> dict:
        pass

# src/geometry_toolkit/engines/numeric_engine.py
class NumericEngine(CalculationEngine):
    def calculate(self, shape: Shape) -> dict:
        return {
            "area": shape.area(),
            "volume": shape.volume()
        }
