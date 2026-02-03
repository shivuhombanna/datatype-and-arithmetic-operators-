# enumarate
name="shivu"
for index, letter in enumerate(name):
    print(letter*(index+1))


cities=["mysur","davanagere","harapanahalli","mydur"]
for city in cities:
    if city=="davanagere":
        continue
    print(f"stop @ {city}")
        
# brake 
cities=["mysur","davanagere","harapanahalli","mydur"]
for city in cities:
    if city=="davanagere":
        print(f"stop @ {city}")
        break
    print(city)
else:
    print("All print")

#math table
m=int(input("enter you rquaird msgiis "))
for i in range(1,11):
    print(f"{m} * {i} ={m*i}")

#multipals of 3
for i in range(1,30):
    if i%3==0:
        print(i)

#sum of first 10 numbers
total=0
for i in range(1,10):
        total+=i
        print(total)

name=input("enter your name")
for later in name:
    print(later)

name=input("enter name ")
vovels="aeiouAEIOU"
count=0
for char in name:
    if char in vovels:
        count+=1
print(count)