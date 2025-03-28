import os
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML

def generate_ingredients_html(meals_list, output_file):
    # Set up Jinja2 environment
    templates_dir = os.path.join(os.path.dirname(__file__), 'Templates')  # Path to the templates folder
    env = Environment(loader=FileSystemLoader(templates_dir))
    template = env.get_template('ingredients_template.html')

    # Render the HTML with the ingredients data
    # Check if meals_list is a list of dictionaries
    if isinstance(meals_list, list) and all(isinstance(meal, dict) for meal in meals_list):
        html_content = template.render(meals=meals_list)  # Pass the entire meals list
    else:
        html_content = template.render(ingredients=meals_list)  # Fallback to the old format

    # Write the HTML content to a file
    with open(output_file, 'w') as f:
        f.write(html_content)

def generate_recipe_html(recipe, output_file):
    # Set up Jinja2 environment
    templates_dir = os.path.join(os.path.dirname(__file__), 'Templates')  # Path to the templates folder
    env = Environment(loader=FileSystemLoader(templates_dir))
    template = env.get_template('recipe_template.html')

    # Define the path to the images directory
    images_dir = os.path.join(os.path.dirname(__file__), 'Images')  # Adjust this if necessary

    # Update the recipe to include the full image path
    if 'image_path' in recipe:
        recipe['image_path'] = os.path.join(images_dir, recipe['image_path'])

    # Render the HTML with the recipe data
    html_content = template.render(recipe=recipe)

    # Write the HTML content to a file
    with open(output_file, 'w') as f:
        f.write(html_content)

def create_pdf_from_html(html_files, output_pdf_file):
    # Combine HTML files into a single PDF
    HTML(string=''.join([open(html_file).read() for html_file in html_files])).write_pdf(output_pdf_file)

    # Delete the generated HTML files after creating the PDF
    for html_file in html_files:
        if not html_file.endswith('_template.html'):  # Avoid deleting template files
            try:
                os.remove(html_file)
                print(f"Deleted: {html_file}")
            except OSError as e:
                print(f"Error deleting file {html_file}: {e}")

# Example usage:
# meals_list = [{'Dinner_Name': 'Spaghetti Bolognese', 'Ingredients': '<P>3 cloves garlic</P>'}, ...]
# generate_ingredients_html(meals_list, 'ingredients.html')
# generate_recipe_html(recipe_data, 'recipe.html')
# create_pdf_from_html(['ingredients.html', 'recipe.html'], 'output.pdf')
