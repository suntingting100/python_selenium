import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart

# 发用邮箱服务器
smtpsever = "smtp.126.com"

# 发送邮箱用户和密码
username = "suntingting_100@126.com"
password = "123456a"

# 发送邮箱
sender = "suntingting_100@126.com"

# 接收邮箱
receiver = "617587058@qq.com"

# 发送邮件主题
subject = "Python email test"

# 发用的附件
sendfile = open("D:\\python file location\\report\\test.txt", "rb").read()

att = MIMEText(sendfile, "base64", "utf-8")
att["Content-Type"] = "application/octet-stream"
att["Content-Disposition"] = 'attachment; filename = "log.txt"'

msgRoot = MIMEMultipart("related")
msgRoot["subject"] = subject
msgRoot["from"] = "suntingting_100@126.com"
msgRoot["to"] = "617587058@qq.com"
msgRoot.attach(att)

# 编写邮件正文
msg = MIMEText("你好")
msg["subject"] = Header(subject, "utf-8")
msg["from"] = "suntingting_100@126.com"
msg["to"] = "617587058@qq.com"

# 连接发送邮件
smtp = smtplib.SMTP()
smtp.connect(smtpsever)
smtp.login(username, password)

smtp.sendmail(sender, receiver, msgRoot.as_string(), )
# smtp.sendmail(sender, receiver, msg.as_string())

smtp.quit()
