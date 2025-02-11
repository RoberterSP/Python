import smtplib
from email import __version__ as email_version

try:
    # 尝试导入 smtplib 和 email 库
    import smtplib
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    print("smtplib 和 email 库已安装。")
    print(f"email 库版本: {email_version}")
except ImportError:
    print("smtplib 或 email 库未安装。")
