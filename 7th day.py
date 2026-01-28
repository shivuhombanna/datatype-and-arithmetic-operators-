dateofbirth={
    "shivu" :"12-12-2005",
    "manjunath":"22-04-1998",
    "mahesh":"25-09-2009"
}
print(dateofbirth) 
print(dateofbirth.get("shivuii")) #safe accessing 

dateofbirth["shantha"]="12-02-1998"#adding 
print(dateofbirth)

dateofbirth["manjnath"]="12-12-1999"# updating 
print(dateofbirth["manjunath"])

dateofbirth.pop("shivu")
print(dateofbirth)#pop the shivu
 
del dateofbirth["manjunath"]
print(dateofbirth) #delete


#update                                          
new={
    "harish":"22-08-2015"
}
dateofbirth.update(new)
print(dateofbirth)

#item
list1={
    "name":"sugar",
    "weight":7,
    "price":88
}
list2={
    "name":"bru",
    "weight":4,
    "price":78.88
}

print(f"Total prize is {list1['price']+list2['price']} is this")