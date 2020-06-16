#Viết chương trình Python dùng map() để tạo list chứa các giá trị bình phương
# của các số trong [1,2,3,4,5,6,7,8,9,10].

l = map(lambda x:x*x,[1,2,3,4,5,6,7,8,9,10])
print(list(l))