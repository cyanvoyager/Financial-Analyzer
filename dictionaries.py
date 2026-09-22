transactions = [
    {"description": "Client A", "amount": 100000, "type": "revenue"},
    {"description": "Rent", "amount": 30000, "type": "expense"},
    {"description": "Client B", "amount": 75000, "type": "revenue"},
    {"description": "Electricity", "amount": 12000, "type": "expense"}
]

total_revenue=0
total_expenses=0

for i in transactions:
    print(i)