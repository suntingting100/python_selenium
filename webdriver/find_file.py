import os

# 定义文件目录
result_dir = "D:\\python file location\\report\\"

lists = os.listdir(result_dir)

# 重新按时间对目录下的文件进行排序
# os.path.getmtime()表示获取文件的最后修改时间
# 而dir代表一个文件夹的路径,所以要加上后面具体的文件（+"fn"也就是加上list元素）才能使用geetmtime方法
# sort是排序，要对元组排序，需要key=lambda
# getmtime 是获得文件的创建时间 正序
# os的用法：http://www.bubuko.com/infodetail-1457985.html
lists.sort(key=lambda fn: os.path.getmtime(result_dir+"\\"+fn))

print("最新文件为： " + lists[-1])
file = os.path.join(result_dir, lists[-1])
print(file)