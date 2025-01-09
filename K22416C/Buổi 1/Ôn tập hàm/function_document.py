def firstdegree(a,b):
    """
    Đây là phương trình bậc 1: ax+b=0
    :param a: hệ số a
    :param b: hệ số b
    :return: Trả về 3 trường hợp kết quả
    """
    if a==0 and b==0:
        print("Phương trình vô số nghiệm")
    elif a==0 and b!=0:
        print("Phương trình vô nghiệm")
    else:
        x = -b/a
        print("Nghiệm của phương trình = ", x)
print("Phương trình bậc 1")
a = float(input("Nhập hệ số a:"))
b = float(input("Nhập hệ số b:"))
firstdegree(a,b)