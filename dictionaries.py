
# total_revenue=sum(transaction["amount"] for transaction in transactions if transaction.get("type")=="revenue" )
# total_expenses=sum(transaction["amount"] for transaction in transactions if transaction.get("type") =="expense")

# profit=total_revenue-total_expenses

# print(total_revenue, total_expenses)

# print(f"The profit is  {profit}")


company1 = [
    {"description": "Client A", "amount": 100000, "type": "revenue"},
    {"description": "Rent", "amount": 30000, "type": "expense"},
    {"description": "Client B", "amount": 75000, "type": "revenue"},
    {"description": "Electricity", "amount": 12000, "type": "expense"}
]

company2 = [
    {"description": "Client X retainer", "amount": 125000, "type": "revenue"},
    {"description": "Software subscriptions", "amount": 18500, "type": "expense"},
    {"description": "Consulting fees", "amount": 90000, "type": "revenue"},
    {"description": "Internet & utilities", "amount": 9500, "type": "expense"},
    {"description": "Office supplies", "amount": 6200, "type": "expense"},
    {"description": "Project milestone payout", "amount": 60000, "type": "revenue"},
]

companies=[company1,company2]


def analyze_transactions(transactions):
    total_revenue=0
    total_expenses=0

    for transaction in transactions:
        if transaction["type"]=="revenue":
            total_revenue=total_revenue+ transaction["amount"]

        elif transaction["type"]=="expense":
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
            "profit margin":profit_margin}



for company in companies:
    analysis1=analyze_transactions(company)
    # print(f"Company analysis: {analysis1}")
    print(f"Company analysis: \nRevenue: {analysis1['revenue']} \nExpense: {analysis1['expense']} \nProfit: {analysis1['profit']} \nProfit Margin: {analysis1['profit margin']} ") 
# analysis2=analyze_transactions(company2)

# print(analysis2)