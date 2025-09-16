import ast
import re
from collections import defaultdict
from UserInputs.input_string import add_cat, add_subcat
from UserInputs.input_list import allCategories, allSubCategories

# ***Call functions at the bottom of the file***

# Ex: addOptions(subCat, ['', 'Access', 'Broken Functionality', 'Content']);
add_subcat = add_subcat.inputString

# Ex: addOptions(category, ['', 'Atlas']);
add_cat = add_cat.inputString

# allCategories = []
allCategories = allCategories.inputList

# allSubCategories = []
allSubCategories = allSubCategories.inputList

# Generate addOptions(category, {value})
def generateCatOptions():
    # Key: subCat, Value: category []
    d = defaultdict(list)

    # Regex to match each case block
    pattern = r"case\s+'([^']+)':\s+addOptions\(subCat,\s+(\[.*?\])\);"

    # Find all matches
    matches = re.findall(pattern, add_subcat, re.DOTALL)

    # Process each match
    processMatches(d, matches, allCategories)

    # Hold code for subcat filter
    add_options_category_string = ""

    # Example: print the dictionary
    for key, value in d.items():
        # Uncomment to view key-value pairs
        # print(f"{key}: {value}")

        # Sort the list of categories
        sorted_value = sorted(value)

        add_options_category_string += f"case '{key.upper()}':\n"
        add_options_category_string += f"\taddOptions(category, {sorted_value});\n"
        add_options_category_string += f"\tbreak;\n"
        add_options_category_string += "\n"

        # output_string += f"\t'{key}',\n"

    print(add_options_category_string)

# Generate addOptions(subCat, {value})
def generateSubCatOptions():
    # Key: subCat, Value: category []
    d2 = defaultdict(list)

    # Regex to match each case block
    pattern2 = r"case\s+'([^']+)':\s+addOptions\(category,\s+(\[.*?\])\);"

    # Find all matches
    matches2 = re.findall(pattern2, add_cat, re.DOTALL)

    # Process each match
    processMatches(d2, matches2, allSubCategories)

    add_options_subcat_string = ""

    # Example: print the dictionary
    for key, value in d2.items():
        # Uncomment to view key-value pairs
        # print(f"{key}: {value}")

        # Sort the list of sub-categories
        sorted_value = sorted(value)

        add_options_subcat_string += f"case '{key.upper()}':\n"
        add_options_subcat_string += f"\taddOptions(subCat, {sorted_value});\n"
        add_options_subcat_string += f"\tbreak;\n"
        add_options_subcat_string += "\n"

        # output_string += f"\t'{key}',\n"

    print(add_options_subcat_string)

def processMatches(dictionaryName, matches, cat_or_subcat_list):
    # Make sure the list and addOptions align
    fixCasingDictionary = generateDictionary(cat_or_subcat_list)

    # Process each match
    for value, options_str in matches:
        try:
            # Safely evaluate the list string to a Python list
            options = ast.literal_eval(options_str)
            for option in options:
                if option:  # Skip empty string for key, but include it in the value list
                    if not dictionaryName[option]:  # Initialize with empty string if not already
                        dictionaryName[option].append('')

                    normalized_value = value.lower().replace(' ', '')
                    if normalized_value in fixCasingDictionary:
                        correctCase = fixCasingDictionary[normalized_value]
                        dictionaryName[option].append(correctCase)
        except Exception as e:
            print(f"Error parsing options for case '{value}': {e}")

def generateDictionary(list):
    cat_or_subcat = {}

    # Normalize key and assign it correct casing for value
    for item in list:
        normalize_item = item.lower().replace(' ', '')
        cat_or_subcat[normalize_item] = item

    return cat_or_subcat

# Call functions
# generateCatOptions()
generateSubCatOptions()