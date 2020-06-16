#Định nghĩa hàm có thể chấp nhận input là số nguyên và in "Đây là một số chẵn" nếu nó chẵn
# và in "Đây là một số lẻ" nếu là số lẻ.

def inRaChanLe(number):
    if(number % 2 == 0):
        print("Đây là một số chẵn")
    else:
        print("Đây là một số lẻ")
inRaChanLe(5)