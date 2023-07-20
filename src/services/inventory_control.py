from csv import DictReader
from typing import Dict

from src.models.dish import Recipe
from src.models.ingredient import Ingredient

BASE_INVENTORY = "data/inventory_base_data.csv"

Inventory = Dict[Ingredient, int]


def read_csv_inventory(inventory_file_path=BASE_INVENTORY) -> Inventory:
    inventory = dict()

    with open(inventory_file_path, encoding="utf-8") as file:
        for row in DictReader(file):
            ingredient = Ingredient(row["ingredient"])
            inventory[ingredient] = int(row["initial_amount"])

    return inventory


# Req 5
class InventoryMapping:
    def __init__(self, inventory_file_path=BASE_INVENTORY) -> None:
        self.inventory = read_csv_inventory(inventory_file_path)

    # Req 5.1

    def check_recipe_availability(self, recipe: Recipe) -> bool:
        """
        Check if all the ingredients in a recipe are available in the
        inventory.

        Parameters:
            recipe (Recipe): A dictionary containing the ingredients and their
            required amounts.

        Returns:
            bool: True if all the ingredients are available in the inventory
            and their amounts are sufficient, False otherwise.

        # Req 5.1
        """
        return all(
            ingredient in self.inventory
            and self.inventory[ingredient] >= amount
            for ingredient, amount in recipe.items()
        )

        # Req 5.2

    def consume_recipe(self, recipe: Recipe) -> None:
        """
        Consumes a recipe by subtracting the required amounts of ingredients
        from the inventory.

        Parameters:
            recipe (Recipe): The recipe to be consumed.

        Raises:
            ValueError: If the recipe is not available in the inventory.

        Returns:
            None

        # Req 5.2
        """
        if not self.check_recipe_availability(recipe):
            raise ValueError("Recipe is not available")

        self.inventory = {
            ingredient: self.inventory[ingredient] - amount
            for ingredient, amount in recipe.items()
        }
