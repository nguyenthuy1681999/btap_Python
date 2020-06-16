#Sử dụng list comprehension để viết chương trình in list sau khi đã loại bỏ các số chia hết
# cho 5 và 7 trong [12,24,35,70,88,120,155]


print([x for x in [12,24,35,70,88,120,155] if x % 5 !=0 and x % 7 !=0])