import csv
from UserInputs.input_list import allSubCategories

# Sub-Category list in the script
scriptSubCategories = allSubCategories.inputList

def editSnowSubCategories():
    # Read the CSV and populate the set
    # Rows in csv, Sub-Category list in snow (Value)
    rows, snowSubCategories = readCsv([], set())

    # Capture snow sub-categories that don't match the script category
    # {normalized value : correct casing}
    wrongSnowSubCategories = {}

    for subcat in scriptSubCategories:
        if subcat == '':
            continue

        normalized_value = subcat.lower().replace(' ', '')
        wrongSnowSubCategories[normalized_value] = subcat

    for row in rows:
        original_value = row.get("Value")
        if original_value:
            normalized_value = original_value.lower().replace(' ', '')
            if normalized_value in wrongSnowSubCategories:
                # print(f"Key: {normalized_value}, Value: {wrongSnowSubCategories[normalized_value]}")
                row["Value"] = wrongSnowSubCategories[normalized_value]

    # Write updated data to a new CSV
    output_file_path = '../Csv-files/subcat-snow.csv'
    with open(output_file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)

    print("CSV updated and saved to", output_file_path)


def readCsv(rows, snowSubCategories):
    csv_file_path = '../Csv-files/subcat-snow.csv'

    # Read the CSV and populate the set
    with open(csv_file_path, mode='r', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        for row in reader:
            value = row.get("Value")
            if value:
                snowSubCategories.add(value)
            rows.append(row)

    return rows, snowSubCategories

# Call methods
editSnowSubCategories()