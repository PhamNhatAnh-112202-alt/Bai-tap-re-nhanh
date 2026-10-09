a = int(input())
b = int(input())
c = int(input())
if (a, b, c > 0) and (a + b > c and b + c > a and a + c > b):
    print("duoc")
else:
    print("khong")
