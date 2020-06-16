#Viết một chương trình để tạo tuple khác, chứa các giá trị là số chẵn
#trong tuple (1,2,3,4,5,6,7,8,9,10) cho trước.

def inRaTupleSoChan(tupleT):
    listSoChan = list()
    #x = tupleT()
    for i in tupleT:
        if(i % 2 == 0):
            listSoChan.append(i)
    return tuple(listSoChan)
print(inRaTupleSoChan((1,2,3,4,5,6,7,8,9,10)))