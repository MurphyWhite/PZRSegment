import os
import tkinter as tk
from tkinter import filedialog
import jieba


class App:
    def __init__(self, root):
        self.root = root
        self.input_directory = ''
        self.output_directory = ''

        # 创建并放置按钮和标签
        self.choose_input_button = tk.Button(root, text="选择输入目录", command=self.choose_input)
        self.choose_input_button.pack(padx=20, pady=10)

        self.choose_output_button = tk.Button(root, text="选择输出目录", command=self.choose_output)
        self.choose_output_button.pack(padx=20, pady=10)

        self.run_button = tk.Button(root, text="运行分词", command=self.run_script)
        self.run_button.pack(padx=20, pady=20)

        self.output_label = tk.Label(root, text="")
        self.output_label.pack(padx=20, pady=20)

    def choose_input(self):
        self.input_directory = filedialog.askdirectory()
        self.output_label.config(text=f"输入目录: {self.input_directory}\n输出目录: {self.output_directory}")

    def choose_output(self):
        self.output_directory = filedialog.askdirectory()
        self.output_label.config(text=f"输入目录: {self.input_directory}\n输出目录: {self.output_directory}")

    def run_script(self):
        # 如果输入和输出目录都已选择
        if self.input_directory and self.output_directory:
            # 运行 main.py
            self.segment_and_save()
        else:
            self.output_label.config(text="请先选择输入和输出目录.")

    def segment_and_save(self):

        # 确保输出目录存在，如果不存在则创建
        if not os.path.exists(self.output_directory):
            os.makedirs(self.output_directory)

        # 获取输入目录下所有的txt文件
        input_files = [f for f in os.listdir(self.input_directory) if f.endswith('.txt')]

        for input_file in input_files:
            input_path = os.path.join(self.input_directory, input_file)
            output_path = os.path.join(self.output_directory, input_file)

            # 打开原始文本文件
            with open(input_path, 'r', encoding='utf-8') as f:
                text = f.read()

            # 使用jieba进行分词
            seg_list = jieba.cut(text, cut_all=False)

            # 将分词结果保存到输出文件
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(' '.join(seg_list))


# 创建主窗口
root = tk.Tk()
root.title("分词工具")
app = App(root)

# 运行主循环
root.mainloop()
