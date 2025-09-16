import csv
from UserInputs.input_string import add_subcat
import re
from UserInputs.input_list import allCategories

# Import input string from another file since its long
input_add_subcat_string = add_subcat.inputString

# Category list (dependent values) in the script
scriptCategories = allCategories.inputList

# Build casing dictionary to preserve original casing
category_casing = {cat.lower(): cat for cat in scriptCategories if cat != ''}

# Build Category & Sub-category combo list from the script
cat_subcat_combo = []

# Regex to extract category and subcategories
pattern = r"case\s+'(.+?)':\s+addOptions\(subCat,\s+\[(.*?)\]\);"

# Find all matches
matches = re.findall(pattern, input_add_subcat_string, re.DOTALL)

# Process each match
for category, subcats in matches:
    category_key = category.lower()
    if category_key in category_casing:
        formatted_category = category_casing[category_key]
        subcat_list = [sub.strip().strip("'\"") for sub in subcats.split(',') if sub.strip().strip("'\"") and sub.strip().strip("'\"") != 'None']
        for subcat in subcat_list:
            cat_subcat_combo.append((formatted_category,subcat))

# for combo in cat_subcat_combo:
#     print(combo)

# Category/Subcategory list in snow (Dependent value:Value)
snow_cat_subcat_combo = set()

# Path to your CSV file
csv_file_path = '../Csv-files/subcat-snow.csv'
rows = []

# Read the CSV and populate the set
with open(csv_file_path, mode='r', encoding='utf-8-sig') as file:
    reader = csv.DictReader(file)
    for row in reader:
        dependent_value = row.get("Dependent value")
        value = row.get("Value")

        # Add combo to set and add the row to rows list
        snow_cat_subcat_combo.add((dependent_value, value))
        rows.append(row)

# for combo in snow_cat_subcat_combo:
#     print(combo)

# Capture snow combos that don't match the script category
wrong_snow_combos = set()

for combo in cat_subcat_combo:
    if combo[1] == '':
        continue

    if combo not in snow_cat_subcat_combo:
        wrong_snow_combos.add(combo)

for key, value in wrong_snow_combos:
    print(f"{key} : {value}")

