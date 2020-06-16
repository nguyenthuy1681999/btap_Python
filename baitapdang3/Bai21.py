#Một website yêu cầu người dùng nhập tên người dùng và mật khẩu để đăng ký.
# Viết chương trình để kiểm tra tính hợp lệ của mật khẩu mà người dùng nhập vào.

#Các tiêu chí kiểm tra mật khẩu bao gồm:

#1. Ít nhất 1 chữ cái nằm trong [a-z]
#2. Ít nhất 1 số nằm trong [0-9]
#3. Ít nhất 1 kí tự nằm trong [A-Z]
#4. Ít nhất 1 ký tự nằm trong [$ # @]
#5. Độ dài mật khẩu tối thiểu: 6
#6. Độ dài mật khẩu tối đa: 12

#Chương trình phải chấp nhận một chuỗi mật khẩu phân tách nhau bởi dấu phẩy
# và kiểm tra xem chúng có đáp ứng những tiêu chí trên hay không.
# Mật khẩu hợp lệ sẽ được in, mỗi mật khẩu cách nhau bởi dấu phẩy.

#Ví dụ mật khẩu nhập vào chương trình là: ABd1234@1,a F1#,2w3E*,2We3345

#Thì đầu ra sẽ là: ABd1234@1
import re
def kiemTraCacTieuChi(matkhau):
    tieuchi1 = re.search(r'[A-Z]',matkhau)
    tieuchi2 = re.search(r'[a-z]',matkhau)
    tieuchi3 = re.search(r'[0-9]',matkhau)
    tieuchi4 = re.search(r'[$#@]',matkhau)
    if tieuchi1 and tieuchi2 and tieuchi3 and tieuchi4 and (6<=len(matkhau)<=12):
        return True
def nhapVaInRaMatKhau():
    listmatkhau = [mk for mk in input("Nhập vào chuỗi các mật khẩu: ").split(",")]
    listmatkhaudung = list()
    for password in listmatkhau:
        if (kiemTraCacTieuChi(password) is True):
            listmatkhaudung.append(password)
    print(",".join(listmatkhaudung))
nhapVaInRaMatKhau()

