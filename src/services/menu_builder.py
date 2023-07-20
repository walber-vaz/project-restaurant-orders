from typing import Dict, List

from services.inventory_control import InventoryMapping
from services.menu_data import MenuData

DATA_PATH = "data/menu_base_data.csv"
INVENTORY_PATH = "data/inventory_base_data.csv"


class MenuBuilder:
    def __init__(self, data_path=DATA_PATH, inventory_path=INVENTORY_PATH):
        self.menu_data = MenuData(data_path)
        self.inventory = InventoryMapping(inventory_path)

    def make_order(self, dish_name: str) -> None:
        try:
            curr_dish = [
                dish
                for dish in self.menu_data.dishes
                if dish.name == dish_name
            ][0]
        except IndexError:
            raise ValueError("Dish does not exist")

        self.inventory.consume_recipe(curr_dish.recipe)

    # Req 4
    def get_main_menu(self, restriction=None) -> List[Dict]:
        """
        Returns the main menu of available dishes based on the given
        restriction.

        Args:
            restriction (Optional[str]): A string representing a dietary
            restriction.
                Defaults to None.

        Returns:
            List[Dict]: A list of dictionaries representing each dish in the
            main menu.
                Each dictionary contains the following keys:
                - 'dish_name': The name of the dish (str).
                - 'ingredients': The ingredients of the dish (List[str]).
                - 'price': The price of the dish (float).
                - 'restrictions': The dietary restrictions associated with the
                dish (List[str]).
        """
        menu = []

        for dish in self.menu_data.dishes:
            if (
                restriction is None
                or restriction not in dish.get_restrictions()
            ):
                ingredients_available = all(
                    self.inventory.inventory.get(ingredient, 0) > 0
                    for ingredient in dish.get_ingredients()
                )
                if ingredients_available:
                    menu.append(
                        {
                            'dish_name': dish.name,
                            'ingredients': dish.get_ingredients(),
                            'price': dish.price,
                            'restrictions': dish.get_restrictions(),
                        }
                    )

        return menu
