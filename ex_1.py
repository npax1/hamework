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
