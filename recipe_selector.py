import pandas as pd
import os
from jinja2 import Environment, FileSystemLoader
import pdfkit

def select_random_recipes(file_path, num_recipes=7):
    df = pd.read_excel(file_path)
    random_recipes = df.sample(n=min(num_recipes, len(df)))
    return random_recipes

def generate_ingredients_list(recipes):
    meals_list = []  # List to hold meal dictionaries

    for index, recipe in recipes.iterrows():
        # Create a dictionary for each meal
        meal = {
            'Dinner_Name': recipe['Dinner_Name'],  # Assuming you have a 'Dinner_Name' column
            'Ingredients': recipe['Ingredients'].replace('\n', '<br>')  # Replace line breaks with <br>
        }
        meals_list.append(meal)  # Add the meal dictionary to the list

    return meals_list  # Return the list of meals

def generate_ingredients_html(meals_list, output_file):
    # Set up Jinja2 environment
    templates_dir = os.path.join(os.path.dirname(__file__), 'Templates')  # Path to the templates folder
    env = Environment(loader=FileSystemLoader(templates_dir))
    template = env.get_template('ingredients_template.html')

    # Render the HTML with the meals data
    html_content = template.render(meals=meals_list)  # Pass the entire meals list

    # Write the HTML content to a file
    with open(output_file, 'w') as f:
        f.write(html_content)

# Example usage
file_path =os.path.join('Data', 'Recipe_DB.xlsx') # Replace with your actual file path
random_recipes = select_random_recipes(file_path)
meals = generate_ingredients_list(random_recipes)

# Generate the ingredients HTML page
generate_ingredients_html(meals, 'ingredients.html')
