
# total_revenue=sum(transaction["amount"] for transaction in transactions if transaction.get("type")=="revenue" )
# total_expenses=sum(transaction["amount"] for transaction in transactions if transaction.get("type") =="expense")

# profit=total_revenue-total_expenses

# print(total_revenue, total_expenses)

# print(f"The profit is  {profit}")


from datetime import datetime

company1 = [
    {"date": "2026-02-27", "description": "Client A", "amount": 100000, "type": "revenue"},
    { "description": "Client A", "amount": 100000, "type": "expense"},
    {"date": "2026-01-13", "description": "Rent", "amount": 30000, "type": "expenseses"},
    {"date": "2026-05-21", "description": "Client B", "amount": 75000, "type": "revenue"},
    {"date": "2026-05-06", "description": "Electricity", "amount": 12000, "type": "expense"},
    {"date": "19/4/2026", "description": "Parking fees", "amount": 4800, "type": "expense"},
    {"date": "2026-09-23",  "amount": 12000, "type": "expense"},
]

company2 = [
    {"date": "2026-04-25", "description": "Client X retainer", "amount": 125000, "type": "revenue"},
    {"date": "2026-03-13", "description": "Software subscriptions", "amount": 18500, "type": "expense"},
    {"date": "2026-02-22", "description": "Consulting fees", "amount": 90000, "type": "revenue"},
    {"date": "2026-02-14", "description": "Internet & utilities", "amount": "nine hundred", "type": "expense"},
    {"date": "2026-08-05", "description": "Office supplies", "amount": -6200, "type": "expense"},
    {"date": "17-01-2026", "description": "Project milestone payout", "amount": 60000, "type": "revenue"},
    {"date": "2026-01-20", "description": "Electricity", "amount": 18000, "type": "expense"},
]




# dictionary to access companies
companies={
    "company 1":company1,
    "company 2":company2,
    "1":company1,
    "2":company2,

}


def validate_transaction(transactions,target_period):
    transaction_keys=["date","description","amount","type"]
    alt_formats=["%d-%m-%Y","%Y/%m/%d","%d/%m/%Y"]

    for t in transactions:
        for key in transaction_keys:
            if key not in t:
                print(f"The following required item '{key}' is not among the transaction attributes!")
                return False

        #Checking to ensure the strict YYYY-MM-DD format is followed
        is_strict_format=False
        parsed_date=None
        try:
            parsed_date=datetime.strptime(t["date"], "%Y-%m-%d")
            is_strict_format=True
        except ValueError:
            for fmt in alt_formats:
                try:
                    parsed_date=datetime.strptime(t["date"],fmt)
                    break
                except ValueError:
                    continue
        
        if parsed_date is None:
            print(f"Error: Unrecognized date format in '{t['description']}")
            return False


        transaction_period=parsed_date.strftime("%Y-%m")


        #Reject the non-standard format
        if transaction_period==target_period:
            if not is_strict_format:
                print(f"Error: Invalid date format '{t['date']}' in '{t['description']}'. Expected format 'YYYY-MM-DD'")
                return None
            
        if t['type'] not in ('expense','revenue'):
            print(f"Error: Invalid type '{t['type']}' in transaction '{t['description']}'")
            return False
        # How it works- isinstance(object, type)
        if not isinstance(t['amount'],(int,float)) or (isinstance(t['amount'],bool)):
            print(f"The transaction value '{t['amount']}'. Amount must be numeric.")
            return False
        if t['amount']<0 :
            print(f"The amount '{t['amount']}' must be positive")
            return False
        
    return True

            


def transactions_by_month(company,month):
    results=[]
    alt_formats=["%d-%m-%Y","%Y/%m/%d","%d/%m/%Y"]
    for transaction in company:
        if "date" not in transaction:
            print(f"Error:Transaction '{transaction.get('description','Unknown')}' is missing the date field")
            return False

        if transaction ['date'][:7]==month :
            results.append(transaction)


    
        # for fmt in alt_formats:
        #     try:
        #         parsed=datetime.strptime(transaction["date"],fmt)
        #         if parsed.strftime("%Y-%m")==month:
        #             results.append(transaction)
        #         break
        #     except ValueError:
        #         continue


        # if transaction ["date"][:7]==month  :
        #     # print(f"Date: {transaction['date']} Description: {transaction['description']} Amount: {transaction['amount']} Type: {transaction['type']}")
        #     results.append(transaction)
        #     # If standard prefix didn't match, check alternative date formats
        # for fmt in all_formats:
        #     try:
        #         parsed=datetime.strptime(transaction["date"],fmt)
        #         if parsed.strftime("%Y-%m")==month:
        #             results.append(transaction)
        #             break
        #     except ValueError:
        #         continue
    return results



def analyze_transactions(transactions):
    total_revenue=0
    total_expenses=0

    for transaction in transactions:
        
        if transaction['type']=="revenue":
            total_revenue=total_revenue+ transaction["amount"]

        elif transaction['type']=="expense":
            total_expenses=total_expenses+transaction["amount"]
        else:
            print( f"Transaction type '{transaction['type']}' is invalid!")
            # exit()
            return False



    profit=total_revenue-total_expenses

    if total_revenue !=0  :
            profit_margin=(profit/total_revenue)*100
    else:
        profit_margin="Undefined"

    # print(f"Revenue: {total_revenue} \nExpenses: {total_expenses} \nProfit: {profit} \n Profit margin: {profit_margin}")
    return {"revenue":total_revenue,
            "expenses":total_expenses, 
            "profit":profit,
            "profit margin":profit_margin,
            }


user_choice=input("Please input the company name:").strip().lower()
period=input("Input the period (YYYY-MM):").strip().lower()

comp=companies.get(user_choice)



if comp is not None:
    filtered_transactions=transactions_by_month(comp,period)
    #checks whether the 'filtered_transactions' list is empty.(works the same as if 'len(filtered_transactios)==0:'. An empty list evaluates to false)
    if not filtered_transactions:
        print(f"No transactions to be shown within period {period}")
    else:
        if validate_transaction(filtered_transactions,period):
            for individual_transaction in filtered_transactions:
                print(f"{individual_transaction['date']} | {individual_transaction['description']} | {individual_transaction['amount']:,.2f} | {individual_transaction['type']}")
                analysis=analyze_transactions(filtered_transactions)
                if analysis is not None:
                    if analysis['profit margin']=="Undefined":
                        margin_text="Undefined"
                    else:
                        margin_text=f"{analysis['profit margin']:.2f}%"
                    print(f"Financial Report\n {user_choice} - {period} \n Revenue \t {analysis['revenue']:,.2f}\n Expenses\t {analysis['expenses']:,.2f} \n Net Profit \t {analysis['profit']:,.2f}\n Profit Margin\t {margin_text}")
                else:
                    print("Aborting transaction...")

else:
    print("Company selected doesn't exist!")

# if user_choice=="1" or user_choice=="company1":
#     comp=company1
# elif user_choice=="2" or user_choice=="company2":
#     comp=company2
# else:
#     comp=None
#     print("Company selected doesn't exist!")

        # for item in filtered_transactions:
            # if item['type']!='revenue' and item['type'] !='expense':
            #     print(f"Error: Transaction '{item['description']}' has an invalid type: '{item['type']}'")
            #     break
            # else:


        # print(filtered_transactions)






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



