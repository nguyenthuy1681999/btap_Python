#Sử dụng một danh sách để lọc các số lẻ từ danh sách được người dùng nhập vào.

#Giả sử đầu vào là: 1,2,3,4,5,6,7,8,9 thì đầu ra phải là: 1,3,5,7,9

def locSoLe():
    listNum = [num for num in input("Nhập danh sách các số: ").split(",")]
    listSoLe = list()
    for num in listNum:
        if(int(num)%2!=0):
            listSoLe.append(num)
    print("Danh sách các số lẻ là",end=": ")
    print(",".join(listSoLe))
locSoLe();