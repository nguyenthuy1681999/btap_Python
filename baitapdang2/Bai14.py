#Viết một chương trình chấp nhận đầu vào là chuỗi các số nhị phân 4 chữ số,
# phân tách bởi dấu phẩy, kiểm tra xem chúng có chia hết cho 5 không.
# Sau đó in các số chia hết cho 5 thành dãy phân tách bởi dấu phẩy.

#Ví dụ đầu vào là: 0100,0011,1010,1001

#Đầu ra sẽ là: 1010
def inNhiPhanChiaHetCho5():
    listnum = [num for num in input("Nhập vào một chuỗi các số nhị phân 4 chữ số: ").split(",")]
    for num in listnum:
        number = int(num,2)
        if(number % 5==0):
            print(num)
inNhiPhanChiaHetCho5();