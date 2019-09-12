import random
attacker=[]
atRev=[]
defender=[]
defRev=[]
numbers=[]
attackNum=(input("How many attackers? "))

while ord(attackNum[0])<49 or ord(attackNum[0])>51:
    attackNum=input("How many attackers? ")
        
else:        

    defendNum=(input("How many defenders? "))
    while ord(defendNum[0])<49 or ord(defendNum[0])>50:
        defendNum=input("How many defenders? ")
    for i in range(int(attackNum)+int(defendNum)):
        numbers.append(random.randint(1,6))
    for i in range(len(numbers)):
        if i<int(attackNum):
            attacker.append(numbers[i])
        else:
            defender.append(numbers[i])

    for i in range(1,len(attacker)):
        A=attacker[i]
        j=i-1
        while(j>=0 and A<attacker[j]):
            attacker[j+1]=attacker[j]
            j-=1
        attacker[j+1]=A
    for i in range(len(attacker)-1,-1,-1):
        atRev.append(attacker[i])
    for i in range(len(defender)-1,-1,-1):
        defRev.append(defender[i])

    for i in range(1,len(defender)):
        A=defender[i]
        j=i-1
        while(j>=0 and A<defender[j]):
            defender[j+1]=defender[j]
            j-=1
        defender[j+1]=A
    line=""
    for i in range(len(atRev)):
        line+=str(atRev[i])+"-"
    print("Dice:")
    line=line[:-1]
    print(" "*2+line)

    line=""
    for i in range(len(defRev)):
        line+=str(defRev[i])+"-"
    line=line[:-1]
    print(" "*2+line)
    print()
    print("Outcome:")
    aDiff=0
    bDiff=0
    if atRev[0]>defRev[0]:
        bDiff+=1
    elif atRev[0]<defRev[0]:
        aDiff+=1
    if atRev[1]>defRev[1]:
        bDiff+=1
    elif atRev[1]<defRev[1]:
        aDiff+=1
        
    if aDiff==1:
        print(" "*2+"Attacker lost "+str(aDiff)+" unit")
    elif aDiff!=1:
        print(" "*2+"Attacker lost "+str(aDiff)+" units")
    if bDiff==1:
        print(" "*2+"Defender lost "+str(bDiff)+" unit")
    elif bDiff!=1:
        print(" "*2+"Defender lost "+str(bDiff)+" units")