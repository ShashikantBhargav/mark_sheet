print("enter marks of 5 subjects:")
a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())

per=(a+b+c+d+e)/5
print("percentage:",per)
if per>=75:
    print("pass with honor")
elif per>=60:
    print("first division")
elif per>=50:
    print("second division")
elif per>=33:
    print("third division")
else:
    print("fail")
