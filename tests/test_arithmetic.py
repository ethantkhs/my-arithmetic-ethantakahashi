import pytest

from my_arithmetic_ethantakahashi.arithmetic import pgcd


@pytest.mark.parametrize(
    ("a", "b", "attendu"),
    [
        (12, 18, 6),
        (18, 12, 6),
        (17, 5, 1),     # nombres premiers entre eux
        (7, 7, 7),
        (0, 5, 5),
        (5, 0, 5),
        (0, 0, 0),
        (-12, 18, 6),   # nombres négatifs
        (12, -18, 6),
        (-12, -18, 6),
    ],
)
def test_pgcd(a, b, attendu):
    assert pgcd(a, b) == attendu