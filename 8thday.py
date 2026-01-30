#logical operation

att=75
tichar_frind=True
if att>=75 and tichar_frind==True:
    print("is write exam")
else:
    print("no exam")


#NESTED FOR BUS TICKET

gender=(input("emter your gender "))
age=int(input("enter your age "))

if gender=="female":
    print("free ticakte ")
else:
    if age<6:
        print("get free ticate")
    elif age <=12:
        print("he willl get childran discount")
    elif age >=60:
        print("get sinor discount")
    else:
        print("tack a full ticket ")


#  H  W

#basic ondition 

age=int(input("enter your age"))
if age<=5:
    print("buss pass is free")
elif age>=60:
    print("thay get senir discounts")
else:
    print("pay full beo !!")



#meal time checker

time=int(input("enter the time (0-23) "))

if time==8:
    print("time to breake fast")
elif time==14:
    print("time to lunch ")
elif time==20:
    print("time for chikan dinar ")
else:
    print("it's not meal time ")

#eligibality member ship in library
 