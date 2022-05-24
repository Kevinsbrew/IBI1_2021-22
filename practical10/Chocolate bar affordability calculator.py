def choco (total_money,price):
    change_left=total_money%price
    bars=(total_money-change_left)/price
    return  print('bars=',bars,'change left =',change_left)

# example shows we have 50.5 yuan, the price of chocolate is 3 yuan per bar
choco(50.5,3)
