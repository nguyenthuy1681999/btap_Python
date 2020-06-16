#Định nghĩa một class exception tùy chỉnh, nhận một thông báo là thuộc tính.

class Error(Exception):
    def __init__(self,exc):
        self.exc = exc
er = Error("Có lỗi")
print(er)