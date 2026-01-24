#list operations
list = ["bru","milk","sugar","cup"]
print(list)
print(list[1]) 
list.pop() #remove last one
print(list)
list.pop(0) #removing 1st one
print(list)
list.append("spoon") #adding the item 
print(list)

list.remove("bru") #remove 
print(list)

list.insert(4,"soppu") #inserting with spesific place 
print(list)

list[0]="kothmerii" #using for editing
print(list)

print(len(list))#checking lenth 
  
j=[3,5,5,44,6,7]
sor_it=sorted(j)
rev= sor_it.reverse()
print(sor_it) 

print(sum(j))

print(list.index("sugar"))#finding index

