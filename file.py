import os
import shutil

def write_file():
    # 打开文件
    with open('./file/demo.text', 'a') as file:
        # 写入文件内容
        for i in range(1000):
            file.write(str(i) + '\n')

def clean_file():
    # 打开文件
    with open('./file/demo.text', 'w') as file:
        # 写入文件内容
        file.write('')
    with open('./file/demo_copy.text', 'w') as file:
        # 写入文件内容
        file.write('')

def read_file():
    # 打开文件
    with open('./file/demo.text', 'r') as file:
        # 读取文件内容
        content = file.read()
        # 打印文件内容
        print(content)

def read_file_line(defaultIndex=0):
    # 打开文件
    with open('./file/demo.text', 'r') as file:
        # 读取文件所有行内容
        content = file.readlines()
        # 打印指定行的内容
        print(content[defaultIndex])
def copy_even_lines(input_file_path, output_file_path):
    """
    从输入文件中复制偶数行到输出文件

    :param input_file_path: 输入文件的路径
    :param output_file_path: 输出文件的路径
    :return: 无
    """
    with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
        for index, line in enumerate(input_file):
            if index % 56 == 0:  # 检查行号是否为偶数
                output_file.write(line)


def chmod_file():
    # 修改文件权限
    os.chmod('./file/demo.text', 0o777)

def copy_file():
    # 复制文件
    shutil.copy('./file/demo.text', './file/demo_copy.text')




