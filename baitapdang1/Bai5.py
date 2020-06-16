#Định nghĩa một class có ít nhất 2 method:

#getString: để nhận một chuỗi do người dùng nhập vào từ giao diện điều khiển.

#printString: in chuỗi vừa nhập sang chữ hoa.

#Thêm vào các hàm hiểm tra đơn giản để kiểm tra method của class.

#Ví dụ: Chuỗi nhập vào là quantrimang.com thì đầu ra phải là: QUANTRIMANG.COM

#Gợi ý:

#Sử dụng __init__ để xây dựng các tham số.

class StringUpper:
    def getString(self):
        string = input("Nhập vào 1 chuỗi: ")
        self.string = string
    def printString(self):
        print(self.string.upper())
s = StringUpper()
s.getString()
s.printString()