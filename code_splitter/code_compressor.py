from compressor.support_compression_LLM import compress_context,initialize_model
import csv

# splitter_map -> rule_based -> code_compressor

def code_compressor(input_file, output_file, tokenizer, model):
    with open(input_file, mode='r', encoding='utf-8') as infile, open(output_file, mode='w', newline='',
                                                                      encoding='utf-8') as outfile:
        reader = csv.reader(infile, delimiter=',', quotechar='"')
        writer = csv.writer(outfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        # 写入表头
        writer.writerow(["relative_path", "info_score", "block", "allocate_token", "soft_token"])

        for row in reader:
            soft_prompt = compress_context(tokenizer, model, row[3])

            # 将结果写入文件
            writer.writerow([row[0], row[1], row[2], row[3], soft_prompt])



def read_from_csv(input_file):
    # 从 CSV 文件中读取数据
    with open(input_file, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=',', quotechar='"')
        for row in reader:
            print(f"relative_path: {row[0]}, info_score: {row[1]}, block: {row[2]}, allocate_token: {row[3]}")


if __name__ == "__main__":
    input_file = "./temp/ruled_output.csv"
    output_file = "./temp/compressed_output.csv"
    tokenizer, model = initialize_model()
    code_compressor(input_file, output_file, tokenizer, model)
    print(f"处理结果已写入文件: {output_file}")
    read_from_csv(output_file)