#Định nghĩa một class có tên là Vietnam, với static method là printNationality.
class VietNam:
    @staticmethod
    def printNatinality():
        print("Hello")

    @staticmethod
    def say():
        print("Xin Chào")
vn = VietNam()
vn.printNatinality()
VietNam.printNatinality()
VietNam.say()