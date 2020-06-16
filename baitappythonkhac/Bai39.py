#Định nghĩa một hàm có thể tạo list chứa giá trị bình phương của các số từ 1 đến 20 (bao gồm cả 1 và 20).
#Sau đó in tất cả các giá trị của list, trừ 5 mục đầu tiên.
def inRaGiaTriBinhPhuong():
    listBinhPhuong = list()
    for i in range(1,21):
        listBinhPhuong.append(i**2)
    print(listBinhPhuong)
    print(listBinhPhuong[5:])
inRaGiaTriBinhPhuong()