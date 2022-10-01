start=int(input("веди число і"))
end=int(input("веди число"))
a = int(input("1Усі числа діапазону\n2. Усі числа діапазону за спаданням.\n3. Усі числа, кратні 7\n4. Кількість чисел, кратних 5."))
if a ==1:
    while start <= end:
        print(start)
        start=start+1
if a ==2:
    temp=start
    start=end
    end=temp
    while start>end:
        start-=1
        print(f"{start}")
if a == 3:
    if start < 7:
        start += (7 % start)
    elif start > 7:
        num1 = (start - (start % 7)) + 7
    number3 = num1

    while number3 <= end:
        print(f'{number3}')
        number3 += 7
if a == 4 :
    if  start < 5:
        start+=(5%start)
    elif start>5:
        start=(start-(start%5))+5
    number4=start

    while number4<=end:
        print(f"{number4}")
        number4+=7

