a, b, c = map(int, input(). split())
if a == b and b == c:
    print("Deu")
elif a == b or a == c or b == c:
    print("Can")
elif a*a + b*b == c*c or b*b + c*c == a*a or a*a + c*c == b*b:
    print("Vuong")
else:
    print("Thuong")
    
