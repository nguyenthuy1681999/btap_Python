#Định nghĩa class có tên là Hinhchunhat được xây dựng bằng chiều dài và chiều rộng.
# Class Hinhchunhat có method để tính diện tích.

class Hinhchunhat:
    def __init__(self,cdai,crong):
        self.cdai = cdai
        self.crong = crong
    def tinhDienTich(self):
        return self.cdai*self.crong
hcn = Hinhchunhat(6,9)
print("Diện tích hình chữ nhật là:",hcn.tinhDienTich())
