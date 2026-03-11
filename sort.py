def sort(width: float, height: float, length: float, mass: float) -> str:
    is_bulky = (
        width * height * length >= 1_000_000
        or width >= 150
        or height >= 150
        or length >= 150
    )
    is_heavy = mass >= 20

    if is_bulky and is_heavy:
        return "REJECTED"
    if is_bulky or is_heavy:
        return "SPECIAL"
    return "STANDARD"


def run_tests():
    cases = [
        (10, 10, 10, 5,          "STANDARD", "Small light package"),
        (149, 1, 1, 19,          "STANDARD", "Just under dimension threshold"),
        (10, 10, 9, 19.9,        "STANDARD", "Just under all thresholds"),
        (150, 1, 1, 5,           "SPECIAL",  "One dimension exactly 150"),
        (200, 1, 1, 5,           "SPECIAL",  "One dimension over 150"),
        (100, 100, 100, 5,       "SPECIAL",  "Volume exactly 1,000,000"),
        (200, 200, 200, 5,       "SPECIAL",  "Volume way over, light"),
        (10, 10, 10, 20,         "SPECIAL",  "Exactly 20kg, small"),
        (10, 10, 10, 50,         "SPECIAL",  "Very heavy, small"),
        (150, 1, 1, 20,          "REJECTED", "Bulky (dim) and heavy"),
        (100, 100, 100, 20,      "REJECTED", "Bulky (volume) and heavy"),
        (200, 200, 200, 100,     "REJECTED", "Massively bulky and heavy"),
        (0, 0, 0, 0,             "STANDARD", "Zero dimensions and mass"),
        (99.9, 99.9, 99.9, 19.9, "STANDARD", "Just under all thresholds (float)"),
        (100, 100, 100.001, 5,   "SPECIAL",  "Volume just over 1,000,000"),
    ]

    passed = failed = 0
    for width, height, length, mass, expected, desc in cases:
        result = sort(width, height, length, mass)
        ok = result == expected
        print(f"{'✅' if ok else '❌'} {desc}")
        if not ok:
            print(f"   Expected {expected}, got {result}")
            failed += 1
        else:
            passed += 1

    print(f"\n{passed}/{passed + failed} tests passed")


if __name__ == "__main__":
    run_tests()
