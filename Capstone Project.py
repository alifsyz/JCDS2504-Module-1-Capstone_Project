#### CRUD Program for automotive spare parts shop ####
#### context: Small to medium spareparts shop, used for parts purchasing (operated by Cashier) or inventory management (operated by Stockist)####
## Part attributes ##
# manufacturer_pn: unique numeric (integer) data specific to a certain part. Given by the part manufacturer, so manufacturer is responsible for any mistakes 
# part_name: string. possible to have duplicates since some cars have the same parts (eg. all cars have spark plugs)
# manufacturer_brand: string data. the name of the company that manufactured the part
# part_compatibility: string data. to check part compatibility with car manufacturer
# stock_quantity: integer
# price: float

from prettytable import PrettyTable # Import prettytable to print list in an aesthetic manner
import datetime # import for inserting date and time of transaction

# dictionary in a list, easy indexing with specific names for part attributes
parts_stock = [{'manufacturer_pn': 1700231, 'part_name': 'Lower Intake Boot', 'manufacturer_brand': 'Uro Parts', 'part_compatibility': 'BMW',
                'stock_quantity' : 4, 'price': 80.00}, {'manufacturer_pn': 1700232, 'part_name': 'CV Axle', 'manufacturer_brand': 'Tokico', 'part_compatibility': 'Honda',
                'stock_quantity' : 2, 'price': 120.00},{'manufacturer_pn': 1700233, 'part_name': 'Main Fuel Pump', 'manufacturer_brand': 'Bosch', 'part_compatibility': 'Mercedes-Benz',
                'stock_quantity' : 10, 'price': 52.00}, {'manufacturer_pn': 1700234, 'part_name': 'Left Lower Control Arm', 'manufacturer_brand': 'Lemforder', 'part_compatibility': 'BMW',
                'stock_quantity' : 6, 'price': 100.00}, {'manufacturer_pn': 1700235, 'part_name': 'Ignition Coil', 'manufacturer_brand': 'Bremi', 'part_compatibility': 'Toyota',
                'stock_quantity' : 14, 'price': 35.00}

]

cart = []
transactions = [] # List of all transactions that has been done. Usually for records that can be useful to claim warranty
# admin_privelages = False # WIP for admin privelages

def displayInventory(): # to display current inventory using prettytable
    # deleteZero() # Remove parts that have zero stock so it does not show when displaying the inventory
    if not parts_stock: # Check for empty list with 'not'
        print('\nDatabase is empty.\n') 
    else:
        print('\n\t\t\t\t\tSpare Parts Inventory\n') 
        tables = PrettyTable()
        tables.field_names = ['Manufacture P/N','Name','Brand','Compatibility', 'Quantity','Price ($)']
        for i in range(len(parts_stock)):
            tables.add_row([parts_stock[i]['manufacturer_pn'],parts_stock[i]['part_name'],parts_stock[i]['manufacturer_brand'],parts_stock[i]['part_compatibility'],
                            parts_stock[i]['stock_quantity'],parts_stock[i]['price']]) # inserting list items into pretty table
        tables.align = 'c' # align center
        print(tables)

def deleteParts():
    while True:
        try:
            print('Delete menu')
            print('1. Delete parts') 
            print('2. Return to main menu')
            choice = int(input('Enter desired function [1-2]: '))
        
            if choice == 1:
                print('1. Delete by Part Number') 
                print('2. Delete all inventory data')
                print('3. Delete parts with empty stock')
                print('4. Return to sub menu')
                delete_by = int(input('Enter a selection [1-4]: '))
                if delete_by == 1:
                    delete_pn = (int(input('\nEnter part number to delete: ')))
                    result = findPartsByPN(delete_pn)
                    int_check = isinstance(result,int)
                    if int_check == True:
                            tables = PrettyTable()
                            tables.field_names = ['Manufacture P/N','Name','Brand','Compatibility', 'Quantity','Price ($)']
                            tables.add_row(([parts_stock[result]['manufacturer_pn'],parts_stock[result]['part_name'],parts_stock[result]['manufacturer_brand'],parts_stock[result]['part_compatibility'],
                                parts_stock[result]['stock_quantity'],parts_stock[result]['price']]))   # inserting list items into pretty table for diplaying 
                            tables.align = 'c'
                            print(tables)
                            confirmation = input('Are you sure you want to delete this part?(Y/N): ') 
                            if confirmation.upper() == 'Y':
                                print(f'\nPart Number {parts_stock[result] ["manufacturer_pn"]} has been successfully deleted.')
                                parts_stock.pop(result)
                                continue
                            elif confirmation.upper() == 'N':
                                print('Part deletion cancelled')
                                continue
                            else:
                                print('Invalid input.')
                                continue
                    elif result == 'False':
                            print('\nPart does not exist.')
                            continue
                elif delete_by == 2:
                    confirmation = input("Are you sure you want to delete all data? (Y/N) ")
                    if delete_by.upper() == 'Y':
                        parts_stock.clear()
                    elif delete_by.upper() == 'N':
                        continue
                    else:
                        print('Invalid input.')
                        continue
                elif delete_by == 3:
                    deleteZero()
                elif delete_by == 4:
                    continue
                else:
                    print('\nInvalid input.')
                    continue
            if choice == 2:
                break
            else:
                print('\nPlease enter the correct menu.')
        except ValueError:
            print('\nPlease enter only integers.')

def deleteZero():
    for i in range(len(parts_stock)):
        if parts_stock[i]['stock_quantity'] == 0:
            parts_stock.pop(i)
    
def add_parts(): # Add new parts to inventory 
    while True:
        print('Add menu')
        print('1. Add a part') 
        print('2. Return to main menu')
        try:
            choice = int(input("Enter desired function [1-2]: "))
            if choice == 1:
                try:
                    manufacturer_pn = int(input('Enter part number : '))
                    result = findPartsByPN(manufacturer_pn) # Checking for duplicate parts (by Part Number)
                    int_check = isinstance(result,int) # isinstance used to check type: 'int'
                    if int_check == True:
                        print('\nPart exists! Please enter a different Part Number\n')
                        continue                    
                    part_name = input('Enter part name : ')
                    part_manufacturer = input('Enter part manufacturer : ')
                    part_compatibility = input('Enter part compatibility: ')
                    while True:
                        stock_quantity = int(input('Enter quantity of parts : '))
                        if stock_quantity <= 0:
                            print('\nPlease enter the correct amount.')
                            continue
                        elif isinstance(stock_quantity,int) == False:
                            print('Please enter the correct amount.')
                            continue
                        else:
                            break
                    while True:
                        part_price = float(input('Please enter price: '))
                        if part_price <= 0:
                            print('\nPlease enter the correct amount.')
                            break
                        elif stock_quantity.isfloat() == False:
                            print('Please enter the correct amount.')
                            continue
                        else: 
                            break
                    
                    tables = PrettyTable()
                    tables.field_names = ['Manufacture P/N','Name','Brand','Compatibility', 'Quantity','Price ($)']
                    tables.add_row([manufacturer_pn,part_name,part_manufacturer,part_compatibility,
                                    stock_quantity,part_price]) #inserting list items into pretty table for diplaying 
                    tables.align = 'c' #align center
                    print(tables)
                    confirmation = input('Confirm adding parts to inventory?(Y/N): ')
                    if confirmation.upper() == 'Y':
                        parts_stock.append({'manufacturer_pn': manufacturer_pn, 'part_name': part_name, 'manufacturer_brand': part_manufacturer, 'part_compatibility': part_compatibility,
                                            'stock_quantity' : stock_quantity, 'price': part_price})
                        print('Part added successfully!')
                        displayInventory()
                        break
                    elif confirmation.upper() == 'N':
                        print('Process cancelled')
                        continue
                    else:
                        print('\nInvalid input. Please try again.')      
                        continue  
                except ValueError:
                    print('\nInvalid input.')
            if choice == 2:
                break
            else:
                print('\nPlease enter the correct menu.')
        except ValueError:
            print('\nPlease enter an integer.')

def bubbleSort(data,key): # Sort using bubble sort method. data = list, key = key in the dictionary that wants to be sorted by
    n = len(data)
    for i in range(n):
        for j in range(0, n-i-1):
            if data[j][key] > data[j+1][key]:
                data[j], data[j+1] = data[j+1], data[j]
      

def viewParts(): # view current inventory list
    while True:
        print('\nInventory:')
        print('1. Display all') 
        print('2. Find parts by part number')
        print('3. Return to main menu')
        try:
            choice = int(input("Enter desired function [1-3]: "))
            if choice == 1:
                displayInventory()
                print('1. Sort by Partnumber\n2. Sort by Name\n3. Sort by Compatibility\n4. Sort by Price\n5. Exit')
                sort = int(input('Enter a selection [1-5]: '))
                if sort == 1: # Sorting is done by bubbleSort function in ascending order
                    bubbleSort(parts_stock,'manufacturer_pn')
                elif sort == 2:
                    bubbleSort(parts_stock,'part_name')
                elif sort == 3:
                    bubbleSort(parts_stock,'part_compatibility')
                elif sort == 4:
                    bubbleSort(parts_stock,'price')
                continue # will continue the loop when no input or any input other 1-4 is entered 
            if choice == 2:
                p_number = int(input('Enter part number: '))
                result = findPartsByPN(p_number)
                int_check = isinstance(result,int) #check if index return is integer
                if int_check == True:
                    print('\nPart exists!\n')
                    tables = PrettyTable()
                    tables.field_names = ['Manufacture P/N','Name','Brand','Compatibility', 'Quantity','Price ($)']
                    tables.add_row([parts_stock[result]['manufacturer_pn'],parts_stock[result]['part_name'],parts_stock[result]['manufacturer_brand'],parts_stock[result]['part_compatibility'],
                                    parts_stock[result]['stock_quantity'],parts_stock[result]['price']]) #inserting list items into pretty table
                    tables.align = 'c' #align center
                    print(tables)
                elif result == 'False':
                    print('\nPart does not exist.')
                    continue
                else:
                    print('\nInvalid input.')
                    continue
            if choice == 3: 
                break
            else:
                print('\nPlease enter the correct menu.')
        except ValueError:
            print('\nInvalid Input.\n')

def findPartsByPN (p_number) : # finding parts by part number. Function with input and output
    for i in range(len(parts_stock)):
        if parts_stock[i]['manufacturer_pn'] == p_number:
            print(parts_stock[i]['manufacturer_pn'])
            return i # returns index of found parts
    return 'False' #return string because False == 0. Detected as INT
    
def updateParts(): # update parts attributes
    while True:
        print('\nUpdate part attributes')
        print('1. Update parts') 
        print('2. Return to main menu')
        try:
            choice = int(input('Enter desired menu [1-2]: '))
            if choice == 1 :
                displayInventory() # for referencing to update
                p_number = int(input('Enter part number: '))
                result = findPartsByPN(p_number)
                int_check = isinstance(result,int) # check if index return is integer. isinstance(a,b) a is variable, b can be int,float,string,etc
                if int_check == True:
                    print('\nPart exists!\n')
                    tables = PrettyTable()
                    tables.field_names = ['Part Number','Name','Brand','Compatibility', 'Quantity','Price']
                    tables.add_row([parts_stock[result]['manufacturer_pn'],parts_stock[result]['part_name'],parts_stock[result]['manufacturer_brand'],parts_stock[result]['part_compatibility'],
                                    parts_stock[result]['stock_quantity'],parts_stock[result]['price']]) # inserting list items into pretty table
                    tables.align = 'c' # align center
                    print(tables)
                    edit_table = input('Which table would you like to edit?: ')
                    if edit_table.title() == 'Part Number': 
                        print('\nPart number cannot be changed. Please delete part and create a new entry with the new part number.\n') #unique, use delete and create new entry
                        continue
                    elif edit_table.title() == 'Name':
                        while True:
                            new_name = input('Enter new name for this part: ')
                            if isinstance(new_name,str) == False:
                                print('Please enter a string.')
                                continue
                            else:
                                confirmation = input('Confirm changes?(Y/N): ')
                                if confirmation.upper() == 'Y':
                                    break
                                elif confirmation.upper() == 'N':
                                    continue
                        parts_stock[result]['part_name'] = new_name
                        print('Name successfully updated')
                        continue                        
                    elif edit_table.title() == 'Brand':
                        while True:
                            new_brand = input('Enter new brand for this part: ')
                            if isinstance(new_brand,str) == False:
                                print('Please enter a string.')
                                continue
                            else:
                                confirmation = input('Confirm changes?(Y/N): ')
                                if confirmation.upper() == 'Y':
                                    break
                                elif confirmation.upper() == 'N':
                                    continue
                        parts_stock[result]['manufacturer_brand'] = new_brand
                        print('Brand successfully updated')
                        continue                        
                    elif edit_table.title() == 'Compatibility':
                         while True:
                            new_compatibility = input('Enter new compatibility for this part: ')
                            if isinstance(new_compatibility,str) == False:
                                print('Please enter a string.')
                                continue
                            else:
                                confirmation = input('Confirm changes?(Y/N): ')
                                if confirmation.upper() == 'Y':
                                    break
                                elif confirmation.upper() == 'N':
                                    continue
                         parts_stock[result]['part_compatibility'] = new_compatibility
                         print('Part compatibility successfully updated')
                         continue
                        
                    elif edit_table.title() == 'Quantity':
                        while True:
                            new_quantity = int(input('Enter new quantity for this part: '))
                            if new_quantity <= 0:
                                print('\nQuantity cannot be zero. Please try again\n')
                                continue
                            elif isinstance(new_quantity,int) == False:
                                print('Please enter an integer.')
                                continue
                            else:
                                confirmation = input('Confirm changes?(Y/N): ')
                                if confirmation.upper() == 'Y':
                                    break
                                elif confirmation.upper() == 'N':
                                    continue
                        parts_stock[result]['stock_quantity'] = new_quantity
                        print('Quantity successfully updated')
                        continue

                    elif edit_table.title() == 'Price':
                        while True:
                            new_price = float(input('Enter new price for this part (in $): '))
                            if new_price <= 0:
                                print('\nPrice cannot be zero. Please try again\n')
                                continue
                            elif isinstance(new_price,float) == False:
                                print('Please enter an integer.')
                                continue
                            else:
                                confirmation = input('Confirm changes?(Y/N): ')
                                if confirmation.upper() == 'Y':
                                    break
                                elif confirmation.upper() == 'N':
                                    continue
                        parts_stock[result]['price'] = new_price
                        print('Price successfully updated')
                        continue
                        
                    else:
                        print('Invalid input.')
            if choice == 2:
                break
            else:
                print('\nPlease enter the correct menu.\n')
                
        except ValueError:
            print('\nInvalid input.\n')

def purchaseParts():
    cart.clear() # Clear cart of any items
    while True:
        print('\nBuy menu.\n1. Purchase parts\n2. View Transactions\n3. Exit to main menu'
              )
        try:
            selection = int(input('Enter desired function [1-3]: '))
            if selection == 1:
                while True:
                    displayInventory()
                    p_number = int(input('Enter Part Number of part(s) that you would like to buy: '))
                    result = findPartsByPN(p_number)
                    int_check = isinstance(result,int) #check if index return is integer
                    if int_check == True:
                        print('\nPart exists!\n')
                        while True:
                            qty = int(input('Add item quantity: '))
                            available = stockChecker(qty,result)
                            if available == True:
                                break
                            else: 
                                print('\nQuantity requested exceeds available part quantity. Please enter correct amount\n') 
                                continue

                        if qty > 0 :
                            item = parts_stock[result].copy()
                            cart_length = len(cart)
                            available = stockChecker(qty,result)
                            if available == False:
                                print('\nQuantity requested exceeds available part quantity.\n') 
                                continue
                            found = 0
                            for i in range(cart_length):
                                # print(i)
                                if item['manufacturer_pn'] == cart[i]['manufacturer_pn']:
                                    found = 1
                                    index = i
                                    print(found)
                                    break
                        
                            if found == 1:
                                cart[index]['stock_quantity'] += qty
                            else:
                                item['stock_quantity'] = qty
                                cart.append(item)   
                            tables = PrettyTable()
                            tables.field_names = ['Manufacture P/N','Name','Brand','Compatibility', 'Quantity','Total Price ($)']
                            for i in range(len(cart)):
                                tables.add_row([cart[i]['manufacturer_pn'],cart[i]['part_name'],cart[i]['manufacturer_brand'],cart[i]['part_compatibility'],
                                cart[i]['stock_quantity'],cart[i]['price'] * cart[i]['stock_quantity']])
                            tables.align = 'c' #align center
                            print('\nPurchase Cart\n')
                            print(tables)
                        else:
                            print('Please enter stock that is more than zero.')
                            continue

                        add_more = input('Would you like to add more items? (Y/N): ')
                        if add_more.upper() == 'Y':
                            continue
                        elif add_more.upper() == 'N':
                            tables = PrettyTable()
                            tables.field_names = ['Manufacture P/N','Name','Brand','Compatibility', 'Quantity','Price ($)']
                            for i in range(len(cart)):
                                tables.add_row([cart[i]['manufacturer_pn'],cart[i]['part_name'],cart[i]['manufacturer_brand'],cart[i]['part_compatibility'],
                                cart[i]['stock_quantity'],cart[i]['price']])
                            tables.align = 'c' #align center
                            total_price = 0
                            for i in range(len(cart)):
                                total_price += cart[i]['price']
                            print(f'Grand total: ${total_price}\n')
                            perform_payment = input('Would you like to make a payment? (Y/N): ')
                            if perform_payment.upper() == 'Y':
                                while True:
                                    payment_type = input('Payment method [Debit/Credit/QR/Cash]: ') # The cashier will have the responsibility of checking if the payment has been done by the customer before entering the payment method
                                    if payment_type.upper() == ('DEBIT') or payment_type.upper() == ('CREDIT') or payment_type.upper() == ('QR') or payment_type.upper() == ('Cash'):
                                        transacation_date = datetime.datetime.now()
                                        transactions.append({
                                            'id': str(transacation_date.year)[2:4] + str(transacation_date.month) + # Auto generate id 
                                                    str(transacation_date.strftime('%d')) + str(len(transactions)),
                                            'items' : cart,
                                            'payment_type' : payment_type.upper(),
                                            'transaction_date': transacation_date, # Record date and time of transaction
                                            'grand_total': total_price
                                        })
                                        
                                        for i in range(len(parts_stock)): # decrement by stock purchased
                                            # print(parts_stock[i])  
                                            for j in range(len(cart)):
                                                if  parts_stock[i]['manufacturer_pn'] == cart[j]['manufacturer_pn']:
                                                    parts_stock[i]['stock_quantity'] -= cart[j]['stock_quantity']
                                        print('\nPurchase successful!\n')
                                        # print(transactions)
                                        break
                                    else:
                                        print('Please enter correct payment method')
                                        continue

                            elif perform_payment.upper() == 'N': #Cancel purchase
                                print('\nPurchase cancelled.\n')
                                cart.clear()
                                continue
                        break
                    else:
                        print('Part not found.')
                        continue
            elif selection == 2:
                
                tables = PrettyTable()
                tables.field_names = ['Transaction ID','Transaction date','Payment Method','Grand total ($)']
                
                for i in range(len(transactions)):
                    tables.add_row([transactions[i]['id'],transactions[i]['transaction_date'],transactions[i]['payment_type'],transactions[i]['grand_total']])
                tables.align = 'c' #align center  
                print(tables)
                continue             
            elif selection == 3:
                break
            else:
                print('Please enter the correct menu selection')        
        except ValueError:
            print('\nInvalid Input.\n')

def stockChecker(qty,index): # to check if quantity is adequate to the amount requested by the customer
    if qty > parts_stock[index]['stock_quantity']:
        return False
    else:
        return True

def menu(): # Display main menu of the program
    print('\n\t\tWelcome to Harney Autoparts and Supplies!\n')
    print('Please select a menu: ')
    print('1. View inventory') #read
    print('2. Add new parts') #create
    print("3. Update parts") #update
    print("4. Delete stock parts") #delete
    print('5. Purchase parts') #purchase
    print('6. Exit program') #Terminate program

def main(): # Where the program starts
    while True:
        menu()
        try:
            choice = int(input('Please select a menu [1-6]: '))
            if choice == 6:
                print('\nThank you!')
                break
            else:
                if choice == 1:
                    viewParts()
                elif choice == 2:
                    add_parts()
                elif choice == 3:
                    updateParts()
                elif choice == 4:
                    deleteParts()
                elif choice == 5:
                    purchaseParts()
                    continue
                else:
                    print('\nPlease enter the correct menu')
        except ValueError:
            print('\nPlease enter only integers.')

if __name__ == "__main__":
    main()