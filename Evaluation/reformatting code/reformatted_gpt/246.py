# Produce a matrix for client data
client_data = [[5, 17, 15],  # Client 1
               [4, 32, 22],  # Client 2
               [8, 3, 12]]   # Client 3

# Show predictions
for i, price in enumerate(reg.predict(client_data)):
    print("Predicted selling price for Client {}'s home: ${:,.2f}".format(i+1, price))