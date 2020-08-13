import math

while True:
    r = float(input("请输入圆柱体的底面半径:"))
    if r <=0:
        continue
    if r >0:
        break
while True:
    h = float(input("请输入圆柱体的高："))
    if h <=0:
        continue
    if h >0:
        break
v=math.pi*r*r*h
print("所求圆柱体的体积是:{:.2f}".format(v))