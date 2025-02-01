# conftest.py
import pytest
from geoshapes.shapes import Circle

@pytest.fixture
def default_circle():
    return Circle(radius=5, unit="m")
