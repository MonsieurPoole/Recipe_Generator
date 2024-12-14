import os
from jinja2 import Environment, FileSystemLoader
import pdfkit

def generate_ingredients_html(ingredients_list, output_file):
    # Set up Jinja2 environment
    templates_dir = os.path.join(os.path.dirname(__file__), 'Templates')  # Path to the templates folder
    env = Environment(loader=FileSystemLoader(templates_dir))
    template = env.get_template('ingredients_template.html')

    # Render the HTML with the ingredients data
    html_content = template.render(ingredients=ingredients_list)

    # Write the HTML content to a file
    with open(output_file, 'w') as f:
        f.write(html_content)

def generate_recipe_html(recipe, output_file):
    # Set up Jinja2 environment
    templates_dir = os.path.join(os.path.dirname(__file__), 'Templates')  # Path to the templates folder
    env = Environment(loader=FileSystemLoader(templates_dir))
    template = env.get_template('recipe_template.html')

    # Render the HTML with the recipe data
    html_content = template.render(recipe=recipe)

    # Write the HTML content to a file
    with open(output_file, 'w') as f:
        f.write(html_content)

def create_pdf_from_html(html_files, output_pdf_file):
    options = {
        'enable-local-file-access': None
    }

    pdfkit.from_file(html_files, output_pdf_file, options=options)  # Pass the options here

     #Delete the generated HTML files after creating the PDF
    for html_file in html_files:
        if not html_file.endswith('_template.html'):  # Avoid deleting template files
            try:
                os.remove(html_file)
                print(f"Deleted: {html_file}")
            except OSError as e:
                print(f"Error deleting file {html_file}: {e}")

# Example usage:
# ingredients_list = ['Ingredient 1', 'Ingredient 2']
# generate_ingredients_html(ingredients_list, 'ingredients.html')
# generate_recipe_html(recipe_data, 'recipe.html')
# create_pdf_from_html(['ingredients.html', 'recipe.html'], 'output.pdf')
