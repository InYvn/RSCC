import os
import csv
from code_splitter.any_code_splitter import parse_file
from calculate_info_score import calculate_info_score

def process_project_files(project_path, output_file):
    # 打开文件进行写入
    with open(output_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(["relative_path", "info_score", "block"])  # 写入表头

        # 遍历目录及其子目录中的所有文件
        for root, _, files in os.walk(project_path):
            for file in files:
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, project_path)
                try:
                    # 使用 parse_file 处理文件
                    result = parse_file(file_path)
                    # 计算信息分数并写入文件
                    for block in result:
                        info_score = calculate_info_score(block)
                        writer.writerow([relative_path, info_score, block])
                except ValueError as e:
                    # 跳过不支持的文件类型
                    print(f"跳过文件 {relative_path}: {e}")
                except Exception as e:
                    # 捕获其他异常
                    print(f"处理文件 {relative_path} 时出错: {e}")

def read_from_csv(input_file):
    # 从 CSV 文件中读取数据
    with open(input_file, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=',', quotechar='"')
        for row in reader:
            print(f"relative_path: {row[0]}, info_score: {row[1]}, block: {row[2]}")

if __name__ == "__main__":
    project_path = "../large_scale_project"
    output_file = "./temp/output.csv"
    process_project_files(project_path, output_file)
    read_from_csv(output_file)

