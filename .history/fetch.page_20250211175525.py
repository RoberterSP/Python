import pyodbc

def connect_to_toad():
    # 连接字符串，根据你的实际情况修改
    connection_string = (
        "Driver=Microsoft SQL Server;"
        "Server=10.0.1.65"
        "Database=default;"
        "UID=sa;"
        "PWD=Ztan134524;"
    )

    try:
        # 建立连接
        conn = pyodbc.connect(connection_string)
        print("Connected to Toad for SQL Server successfully!")

        # 创建游标
        cursor = conn.cursor()

        # 执行查询
        cursor.execute("SELECT TOP 10 * FROM your_table_name")

        # 获取查询结果
        for row in cursor:
            print(row)

        # 关闭游标和连接
        cursor.close()
        conn.close()

    except Exception as e:
        print(f"Error connecting to Toad for SQL Server: {e}")

if __name__ == "__main__":
    connect_to_toad()
