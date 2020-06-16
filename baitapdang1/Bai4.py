#Viết chương trình chấp nhận một chuỗi số,
# phân tách bằng dấu phẩy từ giao diện điều khiển,
# tạo ra một danh sách và một tuple chứa mọi số.

#Ví dụ: Đầu vào được cung cấp là 34,67,55,33,12,98 thì đầu ra là:

#['34', '67', '55', '33', '12', '98']
#('34', '67', '55', '33', '12', '98')


x = input("Nhập vào một chuỗi số: ")
def inRaListNumber(x):
    listnumber = x.split(",")
    return listnumber
#cách 1: tách từng phần tử trong list rồi ép kiểu đẩy vào tuple qua phép + tuple
def inRaTupleNumber(x):
    tuplenumber = tuple()
    list = inRaListNumber(x);
    for i in range(0,len(list)):
        temp = tuple(list[i])
        tuplenumber = tuplenumber + temp ;
    return tuplenumber

print(inRaListNumber(x))
print(inRaTupleNumber(x))
#cách 2: ép kiểu tuple
def inRaTupleNumber2(x):
    return tuple(inRaListNumber(x))
print(inRaTupleNumber2(x))