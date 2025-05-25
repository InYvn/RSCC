import os
import csv


def rule_based(input_file, output_file):
    with open(input_file, mode='r', encoding='utf-8') as infile, open(output_file, mode='w', newline='',
                                                                      encoding='utf-8') as outfile:
        reader = csv.reader(infile, delimiter=',', quotechar='"')
        writer = csv.writer(outfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        # Write the header
        writer.writerow(["relative_path", "info_score", "block", "allocate_token"])

        for row in reader:
            if len(row) < 3:
                continue

            if row[1].isdigit():  # Ensure info_score is a number
                info_score = int(row[1])
                if info_score < 50:
                    allocate_token = 1
                elif 50 <= info_score <= 100:
                    allocate_token = 2
                else:
                    allocate_token = 3

                # Write the result to the file
                writer.writerow([row[0], row[1], row[2], allocate_token])

def read_from_csv(input_file):
    # Read data from the CSV file
    with open(input_file, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=',', quotechar='"')
        for row in reader:
            print(f"relative_path: {row[0]}, info_score: {row[1]}, block: {row[2]}, allocate_token: {row[3]}")


if __name__ == "__main__":
    input_file = "./temp/output.csv"
    output_file = "./temp/ruled_output.csv"
    rule_based(input_file, output_file)
    print(f"Processing results have been written to the file: {output_file}")
    read_from_csv(output_file)