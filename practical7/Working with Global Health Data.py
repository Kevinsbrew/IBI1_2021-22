# import a few python libraries
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

os.chdir(r"C:\Users\14711\IBI1_2021-22\practical7")# change to the working directory (move to the correct path)
print (os.getcwd())#check the working directory
print (os.listdir())# list the file in the directory
covid_data = pd.read_csv("full_data.csv")#read the content of the .csv file
print(covid_data.head(5))# check the first 5 rows
print(covid_data.describe())# check the mean,count,std,min,max,etc
print(covid_data.iloc[0,1])# check row 0,column 1
print(covid_data.iloc[2,0:5])#chek row 2,column 0 to 5
print(covid_data.iloc[0:2,:])#check row 0 to 2, all the column
print(covid_data.iloc[0:10:2,0:5])#check row 0,2,4,6,8,column 0 to 5

my_columns = [True, True, False, True, False, False]
# creat a list of Booleans that dicided whether to read the data frame
print(covid_data.iloc[0:3,my_columns])
print(covid_data.loc[2:4,"date"])


Afghanistandata=[]
for s in range(0,7996): #seta a loop to add Booleans according to the location to the list  Afghanistandata
    if covid_data.iloc[s,1]=="Afghanistan":
        Afghanistandata .append(True)
    else:
        Afghanistandata.append(False)
print(covid_data.loc[Afghanistandata,"total_cases"])
Chinadata=[]

for m in range(0,7996):#seta a loop to add Booleans according to the location to the list  Chinadata
    if covid_data.iloc[m,1]=="China":
        Chinadata.append(True)
    else:
        Chinadata.append(False)
china_new_data=covid_data.iloc[Chinadata,[0,2,3]]
print(china_new_data)
print(china_new_data.describe())
China_new_cases = china_new_data.iloc[:,1]# new case
China_new_death = china_new_data.iloc[:,2]#new death
China_date = china_new_data.iloc[:,0]#date
plt.plot(China_date,China_new_cases, 'b+') #make a plot in the form of "b+”，x axis :date,y axis :new cases
plt.title('new cases per day')
plt.xticks(China_date.iloc[0:len(China_date):4],rotation=-90) # rotate the data units of x axis,to make them not to overlap
plt.show()
plt.boxplot(China_new_cases,vert=False) #vert false lies down the boxplot
plt.show()
plt.boxplot(China_new_death,vert=False)
plt.show()
plt.plot(China_date,China_new_cases,color ='blue')
plt.plot(China_date,China_new_death,color='red')
plt.title('new cases and new death per day in China')
plt.xticks(China_date.iloc[0:len(China_date):4],rotation=-90)
plt.show()


#question: How have new cases and total cases developed over time in Spain?
Spaindata=[]
for k in range(0,7996):
    if covid_data.iloc[k,1]=="Spain":
        Spaindata.append(True)
    else:
        Spaindata.append(False)
Spain_data=covid_data.iloc[Spaindata,:]
Spain_new_cases =Spain_data.iloc[:,2]
Spain_total_cases =Spain_data.iloc[:,4]
Spain_date=Spain_data.iloc[:,0]

plt.plot(Spain_date,Spain_new_cases,color='blue')
plt.plot(Spain_date,Spain_total_cases,color='red')
plt.title("new cases per day and total cases in Spain")
plt.xticks(Spain_date.iloc[0:len(Spain_date):4],rotation=-90)
plt.show()
