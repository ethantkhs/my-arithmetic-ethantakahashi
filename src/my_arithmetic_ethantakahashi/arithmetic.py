"""Fonctions arithmétiques."""


def pgcd(a: int, b: int) -> int:
    """Calcule le plus grand commun diviseur de deux entiers.

    Parameters
    ----------
    a : int
        Premier entier.
    b : int
        Second entier.

    Returns
    -------
    int
        Le PGCD de `a` et `b` (toujours positif ou nul).

    Examples
    --------
    >>> pgcd(12, 18)
    6
    """
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a