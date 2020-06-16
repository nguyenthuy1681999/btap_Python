#Định nghĩa một hàm có thể tạo ra list chứa các giá trị bình phương của các số từ 1 đến 20
#(bao gồm cả 1 và 20), rồi in 5 mục cuối cùng trong list.

def inRaGiaTriBinhPhuong():
    listBinhPhuong = list()
    for i in range(1,21):
        listBinhPhuong.append(i**2)
    print(listBinhPhuong)
    print(listBinhPhuong[-5:])
inRaGiaTriBinhPhuong()