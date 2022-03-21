c=1 #set variables,c relates to times we cut
n = 1 # n relates to pieces of pizza
while n < 64: #set a while loop
    n= (c*c+c+2)/2
    c+=1
    if n < 64 :#test whether the pizza is enough and output sentences
        print("we have cut",c-1,"times,there is",n,"piece of pizza,not enough,keep cutting")
    else :
        print("we have cut",c-1,"times,there is",n,"piece of pizza,well done!")

