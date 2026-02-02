if_fail=True
i=1
while if_fail:
    if i%2!=0:#is not even
        i=i+1
        continue
    print("tray"+ str(i))
    i=i+1
    if i>100:
        break
print("give upp!!")


i=0
while i<=10:
    x=0
    while x<i:
        print("shivu", end="-")
        x+=1
    print("")
    i+=1


pss="1234"
trayal=1

while trayal<=3:
    inputforuser=input(f"thi stry{trayal}  password ")
    trayal+=1
    if inputforuser==pss:
        print("CORRECT")
        break
    else:
        print("faile")

#home work
#1
i=0
while i<=10:
    print(i)
    i+=1
  
#2nd only odd numbers 
i=1
while i<=20:
    if i&3!=0:
        print(i)
    i +=1


#3rd 
