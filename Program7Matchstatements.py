choice = input("Enter the product name =")
choice = choice.lower()
print(choice)
match choice:
    case "pen":
        print("Pen  =  14rs")
    case "pencil":
        print("Pencil  =  10rs")
    case "eraser":
        print("Eraser  =  5rs")
    case _:
        print("The choice does not exist")
