print("——————小甲鱼欢迎你————————")
temp = input("猜一猜小甲鱼心中的一个数:")
guess = int(temp)
if guess == 8:
    print("you are right")
else:
    if guess < 8:
        print("too small")
    else:
        print("too big")
print("game over")
