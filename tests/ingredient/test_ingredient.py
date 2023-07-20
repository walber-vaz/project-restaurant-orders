from src.models.ingredient import (
    Ingredient,
    Restriction,
)  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
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
