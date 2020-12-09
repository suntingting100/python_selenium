import csv # 导入csv包

# 读取csv文件
date = csv.reader(open("C:\\Users\\JRWX\\Desktop\\csv_read.csv", "r"))

# 循环输出每一行信息
# for user in date:
#     print(user)

# 获取用户的邮箱地址
for mail in date:
    print(mail[1])
