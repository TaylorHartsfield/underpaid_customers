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

def calculate_customer_payment_correct(customer_information):
    for customer in customer_information:
        name = customer[0]
        balance_due = customer[1]
        total_paid = customer[2]
        if balance_due != total_paid:
            customer_balance = balance_due - total_paid
            def owes_or_owed(customer_balance):
                if customer_balance > 0:
                    return "is owed:"
                else:
                    return "owes:"
            print(f"{name} paid {total_paid}. \nThe required payment is: {balance_due}.\nCustomer {owes_or_owed(customer_balance)} {customer_balance}.")
            print()
customer_data = customer_information(customer_orders)
calculate_customer_payment_correct(customer_data)



# customer1_name = "Joe"
# customer1_melons = 5
# customer1_paid = 5.00

# customer2_name = "Frank"
# customer2_melons = 6
# customer2_paid = 6.00

# customer3_name = "Sally"
# customer3_melons = 3
# customer3_paid = 3.00

# customer4_name = "Sean"
# customer4_melons = 9
# customer4_paid = 9.50

# customer5_name = "David"
# customer5_melons = 4
# customer5_paid = 4.00

# customer6_name = "Ashley"
# customer6_melons = 3
# customer6_paid = 2.00

# customer1_expected = customer1_melons * melon_cost
# if customer1_expected != customer1_paid:
#     print(f"{customer1_name} paid ${customer1_paid:.2f},",
#           f"expected ${customer1_expected:.2f}"
#           )

# customer2_expected = customer2_melons * melon_cost
# if customer2_expected != customer2_paid:
#     print(f"{customer2_name} paid ${customer2_paid:.2f},",
#           f"expected ${customer2_expected:.2f}"
#           )

# customer3_expected = customer3_melons * melon_cost
# if customer3_expected != customer3_paid:
#     print(f"{customer3_name} paid ${customer3_paid:.2f},",
#           f"expected ${customer3_expected:.2f}"
#           )

# customer4_expected = customer4_melons * melon_cost
# if customer4_expected != customer4_paid:
#     print(f"{customer4_name} paid ${customer4_paid:.2f},",
#           f"expected ${customer4_expected:.2f}"
#           )

# customer5_expected = customer5_melons * melon_cost
# if customer5_expected != customer5_paid:
#     print(f"{customer5_name} paid ${customer5_paid:.2f},",
#           f"expected ${customer5_expected:.2f}"
#           )

# customer6_expected = customer6_melons * melon_cost
# if customer6_expected != customer6_paid:
#     print(f"{customer6_name} paid ${customer6_paid:.2f},",
#           f"expected ${customer6_expected:.2f}"
#           )
