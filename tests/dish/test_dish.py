from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction

import pytest


# Req 2
def test_dish():
    acai = Dish("Açai", 10.0)
    vatapa = Dish("Vatapá", 15.0)

    assert acai.name == "Açai"
    assert acai.price == 10.0

    assert vatapa.name == "Vatapá"
    assert vatapa.price == 15.0

    assert hash(acai) != hash(vatapa)
    assert hash(acai) == hash(Dish("Açai", 10.0))
    assert acai == Dish("Açai", 10.0)

    assert hash(vatapa) != hash(acai)
    assert hash(vatapa) == hash(Dish("Vatapá", 15.0))
    assert vatapa == Dish("Vatapá", 15.0)

    assert str(acai) == "Dish('Açai', R$10.00)"
    assert str(vatapa) == "Dish('Vatapá', R$15.00)"

    with pytest.raises((TypeError, ValueError)):
        Dish("Açai", "preço")  # type: ignore

    with pytest.raises((TypeError, ValueError)):
        Dish("Açai", -1.0)

    ingredient_acai = Ingredient("carne")
    acai.add_ingredient_dependency(ingredient_acai, 1)

    assert ingredient_acai in acai.get_ingredients()
    assert Restriction.ANIMAL_DERIVED in acai.get_restrictions()

    with pytest.raises((TypeError, ValueError)):
        Dish("Vatapá", "preço")  # type: ignore

    with pytest.raises((TypeError, ValueError)):
        Dish("Vatapá", -1.0)

    ingredient_vatapa = Ingredient("camarão")
    vatapa.add_ingredient_dependency(ingredient_vatapa, 1)

    assert ingredient_vatapa in vatapa.get_ingredients()
    assert Restriction.ANIMAL_DERIVED in vatapa.get_restrictions()
