#Dãy Fibonacci được tính dựa trên công thức sau:

#f(n)=0 nếu n=0

#f(n)=1 nếu n=1

#f(n)=f(n-1)+f(n-2) nếu n>1

#Hãy viết chương trình tính giá trị của f(n) với n là số được người dùng nhập vào.
#Ví dụ: Nếu n được nhập vào là 7 thì đầu ra của chương trình sẽ là 13.
def tinhBangDeQuy(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return tinhBangDeQuy(n-1) + tinhBangDeQuy(n-2)
print(tinhBangDeQuy(int(input("Nhập vào số n: "))))

def tinhBangKhac(n):
    listT = []
    #listT[0] = 1
    #print(listT[0])
    #for i in range(2,n+1):
        #listT[i] = listT[i-1] + listT[i-2]
    #return listT[n]
#tinhBangKhac(int(input("Nhập vào số n: ")))
