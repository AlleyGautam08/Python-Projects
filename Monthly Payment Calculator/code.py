from time import monotonic


def main():
     print("This is a monthly payment loan calculator")
     print("")


     principal = float(input("input the loan amount: "))
     apr = float(input("input the annual interest rate: "))
     years = int(input("input amount of years: "))
    
     monthly_interest_rate = apr / 1200
     amount_of_months = years * 12
     monthly_payment = principal * monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** (-amount_of_months))

     print("The monthly payment for this loan is : " + str(monthly_payment))

main()



