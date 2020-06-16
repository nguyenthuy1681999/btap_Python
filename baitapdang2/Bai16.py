#Viết một chương trình chấp nhận đầu vào là một câu, đếm số chữ cái và chữ số trong câu đó.
# Giả sử đầu vào sau được cấp cho chương trình: hello world! 123

#Thì đầu ra sẽ là:

#Số chữ cái là: 10
#Số chữ số là: 3

def demChuCaiVaChuSo():
    string = input("Nhập chuỗi đầu vào: ")
    listStr = list(string)
    countAlpha = 0
    countNumber = 0
    for i in  listStr:
        if(i.isalpha() is True):
            countAlpha = countAlpha + 1
        else:
            if(i.isnumeric() is True):
                countNumber = countNumber + 1
    print("Số chữ cái là: ",countAlpha)
    print("Số chữ số là: ",countNumber)
demChuCaiVaChuSo()
