import csv
from UserInputs.input_list import allCategories

# Category list in the script
scriptCategories = allCategories.inputList

# Fix snow categories with incorrect casing/spacing
def editSnowCategories():
    # Read the CSV and populate the set
    # Rows in csv, Category list in snow (Value)
    rows, snowCategories = readCsv([], set())

    # Capture snow categories that don't match the script category
    # {normalized value : correct casing}
    wrongSnowCategories = {}

    for category in scriptCategories:
        if category == '':
            continue

        if category not in snowCategories:
            normalized_value = category.lower().replace(' ', '')
            wrongSnowCategories[normalized_value] = category

    # for key, value in wrongSnowCategories.items():
    #     print(f"{key} : {value}")

    for row in rows:
        original_value = row.get("Value")
        if original_value:
            normalized_value = original_value.lower().replace(' ', '')
            if normalized_value in wrongSnowCategories:
                # print(f"Key: {normalized_value}, Value: {wrongSnowCategories[normalized_value]}")
                row["Value"] = wrongSnowCategories[normalized_value]

    # Write updated data to the CSV
    output_file_path = '../Csv-files/category-snow.csv'
    with open(output_file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)

    print("CSV updated and saved to", output_file_path)


# Look for a script category that isn't in snow at all
def scriptCategoriesInSnow():
    categoriesMissingFromSnow = []

    # Read the CSV and populate the set
    rows, snowCategories = readCsv([], set())

    for category in scriptCategories:
        if category == '':
            continue

        if category not in snowCategories:
            categoriesMissingFromSnow.append(category)

    print("Missing from snow categories / possibly set to inactive / misspelled")
    for category in categoriesMissingFromSnow:
        print(category)


def readCsv(rows, snowCategories):
    csv_file_path = '../Csv-files/category-snow.csv'

    # Read the CSV and populate the set
    with open(csv_file_path, mode='r', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        for row in reader:
            value = row.get("Value")
            inactive = row.get("Inactive")
            if value and inactive == 'FALSE':
                snowCategories.add(value)
            rows.append(row)

    return rows, snowCategories

# Call functions
# editSnowCategories()
scriptCategoriesInSnow()