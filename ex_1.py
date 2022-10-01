num1=int(input("веди число і"))
num2=int(input("веди число"))
number=7
if num1 / 7==1:
    if num1 < 7:
        number=(int(num1+(7%num1)))
    elif num2>7:
        number1= (int(num1-(num1%7))+7)


while number<num2:
    print(f'{number}')
    number+=7
else:
    print(f'{number}')