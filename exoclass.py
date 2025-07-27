# Mariza
"""
Ce programm definit une hierachie de classes pour gerer des plats dans un menu de restaurant.
La classe de base 'Dish' represente  un plat avec des attributs: nom(name), temp de preparation(prep_time), prix(price) et ingredients.
Les classes derivees plat princpal(MainCourse) et Dessert heritent de 'Dish'.
Le code ajoute aussi fes methodes specifiques telles que : accompagnement(side_dish) pour les plats principaux, niveau de sucre (Sugar_level) pour le niveau de sucre

"""
# Class parent
class Dish:
    def __init__(self,name,prep_time,price,ingredients):
        self.name = name
        self.prep_time = prep_time # in minutes
        self.price = price # in euros
        self.ingredients = ingredients # list of ingredients

    # Method to display dish information
    def display_info(self):
        return (
            f"Dish: {self.name}, Price:{self.price}€, Prep Time:{self.prep_time} min."
            f"{self.ingredients}")

    # Method to estimate serving time
    def estimate_serving_time(self):
        return f"The dish {self.name} will be ready in {self.prep_time} minutes."

    # Method to check if the dish is vegetarian
    def is_vegetarian(self):
        non_vegetarian_ingredients = ['chicken', 'beef', 'pork', 'shrimp', 'lamb', 'milk', 'chocolate', 'gelatin']
        return not any(ingredient.lower() in non_vegetarian_ingredients for ingredient in self.ingredients)

    # Method to add an ingredient to the dish
    def add_ingredient(self, new_ingredient):
        if new_ingredient not in self.ingredients:
            self.ingredients.append(new_ingredient)
            return f"{new_ingredient} added to dish {self.name}"
        return f"{new_ingredient} is already in dish {self.name}"


# Class for main courses
class MainCourse(Dish):
    def __init__(self, name, prep_time, price, ingredients, side_dish):
        super().__init__(name, prep_time, price, ingredients)
        self.side_dish = side_dish

    # Override display_info method
    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, Side Dish: {self.side_dish}"

    # Method to change the side dish
    def change_side_dish(self, side_dish):
        old_side_dish = self.side_dish
        self.side_dish = side_dish
        return f"Side dish for '{self.name}' changed from {old_side_dish} to {side_dish}."
# Class for Dessert
class Dessert(Dish):
    def __init__(self, name, prep_time, price, ingredients, sugar_level):
        super().__init__(name, prep_time, price, ingredients)
        self.sugar_level = sugar_level # low, meduim, high

    # Override display_info method
    def diplay_info(self):
        base_info = super().display_info()
        return f"{base_info}, Sugar Level: {self.sugar_level}"

    # Method to adjust sugar level
    def adjust_sugar(self,new_level):
        valid_levels =['low','medium','high']
        if new_level not in valid_levels:
            self.sugar_level = new_level
            return f"Sugar level for '{self.name}' adjusted to {new_level}."
        return f"Level {new_level} is invalid choose from {valid_levels}."

# Examples
if __name__ == '__main__':
    # Create a main Course
    main_dish = MainCourse("Chicken Tikka Masala",45,15.99,['chicken','tomato', 'cream', 'spices'], "basmati rice")
    print (main_dish.display_info())
    print (main_dish.estimate_serving_time())
    print (main_dish.is_vegetarian())
    print (main_dish.add_ingredient('ginger'))
    print (main_dish.change_side_dish("naan"))
    print (main_dish.display_info())

    # Create Dessert
    dessert = Dessert("Apple Pie", 30, 6.50, ['apples', 'pie crust', 'sugar','cinamon', 'milk'], "meduim")
    print (f"Dessert:{dessert.diplay_info()}")
    print (dessert.estimate_serving_time())
    print (dessert.is_vegetarian())
    print (dessert.adjust_sugar('low'))
    print (dessert.display_info())




