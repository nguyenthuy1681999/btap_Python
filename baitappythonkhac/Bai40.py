#Định nghĩa 1 hàm có thể tạo và in một tuple chứa các giá trị bình phương của các số từ 1 đến 20
# (tính cả 1 và 20).

def tupleChuaGiaTriBinhPhuong():
    listValue = list()
    for i in range(1,21):
        listValue.append(i**2)
    return tuple(listValue)
print(tupleChuaGiaTriBinhPhuong())