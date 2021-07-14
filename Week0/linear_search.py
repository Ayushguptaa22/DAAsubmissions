n=int(input())
l=[]
for i in range(n):
    ele=int(input())
    l.append(ele)

key=int(input())
for i in range(n):
    if l[i]==key:
        print("found")

