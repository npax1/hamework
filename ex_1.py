start=int(input("веди число і"))
end=int(input("веди число"))
if start < 7:
    q=7%start
    h=start+q
if start>7:
    q=start%7
    h=start-q+7