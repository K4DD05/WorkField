#Movie Ticket Pricing. We would be calculating the price of a movie ticket based on age of the buyer.
BuyerAge = int(input("Enter Your Age: "))

# Do not start a variable name with a capital letter.
# "MovieTicket" should be declared before it is used.
# Handle the situation where the user inputs an unexpected value for "BuyerAge". eg. -2.

if BuyerAge <13:
    MovieTicket = 5.00
elif BuyerAge < 18:
    MovieTicket = 8.00
elif BuyerAge < 60:
    MovieTicket = 12.00
elif BuyerAge >= 60:
    MovieTicket = 7.00

print(f" The cost of your movie ticket would be {MovieTicket} dollars.")
