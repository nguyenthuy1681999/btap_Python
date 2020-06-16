#Viết chương trình in list sau khi đã xóa số ở vị trí thứ 0, thứ 4, thứ 5 trong [12,24,35,70,88,120,155].

print([x for (i,x) in enumerate([12,24,35,70,88,120,155]) if i not in(0,4,5)])