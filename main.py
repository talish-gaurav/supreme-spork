
def SquareValue(beg,end):
    lst = []

    for i in range(beg,end):
        lst.append(i**2)

    lst_even = []
    lst_odd = []

    for i in lst:
        if i % 2 == 0:
            lst_even.append(i)
        else:
            lst_odd.append(i)
    print("Here is a list of even squares within a given range", lst_even)
    print("Here is a list of odd squares within a given range", lst_odd)

print(SquareValue(0,100))