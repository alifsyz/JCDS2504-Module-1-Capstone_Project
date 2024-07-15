from prettytable import PrettyTable
parts_stock = [{'manufacturer_pn': 1700231, 'part_name': 'Lower Intake Boot', 'manufacturer_brand': 'Uro Parts', 'part_compatibility': {'car_manufacturer': 'BMW', 'car_model':'3 Series'},
                'stock_quantity' : 4, 'price': 80.00}, {'manufacturer_pn': 1700232, 'part_name': 'CV Axle', 'manufacturer_brand': 'Tokico', 'part_compatibility': 'Honda',
                'stock_quantity' : 2, 'price': 120.00},{'manufacturer_pn': 1700233, 'part_name': 'Main Fuel Pump', 'manufacturer_brand': 'Bosch', 'part_compatibility': 'Mercedes-Benz',
                'stock_quantity' : 10, 'price': 52.00}, {'manufacturer_pn': 1700234, 'part_name': 'Left Lower Control Arm', 'manufacturer_brand': 'Lemforder', 'part_compatibility': 'BMW',
                'stock_quantity' : 6, 'price': 100.00}, {'manufacturer_pn': 1700235, 'part_name': 'Ignition Coil', 'manufacturer_brand': 'Bremi', 'part_compatibility': 'Toyota',
                'stock_quantity' : 14, 'price': 35.00}

]

# print(parts_stock[0]['part_compatibility']['car_model'])
cart = []

def viewInventory():
    print('\n\t\t\t\t\tSpare Parts Inventory\n') 
    tables = PrettyTable()
    tables.field_names = ['Index','Manufacture P/N','Name','Brand','Compatibility', 'Quantity','Price ($)']
    for i in range(len(parts_stock)):
        tables.add_row([i+1,parts_stock[i]['manufacturer_pn'],parts_stock[i]['part_name'],parts_stock[i]['manufacturer_brand'],parts_stock[i]['part_compatibility'],
                        parts_stock[i]['stock_quantity'],parts_stock[i]['price']]) #inserting list items into pretty table
    tables.align = 'c' #align center
    print(tables)

def deleteParts():
    viewInventory()
    while True:
        try:
            part_delete = (int(input('\nPlease choose index of parts you want to delete: ')))-1
            length = len(parts_stock)
            if part_delete not in range(length):
                print('\nIndex not available.')
            else:
                break
        except ValueError:
            print('\nPlease enter only integers.')
    print(f'\nPart Number {parts_stock[part_delete] ["manufacturer_pn"]} has been successfully deleted')
    parts_stock.pop(part_delete)
    # viewInventory()
def add_parts(): #Need to check for duplicate partnumber
    print('Adding new part to inventory. (Type "exit" to cancel) \n')
    manufacturer_pn = int(input('Enter part number : '))
    part_name = input('Enter part name : ')
    part_manufacturer = input('Enter part manufacturer : ')
    part_compatibility = input('Enter part compatibility: ')
    while True:
        try:
            stock_update = int(input('\nEnter quantity of parts : '))
            if stock_update < 0:
                print('\nPlease enter the correct amount.')
            else:
                break
        except ValueError:
            print('\nPlease enter an integer.')
    while True:
        try:
            part_price = float(input('\nPlease enter price: '))
            if part_price < 0:
                print('\nPlease enter the correct amount.')
            else:
                break
        except ValueError:
            print('\nPlease enter  ')

    parts_stock.append({'manufacturer_pn': manufacturer_pn, 'part_name': part_name, 'manufacturer_brand': part_manufacturer, 'part_compatibility': part_compatibility,
                'stock_quantity' : stock_update, 'price': 80.00})

    viewInventory()

def updateParts():
    

def menu(): #main menu of the program
    print('\nWelcome to Harney Parts and Supplies!')
    print('Please select a menu: ')
    print('1. View inventory') #read
    print('2. Add new parts') #create
    print("3. Update parts") #update
    print("4. Delete stock parts") #delete
    print('5. Purchase parts')
    print('6. Exit program') 

while True:
    menu()
    try:
        choice = int(input('Please enter menu number: '))
        if choice == 6:
            print('\nThank you!')
            break
        else:
            if choice == 1:
                viewInventory()
                detail = input('Would you like to view parts compatibility? (Y/N): ')
                if detail.upper() == 'Y':
                    viewPartsDetail()
                elif detail.upper() == 'N':
                    continue
                else:
                    print('\nInvalid input. Please try again.')
            elif choice == 2:
                add_parts()
            elif choice == 3:
                updateParts()
            elif choice == 4:
                deleteParts()
            elif choice == 5:
                buy_parts()
            else:
                print('\nPlease enter the correct menu')
    except ValueError:
        print('\nPlease enter only integers.')