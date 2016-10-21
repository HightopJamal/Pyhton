balance = 42
annualInterestRate = .2
monthlyPaymentRate = .04
count = 0
monthly_rate = annualInterestRate / 12

for i in range(12):
    monthly_min = monthlyPaymentRate * balance
    monthly_unpaid = balance - monthly_min
    updated_balance = monthly_unpaid + (monthly_rate * monthly_unpaid)
    balance = updated_balance
    count +=1

    print("Month" +" "+str(count)+ " "+"balance is:" + str(round(balance,2)))
   
print("Remaining balance:" + str(round(balance,2)))
