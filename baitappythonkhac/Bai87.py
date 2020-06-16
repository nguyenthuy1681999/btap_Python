#Viết chương trình in list sau khi đã xóa số thứ 0, thứ 2, thứ 4, thứ 6 trong [12,24,35,70,88,120,155].

def inList(l):
    listNew = list()
    for i in range(0,len(l)):
        if (i != 0 and i !=2 and i != 4 and i!=6):
            listNew.append(l[i])
    return listNew
print(inList([12,24,35,70,88,120,155]))
#sử dụng list comprehesion
print([x for i, x in enumerate([12,24,35,70,88,120,155]) if  i % 2 != 0])