#Viết một chương trình chấp nhận đầu vào là một câu, đếm chữ hoa, chữ thường.

#Giả sử đầu vào là: Quản Trị Mạng

#Thì đầu ra là:

#Chữ hoa: 3

#Chữ thường: 8
def demChuHoaVaChuThuong():
    string = input("Nhập chuỗi đầu vào: ")
    listStr = list(string)
    countUpper = 0
    countLower = 0
    for i in  listStr:
        if(i.isupper() is True):
            countUpper = countUpper + 1
        else:
            if(i.islower() is True):
                countLower = countLower + 1
    print("Số chữ hoa là: ",countUpper)
    print("Số chữ thường là: ",countLower)
demChuHoaVaChuThuong()