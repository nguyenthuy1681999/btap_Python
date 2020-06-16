#Viết một chương trình để tạo tất cả các câu có chủ ngữ nằm trong
# ["Anh","Em"], động từ nằm trong ["Chơi","Yêu"] và tân ngữ là ["Bóng đá","Xếp hình"].

for s in ["Anh","Em"]:
    for v in ["Chơi","Yêu"]:
        for o in ["Bóng đá","Xếp hình"]:
            print(" ".join([s,v,o]))