#Viết một chương trình chấp nhận chuỗi từ do người dùng nhập vào,
# phân tách nhau bởi dấu phẩy và in những từ đó thành chuỗi theo thứ tự bảng chữ cái,
# phân tách nhau bằng dấu phẩy.

#Giả sử đầu vào được nhập là: without,hello,bag,world, thì đầu ra sẽ là: bag,hello,without,world.
def sapXepChuoi():
    string = input("Mời bạn nhập vào chuỗi: ")
    listString = string.split(",")
    listString.sort(reverse=False)
    print(listString)
sapXepChuoi()