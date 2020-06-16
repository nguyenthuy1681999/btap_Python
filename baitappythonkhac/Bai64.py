#Viết một chương trình tính 1/2 + 2/3 + 3/4 + ... + n/(n + 1) với một n là số được nhập vào (n> 0).

#Ví dụ, nếu n là số sau đây được nhập vào:

#5

#Thì đầu ra phải là:

#3.55

def tinhBieuThuc():
    n = int(input("Nhập vào giá trị n > 0 : "))
    i = 1
    T = 0
    print("Tổng biểu thức là: ",end=" ")
    while(i<=n):
        T = T + i/(i+1)
        i =i+1
    return T
print(tinhBieuThuc())
