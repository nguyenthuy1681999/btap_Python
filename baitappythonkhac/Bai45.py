#Viết chương trình Python có thể lọc các số chẵn trong danh sách sử dụng hàm filter.
# Danh sách là [1,2,3,4,5,6,7,8,9,10].

l = filter(lambda x: x%2 == 0,[1,2,3,4,5,6,7,8,9,10])
print(list(l))