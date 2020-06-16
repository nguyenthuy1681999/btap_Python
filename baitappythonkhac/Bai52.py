#Định nghĩa một class có tên là Circle có thể được xây dựng từ bán kính.
#Circle có một method có thể tính diện tích.

class Circle:
    def __init__(self,r):
        self.r = r
    def tinhDienTich(self):
        return (self.r**2)*3.14
circle = Circle(5)
print("Diện tích hình tròn là:",circle.tinhDienTich())

