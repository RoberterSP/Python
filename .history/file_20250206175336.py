# 打开文件
with open('demo.text', 'r') as file:
    # 读取文件内容
    content = file.read()
    # 打印文件内容
    print(content)