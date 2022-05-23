def choco (total_money,price):
    change_left=total_money%price
    bars=(total_money-change_left)/price
    print('bars=',bars,'change left =',change_left)
    return ''
print(choco(50.5,3))