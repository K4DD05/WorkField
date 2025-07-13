#Shadi's Currency Converter works by the user inputting the amount they want to convert in USD and then the converter returns it in cedis
Amnt_in_USD = float(input("Enter Your Amount:"))
Amnt_in_GHS = float(Amnt_in_USD *12.5)
print (f" {Amnt_in_USD}$ converted to Ghana cedis would be {Amnt_in_GHS}cedis.")