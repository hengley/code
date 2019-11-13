import bcrypt  
  
password = b"admin"  
 # 对password做1轮的加密，获得了加密之后的字符串hashed，形如：$2a$10$aoiufioadsifuaisodfuiaosdifasdf  
hashed = bcrypt.hashpw(password, bcrypt.gensalt())  
# 检查用户输入的password是否正确，其实bcrypt.hashpw()函数的第二个参数是salt，bcrypt自己来解析版本、cost和前22位的salt，所以这里可以把整个hash过的字符串传进去  
if bcrypt.hashpw(password, hashed) == hashed:  
     print(hashed)
     print("It Matches!")  
else:  
     print("It Does not Match :(")  