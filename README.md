# Simple CRUD program for an Automotive Parts Store
### CRUD is short for Create, Read, Update, and Delete. It can be found in many different bussiness applications and is essential to many. 
### Context: Small to medium spareparts shop, used for parts purchasing (operated by Cashier) or inventory management (operated by Stockist)
### Part attributes:
#### manufacturer_pn: unique numeric (integer) data specific to a certain part. Given by the part manufacturer, so manufacturer is responsible for any mistakes 
#### part_name: string. possible to have duplicates since some cars have the same parts (eg. all cars have spark plugs)
#### manufacturer_brand: string data. the name of the company that manufactured the part
#### part_compatibility: string data. to check part compatibility with car manufacturer
#### stock_quantity: integer
#### price: float. Is in USD
### Extra features:
#### - Purchase history for warranty claim
#### - Sort by a defined attribute using bubble sort
#### - Automatic ID of purchasing history
