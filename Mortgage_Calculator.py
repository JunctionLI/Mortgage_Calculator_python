#Monthly payment Program
#Group 7 - Kyle , Junxian, Mavros
#Oct/28/2023

#part1-1-1-montly payment calculator-minimum down payment component#
client_name=input("Enter client name: ")
client_address=input("Enter address of property: ")
purchase_price=float(input("Enter purchase price: "))
#Diverse minimum down payment percentage according to different purchase price#
if purchase_price <=500000:
    min_payment=purchase_price*0.05
elif purchase_price>500000 and purchase_price<=1000000:
    min_payment=(purchase_price-500000)*0.1+500000*0.05
elif purchase_price>1000000:
    min_payment=purchase_price*0.2
#tell customer their minimum down payment percentage#
min_payment_percentage=(min_payment/purchase_price)*100

#part1-1-2 mortgage default insurance component#
down_payment_percentage=float(input(f"Enter down payment percentage (minimum {min_payment_percentage:.3f}): ")) 
while True:
    if down_payment_percentage<min_payment_percentage or down_payment_percentage>100:
       print("Please enter a value between the minimum and 100")
       down_payment_percentage=float(input(f"Enter down payment percentage (minimum {min_payment_percentage:.3f}): ")) 
    else:
        break   
down_payment_amount=(purchase_price*down_payment_percentage)/100  
if down_payment_percentage >=5 and down_payment_percentage<10:
    insurance_rate=0.04
elif down_payment_percentage >=10 and down_payment_percentage<15:
    insurance_rate=0.031
elif down_payment_percentage >=15 and down_payment_percentage<20:
    insurance_rate=0.028
elif down_payment_percentage >=20:
    insurance_rate=0
insurance_cost=(purchase_price-down_payment_amount)*insurance_rate
principal_amount=purchase_price-down_payment_amount + insurance_cost
print(f"Down payment amount is ${down_payment_amount:.0f}.")
print(f"Mortgage insurance price is ${insurance_cost:.0f}.")
print(f"Total mortgage amount is ${principal_amount:.0f}.")

#part1-2 mortgage payment component#
mortgage_term=int(input("Enter mortgage term (1, 2, 3, 5, 10): "))
mortgage_term_list=[1,2,3,5,10]
#only term&period in list can be run next step, or enter in the loop until right answer#
while True:
    if mortgage_term not in mortgage_term_list:
        print("Please enter a valid choice")
        mortgage_term=int(input("Enter mortgage term (1, 2, 3, 5, 10): "))
    else:
        break
mortgage_amortization_period=int(input("Enter mortgage amortization period (5, 10, 15, 20, 25): "))
mortgage_amortization_period_list=[5,10,15,20,25]
while True:
    if mortgage_amortization_period not in mortgage_amortization_period_list:
        print("Please enter a valid choice")
        mortgage_amortization_period=int(input("Enter mortgage amortization period (5, 10, 15, 20, 25): "))
    else:
        break
#classify level of interest rate according to term#
if mortgage_term==1:
   mortgage_interest_rate=0.0595
elif mortgage_term==2:
   mortgage_interest_rate=0.059
elif mortgage_term==3:
   mortgage_interest_rate=0.056
elif mortgage_term==5:
   mortgage_interest_rate=0.0529
elif mortgage_term==10:
   mortgage_interest_rate=0.06
mortgage_interest_rate_percentage=mortgage_interest_rate*100
print(f"Interest rate for the term will be {mortgage_interest_rate_percentage:.2f}%")
EMR=((1+mortgage_interest_rate/2)**2)**(1/12)-1      #EMR is monthly interest rate
total_month=mortgage_amortization_period*12
monthly_payment=principal_amount*(EMR*(1+EMR)**total_month)/((1+EMR)**total_month-1)
print(f"Monthly payment amount is: ${monthly_payment:.0f}.")

#part 2-the amortization schedule
user_schedule=input("would you like to see the amortization schedule? (Y/N): ").lower()
mortage_term_month=mortgage_term*12


if user_schedule=="y": 
    print(f"{'Monthly Amortization Schedule':>50} \n " )
    print(f"{'Month':9}{'Opening Bal':15}{'Payment':11}{'Principal':13}{'Interest':12}{'Closing Bal':15}")
    month_already_pay=0
    monthly_principal_total=0
    monthly_interest_total=0
    opening_balance=principal_amount
    while month_already_pay<mortage_term_month:
        month_already_pay +=1
        monthly_interest=opening_balance*EMR
        monthly_principal=monthly_payment-monthly_interest
        closing_balance=opening_balance-monthly_principal
        monthly_principal_total +=monthly_principal
        monthly_interest_total +=monthly_interest
        print(f"{month_already_pay:5}{opening_balance:15.2f}{monthly_payment:11.2f}{monthly_principal:12.2f}{monthly_interest:13.2f}{closing_balance:15.2f}")
        opening_balance=closing_balance
    print("=============================================================================")    
    print(f"{'Total':31}{monthly_principal_total:13.2f}{monthly_interest_total:13.2f}")    
else:
    print("")