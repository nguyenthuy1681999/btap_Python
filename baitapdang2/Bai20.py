#Viết chương trình tính số tiền thực của một tài khoản ngân hàng dựa trên
# nhật ký giao dịch được nhập vào từ giao diện điều khiển.

#Định dạng nhật ký được hiển thị như sau:

#D 100
#W 200

#(D là tiền gửi, W là tiền rút ra).

#Giả sử đầu vào được cung cấp là:

#D 300

#D 300

#W 200

#D 100

#Thì đầu ra sẽ là:

#500
def tinhSoTienThucTaiKhoanNganHang():
    soTien = 0
    while True:
        lines = [x for x in input().split(" ")]
        if(lines[0] == "D"):
            soTien = soTien + int(lines[1])
        elif(lines[0] == "W"):
            soTien = soTien - int(lines[1])
        else:break
    print("Số tiền trong tài khoản ngân hàng là: ",soTien)
tinhSoTienThucTaiKhoanNganHang()