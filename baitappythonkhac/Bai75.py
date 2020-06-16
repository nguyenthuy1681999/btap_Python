#Viết chương trình xuất ra một số chẵn ngẫu nhiên trong khoảng 0 đến 10 (bao gồm cả 0 và 10),
# sử dụng module random và list comprehension.
import random


print(random.choice([x for x in range(0,11) if x % 2 == 0]))