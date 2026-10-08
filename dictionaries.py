
# total_revenue=sum(transaction["amount"] for transaction in transactions if transaction.get("type")=="revenue" )
# total_expenses=sum(transaction["amount"] for transaction in transactions if transaction.get("type") =="expense")

# profit=total_revenue-total_expenses

# print(total_revenue, total_expenses)

# print(f"The profit is  {profit}")


company1 = [
    {"date": "2026-02-27", "description": "Client A", "amount": 100000, "type": "revenue"},
    {"date": "2026-01-13", "description": "Rent", "amount": 30000, "type": "expense"},
    {"date": "2026-05-21", "description": "Client B", "amount": 75000, "type": "revenue"},
    {"date": "2026-05-06", "description": "Electricity", "amount": 12000, "type": "expense"}
]

company2 = [
    {"date": "2026-04-25", "description": "Client X retainer", "amount": 125000, "type": "revenue"},
    {"date": "2026-03-13", "description": "Software subscriptions", "amount": 18500, "type": "expense"},
    {"date": "2026-02-22", "description": "Consulting fees", "amount": 90000, "type": "revenue"},
    {"date": "2026-02-14", "description": "Internet & utilities", "amount": 9500, "type": "expense"},
    {"date": "2026-08-05", "description": "Office supplies", "amount": 6200, "type": "expense"},
    {"date": "2026-01-17", "description": "Project milestone payout", "amount": 60000, "type": "revenue"}
]


companies=[company1,company2]


def transactions_by_month(company,month):
    results=[]
    for transaction in company:
        if transaction ["date"][:7]==month  :
            # print(f"Date: {transaction['date']} Description: {transaction['description']} Amount: {transaction['amount']} Type: {transaction['type']}")
            results.append(transaction)
    return results


user_choice=input("Please input the company name:")
period=input("Input the period (YYYY-MM):")

if user_choice=="1" or user_choice=="company1":
    comp=company1
elif user_choice=="2" or user_choice=="company2":
    comp=company2
else:
    comp=None
    print("invalid company selected!")
filtered_transactions=transactions_by_month(comp,period)
# print(filtered_transactions)



def analyze_transactions(transactions):
    total_revenue=0
    total_expenses=0

    for transaction in transactions:
        if transaction['type']=="revenue":
            total_revenue=total_revenue+ transaction["amount"]

        elif transaction['type']=="expense":
            total_expenses=total_expenses+transaction["amount"]



    profit=total_revenue-total_expenses

    if total_revenue !=0  :
            profit_margin=(profit/total_revenue)*100
    else:
        profit_margin="Undefined"

    # print(f"Revenue: {total_revenue} \nExpenses: {total_expenses} \nProfit: {profit} \n Profit margin: {profit_margin}")
    return {"revenue":total_revenue,
            "expense":total_expenses, 
            "profit":profit,
            "profit margin":profit_margin,
            }
analysis=analyze_transactions(filtered_transactions)
print(analysis)

# for company in companies:
#     analysis=analyze_transactions(company)


    # print(f"Company analysis: {analysis1}")
    # print(f"Company analysis: \nDate: {analysis['date']} \nRevenue: {analysis['revenue']} \nExpense: {analysis['expense']} \nProfit: {analysis['profit']} \nProfit Margin: {analysis['profit margin']:.2f} % ") 
    # print(company)
    # for transaction in company:
    #     #  print(transaction['date'])
    #      mmyy_str=transaction['date']
    #      mmyy=mmyy_str[5:7]
    #      print(mmyy)



