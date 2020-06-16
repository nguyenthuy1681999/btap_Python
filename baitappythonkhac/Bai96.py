#Viết chương trình nhận chuỗi do người dùng nhập vào và in các ký tự có chỉ số chẵn.

#Ví dụ: Nếu chuỗi sau được nhập vào: q1u2a3n4t5r6i7m8a9n4g5.6c7o8m, thì đầu ra sẽ là: quantrimang.com

#Sử dụng list[::2] để lặp list cách 2 vị trí.

print("".join([x for (i,x) in enumerate(list("q1u2a3n4t5r6i7m8a9n4g5.6c7o8m")) if i % 2 ==0]))
s = "q1u2a3n4t5r6i7m8a9n4g5.6c7o8m"
print("".join(s[::2]))
print("".join(s[::-1]))