import csv
from UserInputs.input_list import allCategories

# Category list (dependent values) in the script
scriptCategories = allCategories.inputList

# Fix snow dependent values with incorrect casing/spacing
def editDependentValues():
    # Read the CSV and populate the set
    # Rows in csv, Category list in snow (Dependent Value)
    rows, snowDependentValues = readCsv([], set())

    # Capture snow dependent values that don't match the script category
    # {normalized value : correct casing}
    wrongDependentValues = {}

    for category in scriptCategories:
        if category == '':
            continue

        normalized_value = category.lower().replace(' ', '')
        wrongDependentValues[normalized_value] = category

    # for key, value in wrongDependentValues.items():
    #     print(f"{key} : {value}")

    for row in rows:
        original_value = row.get("Dependent value")
        if original_value:
            normalized_value = original_value.lower().replace(' ', '')
            if normalized_value in wrongDependentValues:
                # print(f"Key: {normalized_value}, Value: {wrongDependentValues[normalized_value]}")
                row["Dependent value"] = wrongDependentValues[normalized_value]

    # Write updated data to a new CSV
    output_file_path = '../Csv-files/subcat-snow.csv'
    with open(output_file_path, mode='w', encoding='utf-8-sig', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)

    print("CSV updated and saved to", output_file_path)

def readCsv(rows, snowDependentValues):
    csv_file_path = '../Csv-files/subcat-snow.csv'

    # Read the CSV and populate the set
    with open(csv_file_path, mode='r', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        for row in reader:
            dependent_value = row.get("Dependent value")
            if dependent_value:
                normalized_dependent_value = dependent_value.lower().replace(' ', '')
                snowDependentValues.add(normalized_dependent_value)
            rows.append(row)

    return rows, snowDependentValues

# Call methods
editDependentValues()