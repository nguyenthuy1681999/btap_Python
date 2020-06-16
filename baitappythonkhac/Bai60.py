#Viết một chương trình chấp nhận chuỗi từ được phân tách bằng khoảng trống và in các từ chỉ gồm chữ số.

#Ví du: Nếu những từ sau đây là đầu vào của chương trình: 3 quantrimang.com và 2 python.
# Đầu ra sẽ là ['3', '2']
import re


def inRaSoTuChuoi():
    listStr = [x for x in input("Nhập vào chuỗi: ").split(" ")]
    listNum = list()
    for i in listStr:
        if(i.isdigit() is True):
            listNum.append(i)
    return listNum
print(inRaSoTuChuoi())

def inRaSoCach2():
    s = input("Nhập vào 1 chuỗi: ")
    regex = "\d+"
    return re.findall(regex,s)
print(inRaSoCach2())