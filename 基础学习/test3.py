while True:
    p = input("请输入要爬取的页数：")
    if p.isdigit() and int(p) >= 0:
        break
    else:
        continue
print(type(p))