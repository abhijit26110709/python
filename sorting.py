def sortnum(num):
    for i in range(0,len(num)):
        key = num[i]
        j=i-1
        while j>=0 and key<num[j]:
            num[j+1]=num[j]
            j=j-1
        num[j+1]=key

print("Enter 5 numbers\n")
num=[]
for i in range(0,5):
    n=int(input("number: "))
    num.append(n)
sortnum(num)
min_sum = sum(num[0:4])
max_sum = sum(num[1:])
print("Minimum = %d\nMaximum = %d"%(min_sum,max_sum))

