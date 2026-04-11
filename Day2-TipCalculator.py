# print('Welcome to tips calculator!')
# Final_Bill = input('Enter your final bill\n')
# Tip = input('How much do you want to tip?\n')
# People = input('How many people to split the bill? \n')

# tip_percent = int(Tip)/100
# final_cal_tip = tip_percent * float(Final_Bill)

# Total_bill =  final_cal_tip + float(Final_Bill)

# Splitting = Total_bill/int(People)

# Each_to_Pay = round(Splitting,2)


# message = f" \n The total bill was: {Final_Bill} \n and a tip of {Tip}% making {Total_bill} split amongst {People} people\n Each person pays GHC: {Each_to_Pay}"
# print(message)




print("*"*50)
print('Welcome to tips calculator')
print("*"*50)

Bill_Amount = float(input("Enter the total bill amount: GHC "))
Tip_Percent = float(input("Enter tip percentage: "))
People = int(input("How many people to split the bill? "))

Tip_Cal = (Tip_Percent/Bill_Amount)*100
New_Amount = Tip_Cal + Bill_Amount

Each_Person = New_Amount/People

print(f"There are {People} people and a bill of {Bill_Amount} with a tip of {Tip_Percent}\n which is {round(Tip_Cal, 2)} making the total {round(New_Amount,2)} so each pays {round(Each_Person,2)}")