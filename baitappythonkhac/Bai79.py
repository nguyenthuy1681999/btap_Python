#Viết chương trình để tạo ngẫu nhiên một list gồm 5 số, chia hết cho 5 và 7, nằm trong đoạn [1;1000].
import random

print(random.sample([x for x in range(1,1001) if x % 5 == 0 and  x % 7 == 0],5))