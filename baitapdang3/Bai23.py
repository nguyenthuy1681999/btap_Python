#Xác định một class với generator có thể lặp lại các số nằm trong khoảng 0 và n, và chia hết cho 7.

#Gợi ý:

#Sử dụng yield.

def lapSo():
    n = (x for x in range(0,int(input())))
    for i in n:
        if(i%7==0):
            yield i
for j in lapSo():
    print(j)

