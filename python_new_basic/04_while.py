treeHit = 0
while treeHit < 10:
    treeHit += 1
    print("나무를 %d번 찍었습니다." % treeHit)
    if treeHit == 10:
        print("나무 넘어갑니다.")


# break, continue
coffee = 10
money = 300
while money:
    print("돈을 받았으니 커피를 줍니다.")
    coffee -= 1
    print("남은 커피의 양은 %d개입니다." % coffee)
    if not coffee:
        print("커피가 다 떨어졌습니다. 판매를 종료합니다.")
        break       # while문 종료


a = 0
while a < 10:
    a += 1
    if a % 2 == 0:
        continue    # continue를 만나면 while문의 맨 처음으로 감.
    print(a)
