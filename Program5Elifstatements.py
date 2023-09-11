marks = float(input("Enter the marks = "))
if marks>=0 and marks<35:
    print("FAIL")
elif marks>=35 and marks<50:
    print("PASS CLASS")
elif marks>=50 and marks<70:
    print("SECOND CLASS")
elif marks>=70 and marks<=100:
    print("FIRST CLASS")
else:
    print("INVALID MARKS ")