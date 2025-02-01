# tests/unit/test_circle.py
import pytest
from hypothesis import given, strategies as st
from geoshapes.shapes.circle import Circle

@given(radius=st.floats(min_value=0.1, max_value=1000))
def test_circle_area_hypothesis(radius: float):
    circle = Circle(radius=radius, unit="m")
    area, unit = circle.area()
    assert area > 0
    assert unit == "m²"
