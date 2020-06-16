#Định nghĩa class Nguoi và 2 class con của nó: Nam, Nu.
#Tất cả các class có method "getGender" có thể in "Nam" cho class Nam và "Nữ" cho class Nu.

#Gợi ý:

#Sử dụng Subclass(Parentclass) để định nghĩa 1 class con.

class Nguoi:
    def __init__(self):
        pass
    def getGender(self):
        pass
class Nam(Nguoi):
    def getGender(self):
        print("Nam")
class Nu(Nguoi):
    def getGender(self):
        print("Nu")
ng = Nguoi()
ng.getGender()
nu = Nu()
nu.getGender()
nam = Nam()
nam.getGender()