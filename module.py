import math
import modulecalc
a=int(input("Pls enter 1st no: "))
b=int(input("Pls enter 2nd no: "))
c=int(input("Pls enter 1 for addition,2 for subtraction ,3 for division,4 for multiplication,5 for modulus,6 for square root,7 for do all in one,and 0 for exit "))
if(c==1):
    modulecalc.add(a,b)
elif(c==2):
    modulecalc.sub(a,b)
elif(c==3):
    modulecalc.divide(a,b)
elif(c==4):
    modulecalc.multiply(a,b)
elif(c==5):
    modulecalc.module(a,b)
elif(c==6):

    math.sqrt(a)
    print("square root of",a," is: ",a)
    math.sqrt(b)
    print("square root of",b," is: ",b)

elif(c==7):
    c=math.sqrt(a)
    print("square root of",a," is: ",c)

    d=math.sqrt(b)
    print("square root of",b," is: ",d)

    modulecalc.add(a,b)
    modulecalc.sub(a,b)
    modulecalc.multiply(a,b)
    modulecalc.divide(a,b)
    modulecalc.module(a,b)
elif(c==0):
    print("Thankyou!")
else:
    print("Invalid input")

i=input(print("Press 0 to exit "))