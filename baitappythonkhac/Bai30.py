#Định nghĩa một hàm có input là 2 chuỗi và in chuỗi có độ dài lớn hơn trong giao diện điều khiển.
#Nếu 2 chuỗi có chiều dài như nhau thì in tất cả các chuỗi theo dòng.

def inHaiChuoiTheoDoDai(str1,str2):
    if(len(str1)>len(str2)):
        print(str1)
    elif(len(str2)>len(str1)):
        print(str2)
    else:
        print(str1)
        print(str2)
inHaiChuoiTheoDoDai("Nguyễn Thu Thủy","Nguyễn Thị Thu Thủy")
inHaiChuoiTheoDoDai("Thu Thủy","Thu Thuy")