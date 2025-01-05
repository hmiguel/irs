import json
import metadata

def dic_to_json(output_file: str = "metadata.json"):
    data = metadata.irs
    with open(output_file, "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)

def generate_county_data(input_file: str, output_file: str):

    # Read the content of the file
    with open(input_file, "r", encoding="utf-8") as file:
        lines = file.readlines()

    # Initialize a list to store the processed data
    result = {}

    # Process each line, skipping the header
    for line in lines:
        # Split the columns by tabs
        columns = line.strip().split("\t")
        if len(columns) < 3:
            continue  # Skip malformed lines

        # Extract the data
        county = columns[0]
        tax = float(columns[1].replace("%", "").replace(",", ".").strip()) / 100 if "%" in columns[1] else 0.0

        result[county.lower()] = tax

    # Write the result to a JSON file
    with open(output_file, "w", encoding="utf-8") as json_file:
        json.dump(result, json_file, indent=4, ensure_ascii=False)

    print(f"Data successfully converted to JSON and saved to '{output_file}'.")

if __name__ == "__main__":
    #generate_county_data("county_2024.txt", "county_data_2024.json")
    dic_to_json("metadata.json")