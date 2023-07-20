from src.models.ingredient import (
    Ingredient,
    Restriction,
)  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    """
    Test the Ingredient class by creating instances and asserting various
    conditions.

    This function creates instances of the Ingredient class using different
    names, such as 'frango', 'ovo', and 'farinha'.
    It then performs assertions to test the behavior of the Ingredient class.

    Parameters:
        None

    Returns:
        None
    """
    ingredients = ['frango', 'ovo', 'farinha']
    frango, ovo, farinha = [Ingredient(name) for name in ingredients]

    assert farinha != ovo
    assert farinha == farinha

    assert hash(ovo) != hash(farinha)
    assert hash(ovo) != hash(frango)
    assert hash(ovo) == hash(ovo)

    assert repr(ovo) == "Ingredient('ovo')"
    assert ovo.name == 'ovo'

    assert farinha.restrictions == {Restriction.GLUTEN}
