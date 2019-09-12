howMany=int(input("How many fibonacci numbers shall I count? "))
num1=0
num2=1
eq=num1+num2
numOspaces=24
if howMany==0:
    exit
elif howMany==1:
    print("1:"+(numOspaces-len(str(num1))-len(str(3)))*" "+str(num1))
elif howMany==2:
    print("1:"+(numOspaces-len(str(num1))-len(str(3)))*" "+str(num1))
    print("2:"+(numOspaces-len(str(num2))-len(str(3)))*" "+str(num2))
elif howMany>2:
    print("1:"+(numOspaces-len(str(num1))-len(str(3)))*" "+str(num1))
    print("2:"+(numOspaces-len(str(num2))-len(str(3)))*" "+str(num2))
    for i in range(howMany-2):
        print((str(i+3))+":"+(numOspaces-len(str(eq))-len(str(i+3)))*" "+str(eq))
        num1=num2
        num2=eq
        eq=num1+num2

#101=22 karakternyi sor