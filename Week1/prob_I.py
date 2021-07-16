#prob- linear search to find key within the given unsorted array (O(n))

#INPUT 
# line 1- no. of testcase
# line 2- size of array(n)
# line 3- n spaced array elemnts
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
    key=int(input())
    for i in l:
        comp+=1
        if i==key:
            print("Present",comp)
            k=1
            break
    if k==0:
        print("Not Present",comp)
    t-=1