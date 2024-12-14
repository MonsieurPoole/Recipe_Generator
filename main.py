import os
from jinja2 import Environment, FileSystemLoader
from recipe_selector import select_random_recipes, generate_ingredients_list
from pdf_generator import generate_ingredients_html, generate_recipe_html, create_pdf_from_html


def main():
    # Get the current directory
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Define relative paths for the Excel file and output PDF
    file_path = os.path.join(base_dir, 'Data', 'Recipe_DB.xlsx')
    output_pdf_file = os.path.join(base_dir, 'Recipe', '7_random_recipes.pdf')

    # Create output directory if it doesn't exist
    output_dir = os.path.join(base_dir, 'output')
    os.makedirs(output_dir, exist_ok=True)

    # Load the Excel database
    random_recipes = select_random_recipes(file_path)

    # Construct image paths
    images_dir = os.path.join(base_dir, 'Images')  # Path to the Images folder
    random_recipes['image_path'] = random_recipes['Image_Path'].apply(lambda x: os.path.join(images_dir, x))

    # Set up Jinja2 environment for templates
    templates_dir = os.path.join(base_dir, 'templates')
    Environment(loader=FileSystemLoader(templates_dir))

    # Generate HTML for ingredients
    ingredients_list = generate_ingredients_list(random_recipes)
    ingredients_html_file = os.path.join(output_dir, 'ingredients.html')
    generate_ingredients_html(ingredients_list, ingredients_html_file)

    # Generate HTML for each recipe
    recipe_html_files = []
    for index, recipe in random_recipes.iterrows():
        recipe_html_file = os.path.join(output_dir, f'recipe_{index + 1}.html')
        generate_recipe_html(recipe, recipe_html_file)
        recipe_html_files.append(recipe_html_file)

    # Combine all HTML files into a single PDF
    html_files_to_convert = [ingredients_html_file] + recipe_html_files
    create_pdf_from_html(html_files_to_convert, output_pdf_file)

if __name__ == "__main__":
    main()