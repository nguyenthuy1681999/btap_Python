#Định nghĩa một class có tên là Shape và class con là Square.
#Square có hàm init để lấy đối số là chiều dài.
#Cả 2 class đều có hàm area để in diện tích của hình, diện tích mặc định của Shape là 0.

class Shape:
    def __init__(self):
        pass
    def tinhDienTich(self):
        return 0
class Square(Shape):
    def __init__(self,canh):
        Shape.__init__(self)
        self.canh = canh
    def tinhDienTich(self):
        return self.canh*self.canh
shape = Shape()
print(shape)
print("Diện tích shape:",shape.tinhDienTich())
square = Square(5)
print("Diện tích hình vuông là:",square.tinhDienTich())