#Viết một chương trình chấp nhận chuỗi là các dòng được nhập vào,
# chuyển các dòng này thành chữ in hoa và in ra màn hình. Giả sử đầu vào là:

#Hello world
#Practice makes perfect

#Thì đầu ra sẽ là:

#HELLO WORLD
#PRACTICE MAKES PERFECT

def inHoaCacDong():
    lines = []
    print("Nhập vào các dòng chuỗi: ")
    while True:
        str = input()
        if str:
            lines.append(str.upper())
        else:
            break
    for i in lines:
        print(i)
inHoaCacDong()