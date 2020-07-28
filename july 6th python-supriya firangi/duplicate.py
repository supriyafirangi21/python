lst = ["aman", "preet", "aman", "preet", "aman", "deep", "deep","deep","aman","aman"]
temp=set(lst)
result={}
for i in temp:
    result[i]=lst.count(i)
print(result)

