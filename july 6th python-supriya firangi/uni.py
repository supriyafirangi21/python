names=[]
a = 0
while a<10:
    n = input("Please enter the name ")
    if n not in names:
        names.append(n)
        a+=1
    else:
        print("This name is already taken please pick a new one ")
print(names)
print(len(names))