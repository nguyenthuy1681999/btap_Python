#Viết một chương trình Python nhận chuỗi nhập vào bởi người dùng,
# in "Yes" nếu chuỗi là "yes" hoặc "YES" hoặc "Yes", nếu không in "No".

def inYes():
    string = input("Nhập vào chuỗi: ")
    if(string == "yes" or string == "YES" or string == "Yes"):
        print("Yes")
    else:
        print("No")
inYes()