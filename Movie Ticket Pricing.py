#Movie Ticket Pricing. We would be calculating the price of a movie ticket based on age of the buyer.
BuyerAge = int(input("Enter Your Age: "))


if BuyerAge <13:
    MovieTicket = 5.00
elif BuyerAge < 18:
    MovieTicket = 8.00
elif BuyerAge < 60:
    MovieTicket = 12.00
elif BuyerAge >= 60:
    MovieTicket = 7.00

print(f" The cost of your movie ticket would be {MovieTicket} dollars.")
