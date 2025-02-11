from flask import Flask, request, jsonify
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

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

@app.route('/send_email', methods=['POST'])
def send_email_api():
    data = request.get_json()
    sender_email = data.get('sender_email')
    sender_password = data.get('sender_password')
    receiver_email = data.get('receiver_email')
    subject = data.get('subject')
    message = data.get('message')

    if not all([sender_email, sender_password, receiver_email, subject, message]):
        return jsonify({'error': 'Missing required fields'}), 400

    try:
        send_email(sender_email, sender_password, receiver_email, subject, message)
        return jsonify({'message': 'Email sent successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

# 使用示例
sender_email = "shaopeng.chen@mcttechnology.cn"
sender_password = "Csp123456"
receiver_email = "13262851051@163.com"
subject = "这是一封测试邮件"
message = "你好，这是一封通过Python发送的测试邮件。"

send_email(sender_email, sender_password, receiver_email, subject, message)
