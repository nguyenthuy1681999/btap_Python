#Viết chương trình để giải 1 câu đố cổ của Trung Quốc:
# Một trang trại thỏ và gà có 35 đầu, 94 chân, hỏi số thỏ và gà là bao nhiêu?

def giaiToan():
    for tho in range(35):
        if(tho*4 + (35 - tho)*2 == 94):
            print("Thỏ:",tho)
            print("Gà:",35-tho)

giaiToan()