import csv
from src.models.dish import Dish
from src.models.ingredient import Ingredient


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()
        self.load_menu_data(source_path)

    def load_menu_data(self, source_path: str) -> None:
        """
        Load menu data from a CSV file and populate the dishes and ingredients.

        Args:
            source_path (str): The path to the CSV file containing the menu
            data.

        Returns:
            None: This function does not return anything.
        """
        with open(source_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            dishes = {}
            for row in reader:
                dish_name = row['dish']
                dish_price = float(row['price'])
                ingredient_name = row['ingredient']
                recipe_amount = int(row['recipe_amount'])

                dish = dishes.get(dish_name)
                if dish is None:
                    dish = Dish(dish_name, dish_price)
                    dishes[dish_name] = dish
                    self.dishes.add(dish)

                ingredient = Ingredient(ingredient_name)
                dish.add_ingredient_dependency(ingredient, recipe_amount)
