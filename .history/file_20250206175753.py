# 打开文件
with open('./file/demo.text', 'r') as file:
    # 读取文件内容
    content = file.read()
    # 打印文件内容
    print(content)



with open('./file/demo.text', 'w') as file:
    # 写入文件内容
    file.write('')