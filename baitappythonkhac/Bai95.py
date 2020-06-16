#Viết chương trình nhận chuỗi đầu vào từ giao diện điều khiển và in nó theo thứ tự ngược lại.

#Ví dụ nếu chuỗi nhập vào là:

#i love you

#Thì kết quả đầu ra là:

#uoy evol i
def daoNguocChuoi(string):
    listStr = list(string)
    listStr.reverse()
    return "".join(listStr)
print(daoNguocChuoi(input("Nhập vào chuỗi: ")))
#cach2
chuoi=input("Nhập chuỗi vào đây: ")
chuoi = chuoi[::-1]
print (chuoi)