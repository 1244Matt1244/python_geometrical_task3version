# tests/integration/test_sphere.py
import pytest
from hypothesis import given, strategies as st
from geometry_toolkit.shapes.sphere import Sphere
from geometry_toolkit.core.shape import Dimension

@given(
    radius=st.floats(min_value=0.1, max_value=1000),
    unit=st.sampled_from(["m", "cm", "km"])
)
def test_sphere_volume_hypothesis(radius, unit):
    sphere = Sphere(Dimension(radius, unit), UnitConverter())
    volume, vol_unit = sphere.volume()
    assert volume > 0
    assert vol_unit == "m³"
