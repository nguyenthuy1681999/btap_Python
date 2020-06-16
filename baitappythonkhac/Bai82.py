#Bạn hãy viết một chương trình để in thời gian thực thi (running time of execution) phép tính "1+1" 100 lần.
#Sử dụng timeit() để đo thời gian chạy
from timeit import Timer

t = Timer('for i in range(100):1+1')
print(t.timeit())