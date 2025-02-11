
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, sender_password, receiver_email, subject, message):
    # 创建一个多部分消息
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # 添加消息正文
    msg.attach(MIMEText(message, 'plain'))

    # 创建SMTP会话
    with smtplib.SMTP('smtp.gmail.com', 587) as server:  # 使用Gmail的SMTP服务器，端口587
        server.starttls()  # 启用TLS加密
        server.login(sender_email, sender_password)  # 登录到SMTP服务器
        server.send_message(msg)  # 发送邮件

# 使用示例
sender_email = ""
sender_password = "your_email_password"
receiver_email = "recipient_email@example.com"
subject = "这是一封测试邮件"
message = "你好，这是一封通过Python发送的测试邮件。"

send_email(sender_email, sender_password, receiver_email, subject, message)
