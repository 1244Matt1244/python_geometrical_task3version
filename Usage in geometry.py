def calculate_sphere_volume(radius: float, unit: str) -> Tuple[float, str]:
    if radius <= 0:
        raise InvalidDimensionError("Radius must be positive")
    ...
