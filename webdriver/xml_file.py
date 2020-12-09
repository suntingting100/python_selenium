from xml.dom import minidom

# 打开xml文档
dom = minidom.parse("info.xml")

# 得到文档元素对象
root = dom.documentElement

print(root.nodeName)
print(root.nodeValue)
print(root.nodeType)
print(root.ELEMENT_NODE)

# 获取任意标签名 getElementsByTagName可以通过标签名获取标签
tagname = root.getElementsByTagName("browser")
print(tagname[0].tagName)

tagname = root.getElementsByTagName("login")
print(tagname[1].tagName)

tagname = root.getElementsByTagName("province")
print(tagname[2].tagName)

# 获得标签的属性值  getAttribute()用于获取元素的属性值
logins = root.getElementsByTagName("login")
username = logins[0].getAttribute("username")
print(username)

password = logins[0].getAttribute("password")
print(password)

username = logins[1].getAttribute("username")
print(username)

password = logins[1].getAttribute("password")
print(password)

# 获得标签之间的数据
provinces = dom.getElementsByTagName("province")
citys = dom.getElementsByTagName("city")

p2 = provinces[1].firstChild.data
print(p2)

c1 = provinces[1].firstChild.data
print(c1)

c2 = citys[1].firstChild.data
print(c2)

