import sys
path="ideabanksideas.txt"
List=[]
if len(sys.argv) == 1:
    x=input("Enter ur idea normie: ")
    text=open("ideabanksideas.txt","a")
    text.write(x+"\n")
    text.close()
    print()
    print("Your ideabank: ")
    with open(path) as p:
        line= p.readline()
        cnt=1
        while line:
            print("{}: {}".format(cnt,line.strip()))
            line=p.readline()
            cnt+=1
    #text.close()
else:
    first_arg = sys.argv[1]
    if first_arg == "--list":
        print()
        print("Your ideabank: ")

        with open(path) as p:
            line= p.readline()
            cnt=1
            while line:
                print("{}: {}".format(cnt,line.strip()))
                line=p.readline()
                cnt+=1
    if first_arg == "--delete":
        second_arg =sys.argv[2] #a delete után álló szám
        with open(path) as p:
            line=p.readline()
            cnt=0
            while line:
                List.append(line)
                line=p.readline() #ezzel bezárólag fel van töltve a lista
        with open (path,"r+") as f:
            line= f.readline()
            f.seek(0)
            f.truncate() #txt ürítése
        text=open("ideabanksideas.txt","a")
        for i in range(int(second_arg),len(List)):
            text.write(List[i])
        text.close()
        print("Your ideabank: ")
        with open(path) as p:
            line= p.readline()
            cnt=1
            while line:
                print("{}: {}".format(cnt,line.strip()))
                line=p.readline()
                cnt+=1