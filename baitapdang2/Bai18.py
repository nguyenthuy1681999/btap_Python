#Viết một chương trình tính giá trị của a+aa+aaa+aaaa với a là số được nhập vào bởi người dùng.

#Giả sử a được nhập vào là 1 thì đầu ra sẽ là: 1234

def tinhGiaTri():
    a = int(input("Nhập vào số a: "))
    S = a + a*11 + a*111 + a*1111
    print(S)
tinhGiaTri()