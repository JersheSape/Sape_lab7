Name = (input("Enter Name: "))
Section = (input("Enter Section: "))
Prelim = float(input("Prelim Grade: "))
Midterm = float(input("Midterm Grade: "))
Finals = float(input("Final grade:"))

PrelimComp = 0.3333 * Prelim
MidtermComp = 0.3333 * Midterm
FinalsComp = 0.3333 * Finals
Add = PrelimComp + MidtermComp + FinalsComp
Computation = round(Add)
if(Prelim>=40 and Prelim<=100 and Midterm>=40 and Midterm<=100 and Finals>=40 and Finals<=100):
    if(Computation>=99 and Computation<=100 and Computation>=40):
        print("Final Grade: ", round(Computation))
        print("GPA: 1.00")
    elif(Computation>=96 and Computation<=98 and Computation>=40 and Computation<=100):
        print("Final Grade: ", round(Computation))    
        print("GPA: 1.25")
    elif(Computation>=93 and Computation<=95 and Computation>=40 and Computation<=100):
        print("Final Grade: ", round(Computation))    
        print("GPA: 1.50")
    elif(Computation>=90 and Computation<=92 and Computation>=40 and Computation<=100):
        print("Final Grade: ", round(Computation))    
        print("GPA: 1.75")
    elif(Computation>=87 and Computation<=89 and Computation>=40 and Computation<=100):
        print("Final Grade: ", round(Computation))    
        print("GPA: 2.00")
    elif(Computation>=84 and Computation<=86 and Computation>=40 and Computation<=100):
        print("Final Grade: ", round(Computation))    
        print("GPA: 2.25")
    elif(Computation>=81 and Computation<=83 and Computation>=40 and Computation<=100):
        print("Final Grade: ", round(Computation))    
        print("GPA: 2.50")
    elif(Computation>=78 and Computation<=80 and Computation>=40 and Computation<=100):
        print("Final Grade: ", round(Computation))    
        print("GPA: 2.75")
    elif(Computation>=75 and Computation<=77 and Computation>=40 and Computation<=100):
        print("Final Grade: ", round(Computation))    
        print("GPA: 3.00")
    elif(Computation>=75 and Computation<=77 and Computation>=40 and Computation<=100):
        print("Final Grade: ", round(Computation))    
        print("GPA: 3.00")
    elif(Computation>=74 and Computation<=40 and Computation>=40 and Computation<=100):
        print("Final Grade: ", round(Computation))    
        print("GPA: 5.00")
    else:
        print("Invalid Input, Please try again.") 
else:
    print("Invalid Input, Please try again")                     
            
            
           
    
    