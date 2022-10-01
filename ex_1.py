num1=int(input("веди число і"))
num2=int(input("веди число"))
if  num1 < 7 :
    num1+=(7%num1)
elif num1>7:
    num1=(num1-(num1%7))+7
number3 = num1

while number3<= num2:
    print(f'{number3}')
    number3 += 7