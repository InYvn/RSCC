from compressor.support_compression_LLM import compress_context, initialize_model
import csv

# splitter_map -> rule_based -> code_compressor

def code_compressor(input_file, output_file, tokenizer, model):
    combined_soft_prompt = ""
    with open(input_file, mode='r', encoding='utf-8') as infile, open(output_file, mode='w', newline='',
                                                                      encoding='utf-8') as outfile:
        reader = csv.reader(infile, delimiter=',', quotechar='"')
        writer = csv.writer(outfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        # Write the header
        writer.writerow(["relative_path", "info_score", "block", "allocate_token", "soft_token"])

        for row in reader:
            soft_prompt = compress_context(tokenizer, model, row[2], row[3])
            combined_soft_prompt += soft_prompt  # Concatenate soft_prompt

            # Write the result to the file
            writer.writerow([row[0], row[1], row[2], row[3], soft_prompt])

    return combined_soft_prompt



def read_from_csv(input_file):
    # Read data from the CSV file
    with open(input_file, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=',', quotechar='"')
        for row in reader:
            print(f"relative_path: {row[0]}, info_score: {row[1]}, block: {row[2]}, allocate_token: {row[3]}")


if __name__ == "__main__":
    input_file = "./temp/ruled_output.csv"
    output_file = "./temp/compressed_output.csv"
    tokenizer, model = initialize_model()
    code_compressor(input_file, output_file, tokenizer, model)
    print(f"Processing results have been written to the file: {output_file}")
    read_from_csv(output_file)