import os
import csv
from code_splitter.any_code_splitter import parse_file
from calculate_info_score import calculate_info_score

def process_project_files(project_path, output_file):
    # Open the file for writing
    with open(output_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(["relative_path", "info_score", "block"])  # Write the header

        # Traverse all files in the directory and its subdirectories
        for root, _, files in os.walk(project_path):
            for file in files:
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, project_path)
                try:
                    # Use parse_file to process the file
                    result = parse_file(file_path)
                    # Calculate the information score and write it to the file
                    for block in result:
                        info_score = calculate_info_score(block)
                        writer.writerow([relative_path, info_score, block])
                except ValueError as e:
                    # Skip unsupported file types
                    print(f"Skipped file {relative_path}: {e}")
                except Exception as e:
                    # Catch other exceptions
                    print(f"Error processing file {relative_path}: {e}")

def read_from_csv(input_file):
    # Read data from the CSV file
    with open(input_file, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=',', quotechar='"')
        for row in reader:
            print(f"relative_path: {row[0]}, info_score: {row[1]}, block: {row[2]}")

if __name__ == "__main__":
    project_path = "../large_scale_project"
    output_file = "./temp/output.csv"
    process_project_files(project_path, output_file)
    read_from_csv(output_file)