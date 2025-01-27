def is_bulky(width: int, height: int, length: int) -> bool:
    """Return true if bulky.
    If total volume greater than 1 million or any dimension greater or equal to 150cm.

    Args:
        width (int): The width of the package in cm
        height (int): The height of the package in cm
        length (int): The length of the package in cm
    Returns:
        int: Boolean true if the package has a volume greater than 1 million or any dimension is greater or equal to 150.
    """
    return (width * height * length >= 1_000_000) or (
        width >= 150 or height >= 150 or length >= 150
    )


def is_heavy(mass: int) -> bool:
    """A package is heavy if its mass is 20kg or more.


    Args:
        mass (int): mass of package in kg.

    Returns:
        int: A boolean true if package is heavier than or equal to 20kg.
    """
    return mass >= 20


def sort(width: int, height: int, length: int, mass: int) -> str:
    """Sorts packages by property.

    Args:
        width (int): The width of the package in cm
        height (int): The height of the package in cm
        length (int): The length of the package in cm
        mass (int): The weight of the package in kg

        Returns:
            str: A string containing the name of the stack where the package should go.
    """

    # Check if arguments are numbers.
    try:
        ls = [int(arg) for arg in [width, height, length, mass]]
    except ValueError:
        raise ValueError("Please use a numerical value for each argument please.")

    bulky = is_bulky(width, height, length)
    heavy = is_heavy(mass)
    if not heavy and not bulky:
        return "STANDARD"
    elif heavy and bulky:
        return "REJECTED"
    else:
        return "SPECIAL"
