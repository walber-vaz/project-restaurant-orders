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
    frango = Ingredient('frango')
    ovo = Ingredient('ovo')
    farinha = Ingredient('farinha')

    assert farinha != ovo
    assert farinha == farinha

    assert ovo.__hash__() != farinha.__hash__()
    assert ovo.__hash__() != frango.__hash__()
    assert ovo.__hash__() == ovo.__hash__()

    assert repr(ovo) == "Ingredient('ovo')"
    assert ovo.name == 'ovo'

    assert farinha.restrictions == {Restriction.GLUTEN}
