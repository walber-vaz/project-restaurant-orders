from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction

import pytest


# Req 2
def test_dish():
    """
    Function to test the Dish class.

    This function creates two instances of the Dish class, `mocoto` and
    `feijoada`, with different names and prices. It then asserts that the
    `name` and `price` attributes of both instances have the expected values.

    Next, it asserts that the hash value of `mocoto` is not equal to the hash
    value of `feijoada`, and that the hash value of `mocoto` is equal to the
    hash value of a new instance of the Dish class with the same name and
    price as `mocoto`. It also asserts that `mocoto` is equal to a new
    instance of the Dish class with the same name and price as `mocoto`.

    The function then performs similar assertions for the `feijoada` instance.

    It asserts that the string representation of `mocoto` is equal to the
    expected string representation, and does the same for `feijoada`.

    The function uses `pytest.raises` to assert that creating a Dish instance
    with an invalid price raises a `TypeError` or `ValueError` as expected.

    It creates an instance of the Ingredient class named `ingredient_mocoto`,
      and adds it as a dependency to `mocoto` with a quantity of 1. It then
      asserts that `ingredient_mocoto` is in the list of ingredients of
      `mocoto` and that `Restriction.ANIMAL_DERIVED` is in the list of
      restrictions of `mocoto`.

    Similar assertions are performed for the `feijoada` instance.

    This function serves as a comprehensive test for the Dish class and its
    methods.
    """

    mocoto = Dish("Mocotó", 30.0)
    feijoada = Dish("Feijoada", 45.0)

    assert mocoto.name == "Mocotó"
    assert mocoto.price == 30.0

    assert feijoada.name == "Feijoada"
    assert feijoada.price == 45.0

    assert hash(mocoto) != hash(feijoada)
    assert hash(mocoto) == hash(Dish("Mocotó", 30.0))
    assert mocoto == Dish("Mocotó", 30.0)

    assert hash(feijoada) != hash(mocoto)
    assert hash(feijoada) == hash(Dish("Feijoada", 45.0))
    assert feijoada == Dish("Feijoada", 45.0)

    assert str(mocoto) == "Dish('Mocotó', R$30.00)"
    assert str(feijoada) == "Dish('Feijoada', R$45.00)"

    with pytest.raises(TypeError):
        Dish("Mocotó", "preço")  # type: ignore

    with pytest.raises(ValueError):
        Dish("Mocotó", -1.0)

    ingredient_mocoto = Ingredient("carne")
    mocoto.add_ingredient_dependency(ingredient_mocoto, 1)

    assert ingredient_mocoto in mocoto.get_ingredients()
    assert Restriction.ANIMAL_DERIVED in mocoto.get_restrictions()

    with pytest.raises(TypeError):
        Dish("Feijoada", "preço")  # type: ignore

    with pytest.raises(ValueError):
        Dish("Feijoada", -1.0)

    ingredient_feijoada = Ingredient("bacon")
    feijoada.add_ingredient_dependency(ingredient_feijoada, 1)

    assert ingredient_feijoada in feijoada.get_ingredients()
    assert Restriction.ANIMAL_DERIVED in feijoada.get_restrictions()
