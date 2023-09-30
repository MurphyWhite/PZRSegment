import os
import requests
import sys
import subprocess
import jieba


def check_for_updates(current_version, update_url):
    # 发送请求检查是否有新版本
    response = requests.get(update_url)
    new_version = response.text.strip()

    if new_version != current_version:
        return new_version
    else:
        return None


def download_update(update_url, download_path):
    # 下载新版本
    response = requests.get(update_url)
    with open(download_path, 'wb') as f:
        f.write(response.content)


def update_program(update_url, current_version, program_path):
    # 获取新版本号
    new_version = check_for_updates(current_version, update_url)

    if new_version:
        # 下载新版本
        download_path = 'new_version.zip'
        download_update(update_url, download_path)

        # 替换当前程序文件
        os.replace(download_path, program_path)

        # 重新启动程序
        subprocess.Popen([sys.executable, program_path])
        sys.exit()


def segment_and_save(input_dir, output_dir):
    # 确保输出目录存在，如果不存在则创建
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 获取输入目录下所有的txt文件
    input_files = [f for f in os.listdir(input_dir) if f.endswith('.txt')]

    for input_file in input_files:
        input_path = os.path.join(input_dir, input_file)
        output_path = os.path.join(output_dir, input_file)

        # 打开原始文本文件
        with open(input_path, 'r', encoding='utf-8') as f:
            text = f.read()

        # 使用jieba进行分词
        seg_list = jieba.cut(text, cut_all=False)

        # 将分词结果保存到输出文件
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(' '.join(seg_list))


if __name__ == "__main__":
    # 设置输入和输出目录
    input_directory = 'origin'
    output_directory = 'output'

    # 执行分词并保存
    segment_and_save(input_directory, output_directory)