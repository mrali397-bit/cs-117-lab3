No_1 = float(input("Input the First number: "))
Op = input("Input the operator(+,-,*,/,%): ")
No_2 = float(input("Input the Second number(Enter total here for finding percentage): "))

if Op == '+':
    Ans = No_1 + No_2
    print(Ans)
elif Op == '-':
    Ans = No_1 - No_2
    print(Ans)
elif Op == '*':
    Ans = No_1 * No_2
    print(Ans)
elif Op == '/':
    Ans = No_1 / No_2
    print(Ans)
elif Op == '%':
    Ans = 100*No_1 / No_2
    print(Ans, "%")
else:
    print("Invalid Operator.Please input correct operators(+,-,*,/,%)")
E_O = input("To check for even/odd enter Yes otherwise enter No: ")
if E_O == 'Yes':
    Num_selc = input("Which Number would you like to check for(1 , 2 , both) :")
    if Num_selc == '1':
        if No_1 % 2 == 0:
            print("Number 1 is even.")
        else:
            print("Number 1 is odd.")
    elif Num_selc == '2':
        if No_2 % 2 == 0:
            print("Number 2 is even.")
        else:
            print("Number 2 is odd.")
    elif Num_selc == 'both' :
        if No_1 % 2 == 0:
            print("Number 1 is even.")
        else:
            print("Number 1 is odd.")
        if No_2 % 2 == 0:
            print("Number 2 is even.")
        else:
            print("Number 2 is odd.")
    else:
        print("Invalid Input.Please input Correctly")
print("Thank you for using Simple_calc.")



        