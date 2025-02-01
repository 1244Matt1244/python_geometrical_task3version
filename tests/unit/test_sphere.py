# tests/unit/test_sphere.py
from hypothesis import given, strategies as st
from geoshapes.shapes.sphere import Sphere

@given(radius=st.floats(min_value=0.1, exclude_min=True))
def test_sphere_volume_positive_radius(radius):
    sphere = Sphere(radius=radius)
    assert sphere.volume() > 0
