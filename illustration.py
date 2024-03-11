# # product
# # order
# # customer


# # customer - id, email, password, name
# # product - id, name, price, quantity_available
# # order id, customer_id, items[product_id]

# Create a dependency that checks that a username is not in the system when creating a customer. (Usernames should be unique)
# Add an endpoint to edit customers
# Add an endpoint to edit product information
# Add a status attribute to the Order entity. (defualt = pending)
# Add an endpoint to checkout an order. (Chang the status from pending to completed)