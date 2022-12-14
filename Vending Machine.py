#List of products
items = [
    #Snacks
    {'number':1, 'name':'Lays', 'price':6},
    {'number':2, 'name':'Digestives', 'price':6},
    {'number':3, 'name':'Snickers', 'price':6},
    {'number':4, 'name':'Pringles', 'price':7},
    {'number':5, 'name':'Oman Chips', 'price':7},
    #Beverages
    {'number':6, 'name':'Coca Cola', 'price':7},
    {'number':7, 'name':'Pepsi', 'price':8},
    {'number':8, 'name':'Lipton Iced Tea', 'price':8},
    {'number':9, 'name':'Arwa', 'price':8},
]

quit = False

#Welcoming and product display
while quit == False:
    print("Good day and Welcome!")
    for i in items:
        print(f"Name: {i['name'] : <15} | Price: {i['price']} | Number: {i['number']}")

    #Picking and choosing
    request = int(input("Kindly pick a product of your liking: "))
    for i in items:
        if request == i['number'] :
            items = i

    #If number chosen is outside 1-9 and product cost
    if items >= 9:
        print('INVALID INPUT')
    else:
        print(f"{items['name']} will cost you {items['price']} dirhams")
        
    #Payment processing
    price = int(input(f"Enter {items['price']} dirhams to purchase: "))
    if price == items['price']:
        #If paid correctly
        print(f"Thank you for your patronage! Enjoy your {items['name']}!")
        #If paid incorrectly
    else:
        print(f"Please enter the correct amount")

    #Exiting the application
    request = input("Kindly press 0 to quit: ")
    if request == '0':
        quit = True
        print('Goodbye, and have a nice day!')