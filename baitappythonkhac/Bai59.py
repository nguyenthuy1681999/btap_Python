#Tương tự như bài 58, nhưng lần này ta sẽ viết hàm để lấy companyname.
import re


def inRaCompanyname():
    email = input("Nhập vào email:")
    rex = "(\w+)@(\w+)(\.com)"
    rs = re.match(rex,email)
    print(rs.group(2))
inRaCompanyname()