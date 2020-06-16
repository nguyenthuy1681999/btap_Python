#Viết chương trình đếm và in số ký tự của chuỗi do người dùng nhập vào.
def demVaInChuoi(string):
    for i in set(string):
        print(str(i)+","+str(string.count(i)))
demVaInChuoi(input("Nhập vào chuỗi: "))