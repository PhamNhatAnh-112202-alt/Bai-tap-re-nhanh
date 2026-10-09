a, b = map(int, input().split())
if a == 0 and b != 0:
    print("VN")
elif a == 0 and b == 0:
    print("VSN")
else:
    print("x = ", -b/a)
    
    
