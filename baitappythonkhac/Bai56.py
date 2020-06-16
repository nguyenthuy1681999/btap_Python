#Viết hàm để tính 5/0 và sử dụng try/exception để bắt lỗi.
def batLoiChia0():
    try:
        return 5/0
    except ZeroDivisionError:
        print("Đã có lỗi chia 0")
    finally:
        print("Đã thực hiện bắt lỗi")
batLoiChia0()