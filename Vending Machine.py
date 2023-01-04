def vending_machine():
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
        if items == '':
            print('INVALID INPUT')
        else:
            print(f"{items['name']} will cost you {items['price']} dirhams")
            
        #Payment processing
        credits = int(input('Please enter credits: '))
        #If paid with the exact amount
        if credits == items['price']:
            print(f"Thank you for your patronage! Enjoy your {items['name']}!")
        #If paid with extra change
        elif credits >= items['price']:
            print("Thank you for your patronage! Here's your change!", credits - items['price'])
        #Insufficient credits
        else:
            print('Insufficient credits.')

        loop = input("Continue buying? yes/no \n").lower
        if loop == 'yes':
            machine()
        else:
            print('Goodbye, and have a nice day!')
            exit

vending_machine()