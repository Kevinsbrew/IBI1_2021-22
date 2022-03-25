import matplotlib.pyplot as plt    #import the module
risk = {'30': 1.03,'35': 1.07,'40':1.11,'45':1.17,'50':1.23,'55':1.32,'60':1.42,'65':1.55,'70':1.72,'75':1.94} #set dictionary
X = list(risk.keys())# create meannings for x axis and y axis
Y = list(risk.values())
plt.scatter(X,Y)
plt.show() #show the plot


Age = input('enter the age') #input the age and get risk rate
print(risk[Age])


