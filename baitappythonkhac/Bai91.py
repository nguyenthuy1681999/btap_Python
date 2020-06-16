#Với 2 list cho trước: [1,3,6,78,35,55] và [12,24,35,24,88,120,155],
# viết chương trình để tạo list có phần tử là giao của 2 list đã cho.
print([x for x in set([1,3,6,78,35,55]+[12,24,35,24,88,120,155]) if x in [1,3,6,78,35,55] and x in [12,24,35,24,88,120,155]])