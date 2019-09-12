Num1=input("Enter a number (or a letter to exit): ")
if ord(Num1[0])<48 or ord(Num1[0])>58:
    exit
else:
    Op=(input("Enter an operator: "))
    Num2=int(input("Enter another number: "))
    eq=0
    if Op=="+":
        eq=int(Num1)+int(Num2)
        print("{0}+{1}={2}".format(Num1,Num2,eq))
    elif Op=="-":
        eq=int(Num1)-int(Num2)
        print("{0}-{1}={2}".format(Num1,Num2,eq))
    elif Op==":" or Op=="/":
        eq=int(Num1)/int(Num2)
        print("{0}/{1}={2}".format(Num1,Num2,eq))
    elif Op=="*":
        eq=int(Num1)*int(Num2)
        print("{0}*{1}={2}".format(Num1,Num2,eq))



    #sentNc=(str(input("Tell me something to make it ASCII+3 coded: ")))
#numbers=0
#numbersPlus3=[]
#plusThree=""
#for i in range (len(sentNc)):
  #  plusThree+(ord(sentNc[i])+3)
  #  numbers=(ord(sentNc[i])+3)
  #  plusThree+=chr(numbers)
#print(plusThree)