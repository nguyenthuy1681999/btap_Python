#Một Robot di chuyển trong mặt phẳng bắt đầu từ điểm đầu tiên (0,0).
# Robot có thể di chuyển theo hướng UP, DOWN, LEFT và RIGHT với những bước nhất định.
# Dấu di chuyển của robot được đánh hiển thị như sau:

#UP 5

#DOWN 3

#LEFT 3

#RIGHT 3

#Các con số sau phía sau hướng di chuyển chính là số bước đi.
# Hãy viết chương trình để tính toán khoảng cách từ vị trí hiện tại đến vị trí đầu tiên,
# sau khi robot đã di chuyển một quãng đường.
# Nếu khoảng cách là một số thập phân chỉ cần in só nguyên gần nhất.

#Ví dụ: Nếu tuple sau đây là input của chương trình:

#UP 5
#DOWN 3
#LEFT 3
#RIGHT 2

#thì đầu ra sẽ là 2.

#Gợi ý:

#Trong trường hợp dữ liệu đầu vào được nhập vào chương trình nó nên được giả định
# là dữ liệu được người dùng nhập vào từ giao diện điều khiển.
import math


def nhapVaoBuocDi():
    print("Nhập vào các bước đi của Robot:")
    listBuocDi = list()
    while True:
        line = input()
        if line:
            listBuocDi.append(tuple(line.split(" ")))
        else:
            break
    return listBuocDi
def tinhToanKhoangCach(listBuosDi):
    print("Khoảng cách của Robot so với điểm khởi đầu là: ")
    x = 0
    y = 0
    for i in listBuosDi:
        if(i[0] == "UP"):
            y = y + int(i[1])
        elif(i[0] == "DOWN" ):
            y = y - int(i[1])
        elif(i[0] == "LEFT"):
            x = x - int(i[1])
        elif(i[0] == "RIGHT"):
            x = x + int(i[1])
    khoangcach = math.sqrt(x**2 + y**2)
    return int(round(khoangcach))
print(tinhToanKhoangCach(nhapVaoBuocDi()))
