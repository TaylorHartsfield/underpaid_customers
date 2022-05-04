customer_orders = open("customer-orders.txt")
MELON_COST = 1.00

def customer_information(customer_orders = customer_orders):
    customer_data = []
    for line in customer_orders:
        line = line.strip()
        customer = line.split("|")
        
        customer_name = customer[1]
        customer_order_quantity = float(customer[2])
        customer_payment_total = float(customer[3])

        customer_data.append([customer_name, customer_order_quantity, customer_payment_total])

    return customer_data

def calculate_customer_payment_correct(customer_information, cost = MELON_COST):
    for customer in customer_information:
        name = customer[0]
        melon_total = int(customer[1])
        balance_due = customer[1] * cost 
        total_paid = customer[2]
        if balance_due != total_paid:
            customer_balance = balance_due - total_paid
            def owes_or_owed(total_paid = total_paid, balance_due = balance_due):
                if balance_due > total_paid:
                    return f"owes: ${customer_balance}"
                elif balance_due < total_paid:
                    return f"is owed: ${customer_balance*-1}"
            print(f"{name} paid ${total_paid}. \nThe required payment for {melon_total} melons is: ${balance_due}.\nCustomer {owes_or_owed()}.")
            print()

customer_data = customer_information(customer_orders)
calculate_customer_payment_correct(customer_data)
