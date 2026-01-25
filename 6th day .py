#tuples ()
frots=("mango","orenge","bananna","kivi","beri") #create 5 eliments 
frots[4]="tamota"
print(frots.add("coconet")) #no attribute 'add'
print(frots[2:3]) #slicing element
wgitabal=("tamato","potato")
print(frots+wgitabal)#connect the tuple


#set {}
my_frut={"mango","bannana","orenge" }
fri_frut={"beri","cocanet","kiwi","bannana"}
print(my_frut | fri_frut)#union
print(my_frut & fri_frut)#inter secton
dif= my_frut-fri_frut#difference
print(dif)
print(my_frut.add("popcorn"))#non
my_frut.remove("apple")
my_frut.discard("apple")
print(my_frut)  #remove 


# tupel and set comparison
ele=[2,44,3,2,1,55,77,]
tp=tuple(ele)
se=set(ele)
print("tupel",tp)
print("srt",se)

ele=[]
ele.append(tuple((88,23)))#tuple
tp=tuple(ele)


ele.append(set({57,88,99}))
se=set(ele)
print("tupel",tp)
print("set",se)
#error dont change in enything

