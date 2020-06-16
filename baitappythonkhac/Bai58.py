#Giả sử rằng chúng ta có vài địa chỉ email dạng username@companyname.com,
# hãy viết một chương trình để in username của địa chỉ email cụ thể.
# Cả username và companyname chỉ bao gồm chữ cái.

#Ví dụ: Nếu cung cấp địa chỉ email QTM@quantrimang.com thì đầu ra sẽ là: QTM.
import re


def inUsername():
    email = input("Nhập vào email:")
    rex = "(\w+)@((\w+\.)+(com))"
    rs = re.match(rex,email)
    print(rs.group(1))
inUsername()