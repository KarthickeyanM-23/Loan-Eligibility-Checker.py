print(" ")
print(" ------------------ INSTRUCTIONS --------------- ")
print(" 1). The Applicant must be above 21 to below 60 years old for salaried and up to 65 for self employed. ")
print(" 2). The applicant must be a citizen or permanent resident of INDIA.")
print(" 3). The Applicant Preferably have 750 and above as having higher credit scores "
      "increase the chances of your loan approval at lower interest rates")
print(" 4). Based on the applicants employment status ( salaried, government employee, private sector, or self-employed ),"
      " the loan amount and the interest rate has been preferred ")
print(" 5). Applicant monthly income must be above 20,000 because the monthly EMI is mostly reaches 40% of the applicants salary.")
print(" 6). If any of the info provided by the applicant went wrong, "
      "it may lead to rejection even if the applicant is eligible. ")
print("-------------------------------------------------------------------------")
print(" ")
print("(please, fill all the details with UPPERCASE LETTERS)")
print(" ")

try:
    while True:
        A = str(input(" NAME : "))
        Name= A.upper()
        if Name.isalpha():
            break
        else:
            print("Please enter a valid name ")
            print(" ")

    while True:
        try:
            Age = int(input(" AGE : "))
            if 20<=Age<=100:
                break
            else:
                print("Please enter a valid age ")
        except ValueError:
            print("Please enter a valid age ")
            print(" ")

    while True:
        B = str(input(" GENDER(M/F) : "))
        Gender= B.upper()
        if Gender == "M" or Gender == "F" :
            break
        else:
            print("Please enter a valid gender")
            print(" ")

    while True:
        C = str(input(" NATIONALITY : "))
        Nationality= C.upper()
        if Nationality == "INDIAN" or Nationality == "OTHERS" :
            break
        else:
            print("Please enter a valid nationality")
            print(" ")

    while True:
        print("(Salaried- S , Government- G , Private - P , Self-Employed- SE)")
        D = str(input(" EMPLOYMENT TYPE (S, G, P, or SE) : "))
        Employed= D.upper()
        if Employed=="S" or Employed=="G" or Employed=="P" or Employed=="SE":
            break
        else:
            print("Please enter a valid employment type")
            print(" ")

    while True:
        try:
            income = int(input(" INCOME PER MONTH : "))
            break
        except ValueError:
            print("Please enter a valid income amount")
            print(" ")

    while True:
        try:
            Loan = int(input(" LOAN AMOUNT AS PER THE NEEDS : "))
            if 50000<=Loan<=100000000:
                break
        except ValueError:
            print("Please enter a valid loan amount")
            print(" ")

    while True:
        E = str(input(" COLLATERAL or NON-COLLATERAL : "))
        loan_type= E.upper()
        if loan_type=="COLLATERAL" or loan_type=="NON-COLLATERAL":
            break
        else:
            print("Please enter detail as collateral or non-collateral")
            print(" ")

    while True:
        try:
            score = int(input(" YOUR CREDIT SCORE : "))
            if 0<=score<=1000:
                break
        except ValueError:
            print("Please enter a valid credit score" )
            print(" ")
    print(" ")

    def loan_eligibility():
        print(" Hello, ", Name)
        print(" Based on the details you provided,")

        if 21 <= Age <= 65:
            if Nationality == 'INDIAN':
                if Employed == 'S' or Employed == 'G' or Employed == 'P' or Employed == 'SE':
                    if Age <= 60:
                            print("Your age, nationality and employment status are eligible")
                    elif Age > 60:
                        if Employed == 'SE' or Employed == 'G':
                            print("Your age, nationality and employment status are eligible for loan ")
                        else:
                            print("Your age was not eligible for loan")
                else:
                    print("Your Employment status was not eligible for loan")
            else:
                print("Your nationality is not eligible for loan")

            if income >= 20000:
                if loan_type == 'COLLATERAL':
                    if 10000 <= Loan <= 50000000:
                        print("And your loan amount was acceptable based on the worth of your collateral property.")
                    else:
                        print("But, your loan amount was not acceptable")
                        print("because your loan amount was too high")
                elif loan_type == 'NON-COLLATERAL':
                    if 10000 <= Loan <= 100000:
                        print("And your loan amount was acceptable for loan")
                    else:
                        print("But, your loan amount was not eligible for loan")
                        print("because your loan amount was too high for non collateral loan")
                else:
                    print("your info was not clear,")
                    print("please, visit the nearby branch for enquiry")
            else:
                print("sorry, your income was not enough for loan")

            if 1 <= score <= 1000:
                if score > 850:
                    print("Your credit score was best for loan process")
                    print("based on your credit score, your interest rate may calculated")
                    print("please, visit the nearby branch for further procedure")
                elif score > 750:
                    print("Your credit score was good for loan process")
                    print("based on your credit score, your interest rate may calculated")
                    print("please, visit the nearby branch for further procedure")
                else:
                    print("Your credit score was not good for loan process")
            else:
                print("your credit score info was not clear")
        else:
            print("Sorry, your age is not eligible for loan")
            print(" ")
        print("Also, connect with us for any enquires.")

except:
    print(' ')
    print("something went wrong")
    print("please try again")

else:
    loan_eligibility()

finally:
    print(" ")
    print("Thank you for using our application")