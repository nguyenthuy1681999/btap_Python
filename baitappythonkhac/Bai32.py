#Định nghĩa một hàm có thể in dictionary chứa key là các số từ 1 đến n (bao gồm cả hai số)
#và các giá trị bình phương của chúng.

def inRaDictionary():
    n = int(input("Nhập số n:"))
    d = dict()
    for i in range(1,n+1):
        d[i] = i**2
    return d
print("In dictionary chứa key là các số từ 1 đến n (bao gồm cả hai số)")
print(inRaDictionary())