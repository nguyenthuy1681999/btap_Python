#Vui lòng viết chương trình để tạo một list với 5 số ngẫu nhiên từ 100 đến 200.
import random

print(random.sample([x for x in range(100,201) if x % 2 == 0],5))