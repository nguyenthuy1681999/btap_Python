#Viết chương trình Python dùng map() và filter()
# để tạo list chứa giá trị bình phương của các số chẵn trong [1,2,3,4,5,6,7,8,9,10].

def taoListChuaBinhPhuong(l):
    list1 = filter(lambda x: x %2 == 0,l)
    list2 = map(lambda x: x*x,list(list1))
    return list2
print(taoListChuaBinhPhuong([1,2,3,4,5,6,7,8,9,10]))