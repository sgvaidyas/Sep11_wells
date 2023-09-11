endval = int(input("Enter the endval = "))
startval = int(input("Enter the startval"))
while startval<=endval:
    if startval%5 == 0:
        startval = startval+1
        continue
    print(startval)
    startval=startval+1


'''endval = int(input("Enter the number = "))
startval = int(input("Enter the startval"))
while startval<=endval:
    if startval%5 == 0:
        print(startval)
        startval= startval+5
    startval=startval+1'''