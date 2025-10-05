print(" ")
print("        WELCOME TO THE BANK ELIGIBILITY CHECKER         ")
print(" ")
print(" -------------------------- INSTRUCTIONS ---------------------------- ")
print(" 1). The Applicant must be above 18 to below 75 years old for salaried and up to 65 for self employed. ")
print(" 2). The Applicant must be a citizen or permanent resident of INDIA.")
print(" 3). The Applicant Preferably have 600 and above as higher credit scores "
      "increase the chances of your loan approval at lower interest rates")
print(" 4). Based on the applicants employment status ( salaried, government employee, private sector, or self-employed ),"
      " the loan amount and the interest rate has been preferred ")
print(" 5). Applicant monthly income must be above 20,000 because the monthly EMI is mostly reaches 40% of the applicants salary.")
print(" 6). Applicants are allowed to get Loan Amount Above '50000' to '100000000' Based on the applicants income")
print(" 7). If any of the info provided by the applicant went wrong, "
      "It may lead to Rejection even if the applicant is eligible. ")
print("-------------------------------------------------------------------------")
print(" ")

try:
    while True:
        Nationality = str(input(" NATIONALITY ( INDIAN / OTHERS ) : ")).upper()
        print(" ")
        if Nationality == "INDIAN":
            print(f"NATIONALITY = {Nationality} : APPROVED ")
            print(" ")
            while True:
                try:
                    Age = int(input(" APPLICANT'S AGE : "))
                    print(" ")
                    if 18 <= Age <= 75:
                        print(f" YOUR AGE = {Age} : APPROVED")
                        print(" ")
                        if 18 <= Age <= 20 or 65 <= Age <= 75:
                            print("You Are Only Eligible For GOLD Loan Process")
                            print(" ")
                            while True:
                                option = str(input("Want To Continue The Process ( YES / NO ): ")).upper()
                                if option == "YES":
                                    print(" ")
                                    print("Let's Check Your Eligibility For GOLD Loan")
                                    print(" ")
                                    print("(Please, Fill All The Details With UPPERCASE LETTERS)")
                                    print(" ")
                                    while True:
                                        Name = str(input(" NAME OF THE APPLICANT : ")).upper()
                                        if Name.replace(" ", "").isalpha():
                                            print(" ")
                                            break
                                        else:
                                            print(" ")
                                            print("Please Enter A Valid Name (Alphabets Only)")
                                    while True:
                                        print("( M -male, F -female, T -Transgender ) ")
                                        Gender = str(input(" GENDER ( M / F / T ) : ")).upper()
                                        if Gender == "M" or Gender == "F" or Gender == "T":
                                            print(" ")
                                            break
                                        else:
                                            print(" ")
                                            print("Please Enter A Valid Gender")
                                    while True:
                                        try:
                                            print("Please Enter Your GOLD Purity (18,19,20,21,22,23,24) Or Enter( - ) ")
                                            Gold = input(" GOLD PURITY : ")
                                            print(" ")
                                            if Gold in ['18', '19', '20', '21', '22', '23', '24']:
                                                print(f"Hello, {Name}")
                                                print(f" GOLD CARAT= {Gold} : APPROVED ")
                                                print("Please Visit The Nearby Branch For Gold Purity And Weight Measurement")
                                                print("The Loan Officers Needs To Measure The Weight Of The Gold For Loan Process")
                                                print(" ")
                                                break
                                            elif Gold == '-':
                                                print(f"Hello, {Name}")
                                                print("Please Visit The Nearby Branch For Gold Purity Checking And For Value Calculation ")
                                                print("The Loan Officers Needs To Measure The Weight Of The Gold For Loan Process")
                                                print(" ")
                                                break
                                            else:
                                                print(" ")
                                                print("Please Enter A Valid Input")
                                                continue
                                        except ValueError:
                                            print(" ")
                                            print("Please Enter A Valid GOLD Purity")
                                            continue
                                    break
                                elif option == "NO":
                                    print("Your Enquiry Stops Here")
                                    print(" ")
                                    break
                                else:
                                    print(" ")
                                    print("Please Enter A Valid Input as YES or NO")
                                    continue
                            break

                        elif 21 <= Age <= 65:
                            print("Great, You Are Eligible For Loan")
                            print(" ")
                            while True:
                                try:
                                    print("********* Select Loan Type: ************")
                                    print(" ")
                                    print("  1. PERSONAL LOAN")
                                    print("  2. GOLD LOAN")
                                    print("  3. OTHER LOAN")
                                    print(" ")
                                    choice = int(input(" ENTER YOUR OPTION (1 / 2 / 3) : "))
                                    print(" ")
                                    if choice == 1 or choice == 2 or choice == 3:
                                        if choice == 1:
                                            print("LET'S CHECK YOUR ELIGIBILITY FOR PERSONAL LOAN")
                                            print(" ")
                                            break
                                        elif choice == 2:
                                            print("LET'S CHECK YOUR ELIGIBILITY FOR GOLD LOAN")
                                            print(" ")
                                            break
                                        else:
                                            while True:
                                                print("(Loan For : Car, Home, Mobile, Bike, Laptop, Furniture etc. )")
                                                kind = str(input(" What Kind Of Loan Do You Want : ")).upper()
                                                print(" ")
                                                if kind.isalpha():
                                                    print(f"LET'S CHECK YOUR ELIGIBILITY FOR {kind} LOAN")
                                                    print(" ")
                                                    break
                                                else:
                                                    print("Please Enter A Valid Name ")
                                            break
                                    else:
                                        print("Invalid Choice! Please Select 1, 2, or 3")
                                        continue
                                except ValueError:
                                    print("Invalid Choice! Please Select 1, 2, or 3")
                                    continue
                            print("(Please, Fill All The Details With UPPERCASE LETTERS)")
                            print(" ")
                            while True:
                                Name = str(input(" NAME OF THE APPLICANT : ")).upper()
                                if Name.replace(" ", "").isalpha():
                                    print(" ")
                                    break
                                else:
                                    print(" ")
                                    print("Please Enter A Valid Name (Alphabets Only)")
                            while True:
                                print("( M -male, F -female, T -transgender )")
                                Gender = str(input(" GENDER ( M/F ) : ")).upper()
                                if Gender == "M" or Gender == "F":
                                    print(" ")
                                    break
                                else:
                                    print(" ")
                                    print("Please Enter A Valid Gender")
                            while True:
                                print("(Salaried- S , Government- G , Private - P , Self-Employed- SE)")
                                Employed = str(input(" EMPLOYMENT TYPE ( S, G, P, or SE ) : ")).upper()
                                if Employed == "S" or Employed == "G" or Employed == "P" or Employed == "SE":
                                    print(" ")
                                    break
                                else:
                                    print(" ")
                                    print("Please Enter A Valid Employment Type")

                            if choice == 1 or choice == 3:
                                while True:
                                    try:
                                        print("To Approve Loan, Applicant's Income Must Above '20000'")
                                        income = int(input(" INCOME PER MONTH : "))
                                        if 1<=income<=1000000:
                                            print(" ")
                                            break
                                        else:
                                            print(" ")
                                            print("Please Enter A Valid Income Amount ")
                                    except ValueError:
                                        print(" ")
                                        print("Please Enter A Valid Income Amount")

                                while True:
                                    try:
                                        print("Enter A Loan Amount Above '50000' to '100000000' ")
                                        Loan = int(input(" LOAN AMOUNT AS PER THE NEEDS : "))
                                        if 50000 <= Loan <= 100000000:
                                            print(" ")
                                            break
                                        else:
                                            print(" ")
                                            print("Please Enter A Valid Loan Amount ")
                                    except ValueError:
                                        print(" ")
                                        print("Please Enter A Valid Loan Amount")

                                while True:
                                    try:
                                        print("Applicant's Credit Score Must Above '300' to '900'")
                                        score = int(input(" YOUR CREDIT SCORE : "))
                                        if 300 <= score <= 900:
                                            print(" ")
                                            break
                                        else:
                                            print(" ")
                                            print("Please Enter A Valid Credit Score Amount")
                                    except ValueError:
                                        print(" ")
                                        print("Please Enter A Valid Credit Score")

                            if choice == 1:
                                while True:
                                    E = str(input(" COLLATERAL or NON-COLLATERAL LOAN : "))
                                    path = E.upper()
                                    if path == "COLLATERAL" or path == "NON-COLLATERAL":
                                        print(" ")
                                        break
                                    else:
                                        print(" ")
                                        print("Please Enter A Valid Collateral or Non-Collateral")

                            if choice == 2:
                                while True:
                                    try:
                                        print("Please Enter Your GOLD Purity (18,19,20,21,22,23,24) Or Enter( - ) ")
                                        Gold = input(" GOLD PURITY : ")
                                        print(" ")
                                        if Gold in ['18', '19', '20', '21', '22', '23', '24']:
                                            print(f"Hello, {Name}")
                                            print(f" EMPLOYMENT TYPE = {Employed} : APPROVED")
                                            print(f" GOLD CARAT= {Gold} : APPROVED ")
                                            print("Please Visit The Nearby Branch For Gold Purity And Weight Measurement")
                                            print("The Loan Officers Needs To Measure The Weight Of The Gold For Loan Process")
                                            print(" ")
                                            break
                                        elif Gold == '-':
                                            print(f" Hello, {Name}")
                                            print(f" EMPLOYMENT TYPE = {Employed} : APPROVED")
                                            print("Please Visit The Nearby Branch For Gold Purity Checking And For Value Calculation ")
                                            print("The Loan Officers Needs To Measure The Weight Of The Gold For Loan Process")
                                            print(" ")
                                            break
                                        else:
                                            print("Please Enter A Valid Input")
                                            continue
                                    except ValueError:
                                        print("Please Enter A Valid GOLD Purity")
                                        continue
                                break

                    else:
                        print(f" YOUR AGE = {Age} : REJECTED")
                        print("Sorry, Applicant Must Be In 18-75 Age Limit")
                        print(" ")
                        break

                    def loan_eligibility():
                        print(" ")
                        print("Hello, ", Name)
                        print("Based On The Details You Provided,")
                        print(" ")
                        count = 0
                        if choice == 1 or choice == 3:
                            if Employed == 'S' or Employed == 'G' or Employed == 'P' or Employed == 'SE':
                                if 21 <= Age <= 65:
                                    print(f"\n EMPLOYMENT STATUS = {Employed} : APPROVED")
                                    print(" ")
                                elif Age > 65:
                                    if Employed == 'SE' or Employed == 'P':
                                        print(f"\n EMPLOYMENT STATUS = {Employed} : APPROVED")
                                        print(" ")
                                    else:
                                        print(f" EMPLOYMENT STATUS = {Employed} : REJECTED")
                                        count += 1
                                        print("Because, Your Employment Status Is Not Considered Because of Your Age")
                                        print(" ")
                                else:
                                    print(f" EMPLOYMENT STATUS = {Employed} : REJECTED")
                                    count += 1
                                    print("Because, Your Employment Status Is Not Considered Because of Your Age")
                                    print(" ")
                            else:
                                print(f" EMPLOYMENT STATUS = {Employed} : REJECTED")
                                print("Because, Your Employment Status Is Not Considered Because of Your Age")
                                print(" ")
                            if choice == 3:
                                if 20000 <= income <= 50000:
                                    if 50000 <= Loan <= 9000000:
                                        print(f" LOAN AMOUNT = {Loan} : APPROVED")
                                        print(" ")
                                    else:
                                        print(f" LOAN AMOUNT = {Loan} : REJECTED")
                                        count += 1
                                        print("Because, Your Loan Amount Was Not Acceptable For Your Current Income")
                                        print(" ")
                                elif 50000 < income <= 1000000:
                                    if 9000000 <= Loan <= 900000000:
                                        print(f" LOAN AMOUNT = {Loan} : APPROVED")
                                        print(" ")
                                    else:
                                        print(f" LOAN AMOUNT = {Loan} : REJECTED")
                                        count += 1
                                        print("Because, Your Loan Amount Was Not Acceptable For Your Current Income")
                                        print(" ")
                                else:
                                    print(f" LOAN AMOUNT = {Loan} : REJECTED")
                                    count += 1
                                    print(" Sorry, Your Income Was Not Enough For Loan")
                                    print(" ")
                            if choice == 1:
                                if path == 'COLLATERAL':
                                    if 20000 <= income:
                                        if 50000 <= Loan <= 100000000:
                                            print(f" COLLATERAL LOAN AMOUNT = {Loan} : APPROVED")
                                            print("Based On The Worth Of Your Collateral Property")
                                            print("If Your Collateral Property Was Not Enough For Loan Process")
                                            print("Your Loan Amount Will Automatically Move To Rejection")
                                            print(" ")
                                        else:
                                            print(f" COLLATERAL LOAN AMOUNT = {Loan} : REJECTED")
                                            count += 1
                                            print("Because, Your Loan Amount Was Too High ")
                                            print(" ")
                                    else:
                                        print(f" YOUR INCOME = {income} : REJECTED")
                                        count += 1
                                        print("Because Your Income Was Too Low For Loan Process")
                                        print(" ")
                                elif path == 'NON-COLLATERAL':
                                    if 20000 <= income <= 50000:
                                        if 50000 <= Loan <= 1000000:
                                            print(f" NON-COLLATERAL LOAN AMOUNT = {Loan} : APPROVED")
                                            print(" ")
                                        else:
                                            print(f" NON-COLLATERAL LOAN AMOUNT = {Loan} : REJECTED")
                                            count += 1
                                            print("Because, Your Loan Amount Was Too High For Non-Collateral Loan")
                                            print(" ")
                                    elif 50000 <= income:
                                        if 1000000 <= Loan <= 10000000:
                                            print(f"NON-COLLATERAL LOAN AMOUNT = {Loan} : APPROVED")
                                            print(" ")
                                        else:
                                            print(f"NON-COLLATERAL LOAN AMOUNT = {Loan} : REJECTED")
                                            count += 1
                                            print(f"Because, Your Loan Amount Was Too High For Non-Collateral Loan")
                                            print(" ")
                                    else:
                                        print(f" YOUR INCOME = {income} : REJECTED")
                                        count += 1
                                        print("Because Your Income Was Too Low For Loan Process")
                                        print(" ")
                                else:
                                    print("Your Info Was Not Clear,")
                                    print("Please, Visit The Nearby Branch For Further Enquiry")
                                    print(" ")
                            if 300 <= score <= 900:
                                if score > 750:
                                    print(f" CREDIT SCORE = {score} : APPROVED ( BEST )")
                                    print("Based On Your Credit Score, Your Interest Rate May Calculated")
                                    print("Please, Visit The Nearby Branch For Further Procedure")
                                    print(" ")
                                elif score > 600:
                                    print(f" CREDIT SCORE = {score} : APPROVED ( GOOD )")
                                    print("Based On Your Credit Score, Your Interest Rate May Calculated")
                                    print("Please, Visit The Nearby Branch For Further Procedure")
                                    print(" ")
                                else:
                                    print(f" CREDIT SCORE = {score} : REJECTED")
                                    count += 1
                                    print("Because, Your Credit Score Was not Enough For Loan Process")
                                    print(" ")
                            else:
                                print(f" CREDIT SCORE = {score} : REJECTED")
                                count += 1
                                print("Because Your Credit Score Was not Enough For Loan Process")
                                print(" ")

                        print("*** LOAN ELIGIBILITY RESULTS ***")
                        if count == 0:
                            print("Great News,")
                            print("You Are Eligible For Loan")
                            print(" ")
                        elif count >= 0:
                            print(f" YOUR TOTAL REJECTIONS ARE '{count}'")
                            print("Sorry, You Are Not Eligible For Loan")
                            print(" ")
                    loan_eligibility()
                    break

                except ValueError:
                    print(f"Please Enter A Valid Age")
                    continue
            break
        elif Nationality == "OTHERS":
                other = str(input(" YOUR NATIONALITY : ")).upper()
                print(" ")
                print(f" NATIONALITY = {other} : REJECTED")
                print("Sorry, Only Indians Are Approved")
                print(" ")
                break
        else:
            print(" ")
            print("Please Enter A Valid Nationality")
            continue
except:
    print("\nSomething Went Wrong !")
    print("Please Try Again.....")
    print(" ")
finally:
    print("CONNECT WITH US FOR ANY ENQUIRES")
    print(" ")
    print("______ THANK YOU FOR USING THIS APPLICATION _______")
