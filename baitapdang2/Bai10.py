#Viết một chương trình có 2 chữ số, X, Y nhận giá trị từ đầu vào và tạo ra một mảng 2 chiều.
# Giá trị phần tử trong hàng thứ i và cột thứ j của mảng phải là i*j.

#Lưu ý: i=0,1,...,X-1; j=0,1,...,Y-1.

#Ví dụ: Giá trị X, Y nhập vào là 3,5 thì đầu ra là: [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

#Gợi ý:
#Viết lệnh để nhận giá trị X, Y từ giao diện điều khiển do người dùng nhập vào

X = int(input("Nhập số cột của ma trận:"))
Y = int(input("Nhập số hàng của ma trận:"))
def nhapMaTranHaiChieu():
    listMatran = [[0 for i in range(X)]for j in range(Y)]
    for j in range(0,Y):
        for i in range(0,X):
            ptu = input("Ma trận phần tử [%d][%d]:"%(j+1,i+1))
            listMatran[j][i] = ptu
    return  listMatran
def inMaTran(list):
    for j in range(0,Y):
        for i in range(0,X):
            print(list[j][i],end=" ")
        print("\n")
def congHaiMaTran():
    print("Nhập ma trận thứ nhất: ")
    a = nhapMaTranHaiChieu();
    print("Nhập ma trận thứ 2: ")
    inMaTran(a)
    b = nhapMaTranHaiChieu();
    inMaTran(b)
    c = [[0 for i in range(X)]for j in range(Y)]
    for j in range(0,Y):
        for i in range(0,X):
            c[j][i] = a[j][i]+b[j][i]
    print("Ma trận kết quả là:")
    inMaTran(c)
congHaiMaTran();
'''''
input_str = input("Nhập X, Y: ")
dimensions=[int(x) for x in input_str.split(',')]
rowNum=dimensions[0]
colNum=dimensions[1]
multilist = [[0 for col in range(colNum)] for row in range(rowNum)]

for row in range(rowNum):
    for col in range(colNum):
        multilist[row][col]= row*col

print (multilist)
'''''''''