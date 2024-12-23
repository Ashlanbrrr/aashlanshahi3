price = float (input("Enter the price of the item:"))
if price >=1000:
    discount =(price / 100)*10
    print ("the price after applying discount is ", price- discount)
elif price >=500:
    discount = (price /100)*50
    print ("the price after applying discount is", price - discount )
else  :
    print ("the final price is :",price )
