#Định nghĩa một lớp gồm có tham số lớp và có cùng tham số instance

#Gợi ý:

#Khi định nghĩa tham số instance, cần thêm nó vào __init__
#Bạn có thể khởi tạo một đối tượng với tham số bắt đầu hoặc thiết lập giá trị sau đó.

class Person:
    name = None
    def __init__(self, name = None):
        self.name = name
    def setName(self):
        self.name = input("Nhập tên của bạn: ")
    def printName(self):
        print("Hello",self.name)
ps1 = Person("Thủy")
ps1.printName()
ps2 = Person()
ps2.setName()
ps2.printName()