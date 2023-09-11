i=10
interruptval = int(input("Enter the val to interrupt = "))
while i<=100:
    print(i)
    if i == interruptval:
        break
    i=i+1
print(" this is a line")