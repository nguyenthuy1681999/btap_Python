#Định nghĩa một hàm có thể tạo list chứa các giá trị bình phương của các số từ 1 đến 20 (bao gồm cả 1 và 20)
# và in 5 mục đầu tiên trong list.

def inRaGiaTriBinhPhuong():
    listBinhPhuong = list()
    for i in range(1,21):
        listBinhPhuong.append(i**2)
    print(listBinhPhuong)
    print(listBinhPhuong[:5])
    #j=0
    #while (j<=5):
    #   print(listBinhPhuong[j])
    #   j=j+1
inRaGiaTriBinhPhuong()