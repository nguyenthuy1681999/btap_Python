#Viết một method tính giá trị bình phương của một số.

#Gợi ý:

#Sử dụng toán tử **.
x = int(input("Nhập một số: "))
def tinhBinhPhuong(x):
    xmu2 = x**2
    return xmu2
print(tinhBinhPhuong(x))