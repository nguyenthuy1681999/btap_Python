#Viết một chương trình minigame đoán số, khi bắt đầu chương trình sẽ hỏi
#người dùng nhập vào một số dương từ 1-300. Minigame có yêu cầu như sau:
#Mỗi khi bắt đầu chương trình kết quả cần dự đoán số khác nhau: 1 <= (số dự
#đoán) <= 300
#Trả lời sai sẽ hiện ra kết quả “Bạn đã trả lời sai x lần”, với x là số lần trả lời
#sai; Nếu trả lời sai năm lần thì sẽ đổi số kết quả và cho người dùng đoán lại năm lần,
#và thông báo với người dùng: “Bạn đoán sai tất cả năm lần, kết quả đã thay đổi. Mời
#bạn đoán lại”
#Nếu trả lời số gần đúng trong khoảng lớn hơn hoặc nhỏ hơn 10 số sẽ thông
#báo người dùng là “Bạn đoán gần đúng rồi!”.
#Nếu người dùng trả lời đúng kết quả, chương trình sẽ kết thúc và hiện ra thông
#báo “Bạn đã dự đoán chính xác số y”, với y là kết quả của số dự đoán
import random


def minigame():
    socantim = random.randrange(1, 300)
    print("=>Gợi ý: Số cần tìm =",socantim)
    solandoan = 1
    while(solandoan<=5):
        soduocdoan = int(input("Mời bạn nhập số dự đoán: "))
        if(soduocdoan == socantim):
            print("-Bạn đã dự đoán chính xác ^^")
            break
        elif(soduocdoan in range(socantim-10,socantim+11)):
            print("-Bạn đoán gần đúng rồi!")
            print("-Bạn đã đoán sai", solandoan, "lần")
        else:
            print("-Bạn đã đoán sai",solandoan,"lần")
        solandoan = solandoan + 1
        if(solandoan > 5):
            socantim = random.randrange(1, 5)
            print('-Bạn đoán sai tất cả năm lần, kết quả đã thay đổi. Mời bạn đoán lại.')
            print("=>Gợi ý: Số cần tìm =", socantim)
            solandoan = 1
minigame()