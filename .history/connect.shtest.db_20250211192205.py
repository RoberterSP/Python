import pyodbc

def connect_to_toad():
    # 连接字符串，根据你的实际情况修改
    connection_string = (

    )

    try:
        # 建立连接
        conn = pyodbc.connect(connection_string)
        print("Connected to Toad for SQL Server successfully!")

        # 创建游标
        cursor = conn.cursor()

        # 执行查询
        cursor.execute("select Name, Options from app_form_component where FormCode='cc4.servicetrack.entitytype.list'")

        rows = cursor.fetchall()

        # 获取查询结果
        for row in rows:
            print(row)

        # 关闭游标和连接
        cursor.close()
        conn.close()

    except Exception as e:
        print(f"Error connecting to Toad for SQL Server: {e}")

if __name__ == "__main__":
    connect_to_toad()
