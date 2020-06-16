#Viết chương trình tính tần suất các từ từ input. Output được xuất ra sau khi đã sắp xếp theo bảng chữ cái.

#Giả sử input là: New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.

#Thì output phải là:

#2:2
#3.:1
#3?:1
#New:1
#Python:5
#Read:1
#and:1
#between:1
#choosing:1
#or:2
#to:1
def tinhTanSuat():
    listStr = [x for x in input("Nhập vào chuỗi: ").split(" ")]
    listStr2 = list(set(listStr))
    listStr2.sort()
    for str in listStr2:
        print(str,end=":")
        countStr = listStr.count(str)
        print(countStr)
tinhTanSuat()