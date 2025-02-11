
def write_file():
    # 打开文件
    with open('./file/demo.text', 'w') as file:
        # 写入文件内容
        for i in range(1000):
            file.write(str(i) + '\n')

def clean_file():
    # 打开文件
    with open('./file/demo.text', 'w') as file:
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
    """
    读取文件的指定行内容

    :param defaultIndex: 要读取的行索引，默认为0
    :return: 无
    """
    # 打开文件
    with open('./file/demo.text', 'r') as file:
        # 读取文件所有行内容
        content = file.readlines()
        # 打印指定行的内容
        print(content[defaultIndex])