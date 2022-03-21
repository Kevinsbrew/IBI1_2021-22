# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
a = 19245301 #set variables
b = 4218520
c = 271
d = b - c
e = a - b
#compare d to e
if d>e :
    print("d is greater")
if d < e :
    print("e is greater")
if d == e:
    print("d is equal to e")
#calculate the rate and compare
rate2020 = c%366
rate2021 = (b-c)%365
if rate2020 >rate2021:
    print("rate of 2020 is greater")
if rate2021>rate2020:
    print("rate of 2021 is greater")
else :
    print("the rate is equal")
