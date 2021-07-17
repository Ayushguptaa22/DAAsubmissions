#prob- linear search to find key within the given sorted array (O(n/2))

#INPUT 
# line 1- no. of testcase
# line 2- size of array(n)
# line 3- n spaced 'sorted' array elemnts
# line 4- 'key' to be searched

#OUTPUT
# "Present" or "Not Present"  with the number of comparisons

t=int(input())
while(t>0):
    n=int(input())
    l=[]
    for i in range(n):
        ele=int(input())
        l.append(ele)
    comp=0
    k=0
    le=len(l)
    h=le-1
    lo=0
    mid=(h+lo)//2
    key=int(input())
    if l[mid]==key:
        comp+=1
        print("Present",comp)
        k=1
        break
    elif l[mid]<key:
        lo=mid+1
        for j in range(lo,le):
            comp+=1
            if l[j]==key:
                print("Present",comp)
                k=1
        break
    elif l[mid]>key:
        h=mid-1
        for j in range(lo,h):
            comp+=1
            if l[j]==key:
                print("Present",comp)
                k=1
        break
    if k==0:
        print("Not Present",comp)
    t-=1