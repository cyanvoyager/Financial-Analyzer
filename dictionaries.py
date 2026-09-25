transactions = [
    {"description": "Client A", "amount": 100000, "type": "revenue"},
    {"description": "Rent", "amount": 30000, "type": "expense"},
    {"description": "Client B", "amount": 75000, "type": "revenue"},
    {"description": "Electricity", "amount": 12000, "type": "expense"}
]

# total_revenue=sum(transaction["amount"] for transaction in transactions if transaction.get("type")=="revenue" )
# total_expenses=sum(transaction["amount"] for transaction in transactions if transaction.get("type") =="expense")

# profit=total_revenue-total_expenses

# print(total_revenue, total_expenses)

# print(f"The profit is  {profit}")

total_revenue=0
total_expenses=0
for transaction in transactions:
    if transaction["type"]=="revenue":
        total_revenue=total_revenue+ transaction["amount"]

    if transaction["type"]=="expense":
        total_expenses=total_expenses+transaction["amount"]


profit=total_revenue-total_expenses

print(f"Revenue: {total_revenue} \nExpenses: {total_expenses} \nProfit: {profit}")



