num1 = [1,2,3]
num2 = [5,7,9]

result = map(lambda x,y:x+y,num1,num2)

print(list(result))

def sq(n):
    return n*n 

result=map(sq,num1)
print(list(result))


