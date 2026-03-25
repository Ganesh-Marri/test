#fabnocci series
n=int(input("Enter the number of terms:"))
a,b = 0,1
c=0 #counter
print("Fibnocci series:")
while c<n:
    print(a,end="")
    a,b = b,a+b
    c+=1