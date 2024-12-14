import pandas as pd


def select_random_recipes(file_path, num_recipes=7):
    df = pd.read_excel(file_path)
    random_recipes = df.sample(n=min(num_recipes, len(df)))
    return random_recipes


def generate_ingredients_list(recipes):
    ingredients_set = set()  # Use a set to avoid duplicates
    ingredients_list = []  # Use a list to maintain order

    for index, recipe in recipes.iterrows():
        # Directly use the 'Ingredients' column without splitting or stripping
        ingredient = recipe['Ingredients']  # Get the ingredient string directly
        if ingredient and ingredient not in ingredients_set:  # Check if the ingredient is not empty and not a duplicate
            ingredients_set.add(ingredient)  # Add to the set to track duplicates
            ingredients_list.append(ingredient)  # Add the ingredient to the list

    # Join the ingredients with a comma and space (or any other delimiter)
    return '<br><br>'.join(ingredients_list)

# Example usage:
# file_path = 'path_to_your_excel_file.xlsx'
# recipes = select_random_recipes(file_path)
# ingredients = generate_ingredients_list(recipes)
# print(ingredients)
