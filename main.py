# revenue=1000000
# expenses=6500000

# profit=revenue-expenses

# print(f"Revenue: {revenue}\nExpenses: {expenses}\nProfit: {profit}" )

# if profit>0:
#     print("Business made a profit")
# else:
#     print("Business made a loss")

print("Give me your revenue and expenses and I'll analyse them for you")
print("Revenue:")
rev=int(input())
print("Expenses:")
exp=int(input())

def analyze_finances(revenue,expenses):
    profit=revenue-expenses
    if revenue !=0  :
        profit_margin=(profit/revenue)*100
    else:
        profit_margin="Undefined"
    print(f"Revenue: {revenue}\nExpenses: {expenses}\nProfit: {profit}\nProfit Margin: {profit_margin}")

    if profit>0:
        print("You made a profit")
    elif profit==0:
        print ("A break-even was recorded")
    else:
        print("You made loss")


analyze_finances(rev,exp)