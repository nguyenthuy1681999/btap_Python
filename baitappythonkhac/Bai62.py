#Viết chương trình để đọc chuỗi ASCII và chuyển đổi nó sang một chuỗi Unicode được mã hóa bằng UTF-8.

#Gợi ý:

#Sử dụng hàm encode() để chuyển đổi.


s = input()
v = s.encode("utf-8") # có thể dùng v=s.encode('utf-8')
print(v)