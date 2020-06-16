#Viết chương trình để in một số nguyên ngẫu nhiên từ 7 đến 15.

import random

print(random.choice([x for x in range (7,16)]),type(random.choice([x for x in range (7,16)])))
print(random.randrange(7,16))