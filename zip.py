num1 = [1,2,3,4]
names = ["Shayan","Jo","Elkhana","Rishiram"]

zips = list(zip(num1,names))

print(zips)


x = [10,20,30,40]
y = [70,80,90,100]
    # Here a and b refers to insilization of each elements in the cycle 
for a , b in zip(x,y):
    print(a,b)


set1 = {1,2,3,4,5}
set2 = {7,6,5,3,2}

for set12 , set42 in zip(set1,set2):
    print(set12,set42)
    