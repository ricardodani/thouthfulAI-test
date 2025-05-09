SPECIAL, STANDARD, REJECTED = "special", "standard", "rejected"


def sort(width: float, height: float, length: float, mass: float) -> str:
    volume = width * height * length
    bulky_dimensions = (height >= 150, width >= 150, length >= 150)
    is_bulky = volume >= 1_000_000 or any(bulky_dimensions)
    is_heavy = mass >= 20

    if is_bulky and is_heavy:
        return REJECTED
    elif is_bulky or is_heavy:
        return SPECIAL
    return STANDARD


if __name__ == "__main__":
    # Test cases
    assert sort(10, 10, 10, 10) == STANDARD
    assert sort(10, 10, 151, 10) == SPECIAL
    assert sort(10, 10, 151, 21) == REJECTED
