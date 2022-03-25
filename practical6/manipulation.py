M = [45,36,86,57,53,92,65,45]#create a list
M = sorted(M)#sort the list
print(M)
SUM = 0
for I in range(0,len(M)):#set a loop to get the sum
    SUM+= M[I]

print("average =",SUM/8)#get the average
if SUM/8 > 60:
    print("his mark is higher than 60")
else :
    print("his mark is not higher than 60")


# show the boxplot
import matplotlib.pyplot as plt
plt.title('boxplot for mark')
plt.boxplot(M)
plt.show()