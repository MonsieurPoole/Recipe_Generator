# Recipe_Generator
Recipe Generator is based on the Aldi grocery store. It contains about 8 months of weekly 7-day meals.
The first page lists all of the ingredients for each of the 7 randomly selected meals, for easier review when grocery shopping.
The servings may be per adult or how many items the ingredients make, such as 4 spring rolls.


You can add new recipes to the database by accessing ~/Data/Recipe_DB.xlsx. Do not use ODS/other format(s).
If you wish to add new columns to the DB, please be sure to use JINJA2 syntax in your HTML code to reference the header(s).
If you wish to add a new picture of a meal, please save a PNG image in ~/Images/ and include the name of the .PNG to Recipe_DB.xlsx. 
If you wish to modify or create another HTML template, either keep the existing template names, such as "ingredients_template.html", or by updating the name of the HTML file in the pdf_generator.py module.

*If you are on Linux, and using a flatpak version of your main web browser, ensure your permissions are set to 'allow /user access', otherwise, the images will not print to pdf.*

Lastly, I highly recommend setting a chron job to run the main.py weekly so that you have a new PDF waiting for you on your grocery shopping day. 
